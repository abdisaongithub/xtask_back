from django.contrib.auth.models import User
from .models import Collection, Task, Collaborator, Tag
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    collections = serializers.PrimaryKeyRelatedField(many=True, queryset=Collection.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'collections')
        # exclude = ['password']


class TaskSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True,)
    # name = serializers.CharField(required=True, max_length=255, min_length=2)
    # detail = serializers.CharField(max_length=255, min_length=10)
    # isChecklist = serializers.BooleanField(default=False)
    # done = serializers.BooleanField(default=False)
    # priority = serializers.IntegerField(min_value=1, max_value=5, default=1)
    # collection = serializers.PrimaryKeyRelatedField(read_only=False, many=False)

    class Meta:
        model = Task
        fields = ('id', 'name', 'detail', 'isChecklist', 'done', 'priority')


class CollaboratorSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(many=False,)

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


class CollectionSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'name', 'description', 'color', 'starred', 'updated')


class TagSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Tag
        fields = ('id', 'name', 'tasks')

