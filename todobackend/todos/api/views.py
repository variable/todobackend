# encoding: utf-8
from rest_framework import viewsets
from todobackend.todos.api.serializers import TODOItemSerializer
from todobackend.todos.models import TODOItem

class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TODOItemSerializer

    @property
    def session_id(self):
        if not self.request.session.session_key:
            self.request.session.save()
        return self.request.META.get('HTTP_SESSION_ID') or self.request.session.session_key

    def get_queryset(self):
        return TODOItem.objects.filter(session_id=self.session_id)

    def perform_create(self, serializer):
        serializer.save(session_id=self.session_id)
        TODOItem.objects.trim_rows()
