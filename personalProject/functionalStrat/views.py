from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return HttpResponse('home page')
