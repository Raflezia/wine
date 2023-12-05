# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world")
from .models import *
from django.shortcuts import render #для вывозва html шаблона
from django.http import HttpResponse

# def index(request):
#     return render(request, "wino/index.html")

def index(request):
    # bbs = bochka.objects.order_by('-mesto')
    # return render(request, "wino/mainS.html", {'bbs': bbs})
    return render(request, "wino/mainS.html")

def sortW(request):   
    ws=wine_sort.objects.order_by('-title')
    bbs = bochka.objects.order_by('-mesto')
    b=0
    return render(request, "wino/wineSort.html",{'sw': ws,'bbs':bbs})

def barrelwine(request):   
    bbs = bochka.objects.order_by('-mesto')
    return render(request, "wino/index.html", {'bbs': bbs})
    
#def index(request):
#     return HttpResponse('')

# def index(request):
#     return render(request,'wino/index.html') 