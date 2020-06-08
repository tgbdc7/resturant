from django.http import HttpResponse
from django.shortcuts import render
from menu.models import Dish


def hello(request, name):
    return HttpResponse("Hello {}!".format(name))


def dishes(request):
    dishes = Dish.objects.all()
    ctx ={
        "dishes":dishes
    }
    return render(request, 'dishes.html', context=ctx)
