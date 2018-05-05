from django.db import models

from gallery.utils import minify_name


def image_path(instance, filename):
    return '{0}/{1}.jpeg'.format(instance.user, minify_name(instance.name))


def image_medium_path(instance, filename):
    return '{0}/{1}_medium.jpeg'.format(instance.user, minify_name(instance.name))


def image_small_path(instance, filename):
    return '{0}/{1}_small.jpeg'.format(instance.user, minify_name(instance.name))


class Image(models.Model):
    name = models.CharField(max_length=64)
    user = models.CharField(max_length=64)

    class Meta:
        abstract = True


class UploadedImage(Image):
    file = models.ImageField(upload_to=image_path)
    file_medium = models.ImageField(upload_to=image_medium_path)
    file_small = models.ImageField(upload_to=image_small_path)
