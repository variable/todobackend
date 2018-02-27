# encoding: utf-8
from rest_framework import serializers
from todobackend.todos.models import TODOItem


class TODOItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TODOItem
