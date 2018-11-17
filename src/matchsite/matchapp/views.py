from django.shortcuts import render
from django.http import HttpResponse, Http404
from matchapp.models import Member, Profile, Hobby

def index(request):
    return HttpResponse("Hello match app GIT")

def login(request):
    pass

def register(request):
    pass

def signup(request):
    pass
