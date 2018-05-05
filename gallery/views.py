from django.shortcuts import render, HttpResponse

from gallery.forms import UploadedImageForm


def upload(request):
    form = UploadedImageForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()

    return HttpResponse('')
