from django.shortcuts import render, HttpResponse

from gallery.forms import ImageForm


def upload(request):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        print(form)
    return HttpResponse('')
