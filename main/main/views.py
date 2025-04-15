
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Game



def index(request: HttpRequest):
    return render(request, "index.html")


def main_page(request: HttpRequest):
    return render(request,'main_page.html')


def register(request: HttpRequest):
    return render(request, "register.html")
