from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('This is the profile page.')


def login(request):
    return HttpResponse('This is the login page.')


def register(request):
    return HttpResponse('This is the register page.')
