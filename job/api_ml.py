import json

from django.contrib.auth.models import User
from django.db.models import Q, Count, Max, FilteredRelation
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from job.models import Job, Skill
from job.serializers import JobSerializer, JobSerializerAllField, JobUpdateSerializer, JobSerializerAdmin, \
    UserSerializer
from p7.models import is_professional, populate_user_info_request, populate_user_info_querydict
from p7.pagination import P7Pagination
from p7.permissions import StaffPermission
from job.utils import job_slug_generator

class JobPublisherList(ListAPIView):
    permission_classes = [StaffPermission]
    required_privilege = 'job.add_job'
    queryset = User.objects.filter(groups__name='Publisher')
    serializer_class = UserSerializer


class MlJobAPI(RetrieveAPIView):
    required_privilege = 'job.view_job'
    permission_classes = [StaffPermission]
    serializer_class = JobSerializerAllField

    def get_object(self):
        return get_object_or_404(
            Job.objects.filter(
                job_id = self.kwargs['id']
            ).select_related(
                'company'
            ).prefetch_related(
                'job_skills'
            )
        )


class JobCreateView(CreateAPIView):
    required_privilege = 'job.add_job'
    permission_classes = [StaffPermission]
    serializer_class = JobSerializerAdmin

    def post(self, request, *args, **kwargs):
        populate_user_info_request(request, False, False)
        return super().post(request, *args, **kwargs)


class MlJobUpdateView(UpdateAPIView):
    required_privilege = 'job.change_job'
    permission_classes = [StaffPermission]
    serializer_class = JobSerializerAdmin

    def put(self, request, *args, **kwargs):
        populate_user_info_request(request, True, False)
        return super().put(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(
            Job.objects.filter(
                job_id = self.kwargs['id']
            )
        )

class AdminJobList(ListAPIView):
    # required_privilege = 'job.view_job'
    # permission_classes = [StaffPermission]
    pagination_class = P7Pagination
    serializer_class = JobSerializerAllField

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        datePosted = request.GET.get('datePosted')
        datePublished = request.GET.get('datePublished')
        dateCreated = request.GET.get('dateCreated')
        status = request.GET.get('status')
        creator_type = request.GET.get('creator_type')
        not_creator_type = request.GET.get('not_creator_type')
        job_type = request.GET.get('job_type')
        category = request.GET.get('category')
        applicationDeadline = request.GET.get('application_deadline')
        modified_at = request.GET.get('modified_at')

        queryset = Job.objects.all()

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query) |
                Q(company_id__name__icontains=query) |
                Q(additional_requirements__icontains=query)
            )

        if category:
            queryset = queryset.filter(job_category=category)

        if creator_type:
            queryset = queryset.filter(creator_type=creator_type)

        if not_creator_type:
            queryset = queryset.exclude(creator_type=creator_type)

        if status:
            queryset = queryset.filter(status=status)

        if datePosted:
            queryset = queryset.filter(post_date__gt=datePosted)

        if dateCreated:
            queryset = queryset.filter(created_at__gt=dateCreated)

        if datePublished:
            queryset = queryset.filter(publish_date__gt=datePublished)

        if applicationDeadline:
            queryset = queryset.filter(
                Q(application_deadline__isnull=True) | Q(application_deadline__gte=applicationDeadline))

        if job_type:
            queryset = queryset.filter(job_type=job_type)

        if modified_at:
            queryset = queryset.filter(modified_at=modified_at)

        return queryset

class SlugRegenerateAPI(APIView):
    required_privilege = 'job.change_job'
    permission_classes = [StaffPermission]
    def put(self, request):
        requested_job_ids : list = request.data["job_id"]
        processed_jobs = []
        failed_jobs = []
        for job_id in requested_job_ids:
            try:
                job = Job.objects.get(job_id=job_id)
                generated_slug = job_slug_generator(job)
                job.slug = generated_slug
                job.save()
                processed_jobs.append({
                    "id": job_id,
                    "slug": job.slug
                })
            except:
                failed_jobs.append(job_id)

        return Response({
            'processed_jobs': processed_jobs,
            'failed_jobs': failed_jobs
        })

class JobBulkCreateView(APIView):
    required_privilege = 'job.add_job'
    permission_classes = [StaffPermission]
    serializer_class = JobSerializerAdmin
    def post(self, request, *args, **kwargs):
        job_list = json.loads(request.body)
        if 20 >= len(job_list) > 0:
            success = []
            errors = []
            warning = []

            for j in job_list:
                try:

                    j_obj = Job.objects.filter(job_id = j["job_id"])
                    if j_obj.exists():
                        errors.append({"id":j["job_id"], "error" : "Exist"})
                    else:
                        if "job_skills" in j.keys():
                            skills = j["job_skills"]
                            del j['job_skills']
                        else:
                            skills = None

                        job_obj = Job(**j)
                        populate_user_info_querydict(request, j, False, False)
                        job_obj.save()

                        if skills:
                            for skill in skills:
                                try:
                                    skill_obj = Skill.objects.get(id=skill)
                                    job_obj.job_skills.add(skill_obj)
                                except Skill.DoesNotExist:
                                    warning.append({"id":j["job_id"], "error" : f"Skill {skill} not exist but job was added"})
                        success.append(j["job_id"])
                except Exception as ex:
                    #errors.append({"id": j["job_id"] if "job_id" in j.keys() else None, "error": str(ex)})
                    errors.append({"id": j.get("job_id") , "error": str(ex)})

                result = {
                    "success" : success,
                    "warning" : warning,
                    "error" : errors
                }
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response({'Error' : 'Job list size should be 1-20'})

