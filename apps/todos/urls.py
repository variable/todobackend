# encoding: utf-8
from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.todos.api.urls')),
]

