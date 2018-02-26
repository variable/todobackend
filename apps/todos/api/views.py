# encoding: utf-8
from django.db.models import Max
from rest_framework import viewsets
from apps.todos.api.serializers import TODOItemSerializer
from apps.todos.models import TODOItem

class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TODOItemSerializer

    @property
    def session_id(self):
        if not self.request.session.session_key:
            self.request.session.save()
        return self.request.META.get('session_id') or self.request.session.session_key

    def get_queryset(self):
        return TODOItem.objects.filter(session_id=self.session_id)

    def perform_create(self, serializer):
        serializer.save(session_id=self.session_id)
        TODOItem.objects.trim_rows()

    def perform_update(self, serializer):
        serializer.save(session_id=self.session_id)
