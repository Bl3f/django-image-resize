from django.shortcuts import render, HttpResponse

from gallery.forms import ImageForm


def upload(request):
    form = ImageForm(data=request.POST)
    return HttpResponse('')
