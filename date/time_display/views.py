from django.shortcuts import render
from time import gmtime, strftime
import datetime
from django.utils import timezone


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)


def format(request):
    context = {
        "time": datetime.datetime.now()
    }
    return render(request, 'index.html', context)


def format1(request):
    context = {
        "time": timezone.now()
    }
    return render(request, 'index.html', context)
