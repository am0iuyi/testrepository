
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Game


# def html(request):
#     return HttpResponse(
#         '''<h1> алфавит </h1>
#         <a href = 'https://avatars.mds.yandex.net/i?id=6e6a84f5253b938007c377ccd2d708e31a02c24a-10231558-images-thumbs&n=13'> алфавит </a>
#         <br></br>
#         <img src='https://cdn1.ozone.ru/multimedia/1018056524.jpg' wide='100' height='200' >
#         <h2> Ру́сский алфави́т (ру́сская а́збука) — алфавит русского языка, включающий 33 буквы.</h2>
#         <p> Алфавит создали в 863году, братья кирилл и мефодий, по указц византийского императора
#         <h3> состав алфавита</h3>
#         </p> a б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я </p>
#         <h1> всем спасибо за внимание <h1>
#         '''
#     )
def index(request: HttpRequest):
    result=0

    if request.POST:
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        number3 = int(request.POST.get('number3'))
        result = f's vas {number1+number2+number3} deneg'


    return render(request, "index.html",{"result":result,})


def test(request: HttpRequest):
    print(*Game.objects.all())
    return ""