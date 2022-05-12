from django.http import HttpResponse
from django.shortcuts import render

from .detect import detect

# Create your views here.

def index(request):
  prediction = detect(r"D:\Coding\Competitions\HackMait\lwd\main\static\street.jpg")
  return render(request, "index.html", prediction)
