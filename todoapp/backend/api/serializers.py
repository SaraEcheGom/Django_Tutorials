from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['title', 'memo', 'created', 'completed']

class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'completed']
        read_only_fields = ['id']