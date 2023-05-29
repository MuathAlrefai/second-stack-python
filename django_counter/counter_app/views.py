from django.shortcuts import render, redirect

def index(request):
    # checks if there's a previous saved session or not, if not it creates one
    if 'counter' not in request.session:
        request.session['counter'] = 0
    #increment the session key by 1 with each site reload
    request.session['counter'] += 1
    session = request.session['counter']
    context = {
        "counter": session
    }
    return render(request, 'index.html', context)

# to clear the session key (resets back to 1)
def destroy(request):
    del request.session['counter']
    return redirect('/')

def addNum(request):
    request.session['counter'] +=1
    return redirect('/')

def addByInputs(request):
    x = request.POST['user_input']
    request.session['counter'] += int(x)-1
    return redirect('/')