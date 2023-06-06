from django.shortcuts import render, redirect
from . import models

def root(request):
    return redirect('/shows')
def shows(request):
    context = {
        "SHOWS": models.getShows_model(request)
    }
    return render(request, 'shows.html', context)
def renderAddShow(request):
    return render(request, 'addShow.html')
def addShow(request):
    models.addShow_model(request)
    #! how to make it redirect to show info page??!!
    return redirect('/shows')
def showInfo(request, showID):
    context = {
        "SHOW_INFO": models.getShowInfo_model(request, showID)
    }
    return render(request, 'showInfo.html', context)
def deleteShow(request, showID):
    models.deleteShow_model(request, showID)
    return redirect('/shows')
def renderEditShow(request, showID):
    context = {
        "SHOW_INFO": models.getShowInfo_model(request, showID)
    }
    return render(request, 'editShow.html', context)
def editShow(request, showID):
    models.editShow_model(request, showID)
    #! how to make it redirect to show info page??!!
    return redirect('/shows')