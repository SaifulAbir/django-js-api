from io import BytesIO

from ckeditor.fields import RichTextField
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from PIL import Image
from p7.models import P7Model, populate_time_info
from resources import strings_job

class CareerAdvice(P7Model):
    title = models.CharField(max_length=64)
    short_description = models.TextField()
    description = RichTextField()
    author = models.CharField(max_length=50)
    thumbnail_image = models.ImageField(upload_to='images/', null=True)
    featured_image = models.ImageField(upload_to='images/', blank=True, null=True)
    posted_at = models.DateTimeField(blank=False,null=False)


    class Meta:
        verbose_name = strings_job.CAREER_VERBOSE_NAME
        verbose_name_plural = strings_job.CAREER_VERBOSE_NAME_PLURAL
        db_table = 'career_advices'

    def __str__(self):
        return self.title

def resized_image(sender, instance: CareerAdvice, *args, **kwargs):

    ## Thumbnail image resize start
    im = instance.thumbnail_image
    im = Image.open(im)
    im = im.convert('RGB')
    ratio = im.width/im.height
    thumbnail_resized_width = settings.CEREAR_ADVICE_THUMBNAIL_DEFAULT_IMAGE_WIDTH
    resized_im = im.resize((thumbnail_resized_width, round(thumbnail_resized_width/ratio)))
    img_io = BytesIO()
    resized_im.save(img_io, format='JPEG', quality=100)
    img_content = ContentFile(img_io.getvalue(), 'career_advice_thumbnail.jpg')
    instance.thumbnail_image = img_content
    ## Thumbnail image resize end

    ## Featured image resize start
    im = instance.featured_image
    im = Image.open(im)
    im = im.convert('RGB')
    ratio = im.width/im.height
    thumbnail_resized_width = settings.CEREAR_ADVICE_FEATURED_DEFAULT_IMAGE_WIDTH
    resized_im = im.resize((thumbnail_resized_width, round(thumbnail_resized_width/ratio)))
    img_io = BytesIO()
    resized_im.save(img_io, format='JPEG', quality=100)
    img_content = ContentFile(img_io.getvalue(), 'career_advice_featured.jpg')
    instance.featured_image = img_content
    ## Thumbnail image resize end

pre_save.connect(populate_time_info, sender=CareerAdvice)
pre_save.connect(resized_image, sender=CareerAdvice)
