from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Person
def home(request):
    obj=Place.objects.all() # to fetch all objects from table place
    obj1=Person.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

