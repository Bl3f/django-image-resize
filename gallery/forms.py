from io import StringIO, BytesIO
import PIL

from django.core.files.base import ContentFile, BytesIO
from django.forms import ModelForm

from gallery.models import Image, UploadedImage


def resize(image, factor):
    w, h = image.size

    medium = image.resize((int(w / factor), int(h / factor)), PIL.Image.ANTIALIAS)
    buffer = BytesIO()
    medium.save(buffer, 'JPEG')
    return ContentFile(buffer.getvalue())


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'user']


class UploadedImageForm(ImageForm):
    def save(self, commit=True):
        instance = super(UploadedImageForm, self).save(commit=False)

        instance.file.file.seek(0)
        image = PIL.Image.open(instance.file.file)

        instance.file_medium.save('__', content=resize(image, 2))
        instance.file_small.save('__', content=resize(image, 5))

        if commit:
            instance.save()
        return instance

    class Meta:
        model = UploadedImage
        fields = ImageForm.Meta.fields + ['file']
