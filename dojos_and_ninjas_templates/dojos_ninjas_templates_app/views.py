from django.shortcuts import render, redirect
from . import models

def index(request):
    context = {
        "DOJO": models.dojoRender,
        "NINJA": models.ninjaRender
    }
    return render(request, 'index.html', context)
def dojo(request):
    models.dojoAdd(request)
    return redirect('/')
def ninja(request):
    models.ninjaAdd(request)
    return redirect('/')
