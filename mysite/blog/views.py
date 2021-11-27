import os
from django.shortcuts import render
from blog.models import Images

# Create your views here.

def home(request):
    return render(request, 'blog/index.html')


def about(request):
    with open('./blog/templates/blog/about.txt') as f:
        data = f.read().splitlines()
    context = {'data': data}
    return render(request, 'blog/about.html', context)


def contacts(request):
    with open('./blog/templates/blog/contact.txt') as f:
        data = f.read().splitlines()
    context = {'data': data}
    return render(request, 'blog/contacts.html',context=context)


def galary(request):
    images = Images.objects.all()
    context = {"images": images}
    return render(request, 'blog/galary.html', context=context)

