from django.shortcuts import render
from time import gmtime, strftime

def currentTime(request):
    time_dic = {
        "time": strftime("%Y-%m-%d %I:%M %p", gmtime())
    }
    return render(request, 'index.html', time_dic)
