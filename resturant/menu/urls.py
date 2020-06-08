from django.urls import path, include

from menu.views import hello,dishes

urlpatterns = [
    path('hello/<str:name>', hello),
    path('dishes/', dishes),
]