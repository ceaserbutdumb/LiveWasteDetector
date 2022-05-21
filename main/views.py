from django.http import HttpResponse
from django.shortcuts import render

from .ml.detect import predict

# Create your views here.

def index(request):
  # prediction = predict(r"D:\Coding\Competitions\HackMait\lwd\main\static\street.jpg")
  return render(request, "index.html")

def detect(request, vid_id):
  prediction = predict(int(vid_id))
  return render(request, "detect.html", {"vid_id": vid_id, "class": prediction["class"], "probibility": prediction["probibility"], "link": prediction["links"]})
