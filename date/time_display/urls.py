from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('format', views.format),
    path('format1', views.format1)
]
