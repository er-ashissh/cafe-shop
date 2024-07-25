from django.shortcuts import render
from django.views import View
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    template = loader.get_template('webs/users/user_register.html') 
    return HttpResponse(template.render())


@csrf_exempt
def activation(request):
    template = loader.get_template('webs/users/user_activation.html') 
    return HttpResponse(template.render())


@csrf_exempt
def login(request):
    template = loader.get_template('webs/users/user_login.html') 
    return HttpResponse(template.render())


@csrf_exempt
def about(request):
    template = loader.get_template('webs/users/user_about.html') 
    return HttpResponse(template.render())


