from django.db import models

from gallery.utils import minify_name


def image_path(instance, filename):
    return '{0}/{1}.jpeg'.format(instance.user, minify_name(instance.name))


class Image(models.Model):
    name = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    file = models.ImageField(upload_to=image_path)