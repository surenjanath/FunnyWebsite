from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import RoastMe


import os
from pathlib import Path
# Create your views here.
def Home(request) :
    BASE_DIR = Path(__file__).resolve().parent.parent

    roasts          = RoastMe.objects

    context = {
               'Roasts' : roasts,

    }
    x = len(roasts.all())


    return render(request,'Roast/home.html', context)
