from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello, world!')


def hello_template(request):
    return render(request, 'hello.html', {'name': 'world'})


def hello_url_params(request):
    name = request.GET.get('name', 'world')
    return render(request, 'hello.html', {'name': name})


def hello_path_params(request, name):
    return render(request, 'hello.html', {'name': name})


def hello_post(request):
    request.POST.get('name', 'world')
