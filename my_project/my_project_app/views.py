from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework.decorators import api_view
# Create your views here.


def home(request):
    theIndex = open('static/index.html').read()
    return HttpResponse(theIndex)