from django.forms import ModelForm

from gallery.models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'user', 'file']
