import json

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer
from p7.models import populate_user_info


class FeedbackCreateAPI(CreateAPIView):
    permission_classes = []
    serializer_class = FeedbackSerializer

    def post(self, request, *args, **kwargs):
        feedback_data = json.loads(request.body)
        feedback_obj = Feedback(**feedback_data)
        populate_user_info(request, feedback_obj, False, False)
        feedback_obj.save()
        return Response(HTTP_200_OK)