import json
from django.shortcuts import render
from django.core import serializers
from django.http.response import JsonResponse
from .models import Person

def index(request):
    return render(request, 'index.html', {})

def getdata(request):
    search      = request.POST.get('search');
    personList  = []
    if search == '':
        persons = Person.objects.all()
    else:
        persons = Person.objects.filter(name__icontains=search)

    for person in persons:
        personList.append(
            {
                'pk'        :person.pk, 
                'name'      :person.name, 
                'surname'   :person.surname
            }
        )

    return JsonResponse({'persons':personList});

