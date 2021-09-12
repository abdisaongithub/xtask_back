from django.contrib.auth.models import User
from .models import Collection, Task, Collaborator
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        # exclude = ['password']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'detail', 'isChecklist', 'done', 'priority')


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = ('id', 'user', 'collection')


class CollectionSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(
        many=True,
        read_only=True
    )

    collaborators = CollaboratorSerializer(
        many=True,
        read_only=True
    )

    user = UserSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = Collection
        fields = ('id', 'name', 'description', 'color', 'starred', 'tasks', 'collaborators', 'user')




