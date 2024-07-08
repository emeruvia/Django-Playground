from django.urls import path, include
from . import views

#URLConfs
urlpatterns = [
    path('hello/', views.say_hello)
]
