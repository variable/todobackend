# encoding: utf-8
from rest_framework import serializers
from todobackend.todos.models import TODOItem


class TODOItemSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['session_id']
        model = TODOItem
