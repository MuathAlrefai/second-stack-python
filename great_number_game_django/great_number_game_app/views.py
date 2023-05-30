from django.shortcuts import render, HttpResponse
import random

def index(request):
    if 'randomNum' not in request.session:
        request.session['randomNum'] = random.randint(1,100)
    return render(request,'index.html')

def answer(request):
    user_input = request.POST['user_number']

    if user_input == request.session['randomNum']:
        return HttpResponse("Correct, wow you're a (شنّيص من الاخر)")
    else:
        return HttpResponse("Sorry, wrong answer, good luck next time!")