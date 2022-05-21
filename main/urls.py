from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detect/<vid_id>', views.detect, name='detect'),
]