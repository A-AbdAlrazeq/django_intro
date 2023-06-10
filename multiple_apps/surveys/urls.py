from django.urls import path, include
from . import views
urlpatterns = [
    path('/surveys', views.index),
    path('/surveys/new', views.new),

]
