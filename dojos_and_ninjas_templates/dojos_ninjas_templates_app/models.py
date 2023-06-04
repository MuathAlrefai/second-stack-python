from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

def dojoAdd(request):
    dojoName = request.POST['dojoName']
    dojoCity = request.POST['dojoCity']
    dojoState = request.POST['dojoState']
    some_dojo = Dojo.objects.create(name = dojoName, city = dojoCity, state = dojoState)
    return some_dojo
def ninjaAdd(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    ninjaDojo = request.POST['ninjaDojo']
    dojo_name = Dojo.objects.get(name = ninjaDojo)
    some_ninja = Ninja.objects.create(first_name = firstName, last_name = lastName, dojo = dojo_name)
    return some_ninja

def dojoRender():
    DOJO = Dojo.objects.all()
    return DOJO
def ninjaRender():
    NINJA = Ninja.objects.all()
    return NINJA
