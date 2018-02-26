# encoding: utf-8
from rest_framework import routers
from apps.todos.api.views import TodoItemViewSet


router = routers.SimpleRouter()
router.register(r'todos', TodoItemViewSet, base_name='todo')

urlpatterns = router.urls
