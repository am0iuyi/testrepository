
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Game



def index(request: HttpRequest):
    result=0

    if request.POST:
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        number3 = int(request.POST.get('number3'))
        result = f's vas {number1+number2+number3} deneg'


    return render(request, "index.html",{"result":result,})


def main_page(request: HttpRequest):
    return render(request,'main_page.html')