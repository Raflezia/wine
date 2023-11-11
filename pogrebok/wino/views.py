# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world")
from .models import *
from django.shortcuts import render


# def index(request):
#     return render(request, "wino/index.html")

def index(request):
    bbs = bochka.objects.order_by('-mesto')
    return render(request, "wino/index.html", {'bbs': bbs})

