from django.shortcuts import render
from .models import *

def home(request):

    return render(request, 'wiki/home.html')


def block_page(request):
    return render(request, 'wiki/block_page.html')