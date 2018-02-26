# encoding: utf-8
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', include('todobackend.todos.api.urls')),
]

