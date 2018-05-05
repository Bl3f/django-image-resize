from django.db import models

from gallery.utils import minify_name


def image_path(instance, filename, size):
    return '{0}/{1}{2}.jpeg'.format(instance.user, minify_name(instance.name), size)


def image_normal_path(instance, filename):
    return image_path(instance, filename, '')


def image_medium_path(instance, filename):
    return image_path(instance, filename, '_medium')


def image_small_path(instance, filename):
    return image_path(instance, filename, '_small')


class Image(models.Model):
    name = models.CharField(max_length=64)
    user = models.CharField(max_length=64)

    class Meta:
        abstract = True


class UploadedImage(Image):
    file = models.ImageField(upload_to=image_normal_path)
    file_medium = models.ImageField(upload_to=image_medium_path)
    file_small = models.ImageField(upload_to=image_small_path)
