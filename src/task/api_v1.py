from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.utils import json
from .models import Collection, Collaborator, Task, Tag
from .serializers import (
    CollectionSerializer,
    CollaboratorSerializer,
    TaskSerializer,
    CollectionSerializerShort,
    TagSerializer,
)


class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.filter(user=2)
    serializer_class = CollectionSerializer


class CollectionListViewShort(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializerShort


class CollectionCreateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        if 'name' not in request.data:
            return Response(
                data=json.dumps({'error': 'Name is required'}),
                status=status.HTTP_400_BAD_REQUEST)
        collection = Collection(name=request.data['name'], user_id=2, **kwargs)
        collection.save()
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)


class CollectionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollaboratorCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        if 'user' not in request.data:
            return Response(
                json.dumps({'error': 'user is required'}),
                status=status.HTTP_400_BAD_REQUEST
            )
        collection = Collection.objects.get(pk=kwargs['pk'])
        collaborator = Collaborator(user_id=request.data['user'], collection=collection)
        collaborator.save()
        serializer = CollaboratorSerializer(collaborator)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CollaboratorUpdateView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        if 'user' not in request.data:
            return Response(
                json.dumps({'error': 'user is required'}),
                status=status.HTTP_400_BAD_REQUEST)
        collaborator = Collaborator.objects.get(pk=kwargs['id'])
        serializer = CollaboratorSerializer(instance=collaborator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollaboratorDeleteView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        collaborator = Collaborator.objects.get(pk=kwargs['id'])
        collaborator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        task = Task.objects.filter(collection=kwargs['pk'])
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        collection = Collection.objects.get(pk=kwargs['pk'])
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = Task(
                isChecklist=serializer.validated_data['isChecklist'],
                name=serializer.validated_data['name'],
                detail=serializer.validated_data['detail'],
                done=serializer.validated_data['done'],
                priority=serializer.validated_data['priority'],
                collection=collection,
            )
            task.save()
            return Response(data=serializer.initial_data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TaskUpdateView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        instance = Task.objects.get(pk=kwargs['id'])
        serializer = TaskSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TaskDeleteView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['id'])
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


@api_view()
def searchApiView(request, *args, **kwargs):
    if 'key' not in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    key = request.data['key']
    collection_name = Collection.objects.filter(name__contains=key)
    collection_description = Collection.objects.filter(description__contains=key)
    task_name = Task.objects.filter(name__contains=key)

    serialized_coll_name = CollectionSerializer(data=collection_name, many=True)
    serialized_coll_desc = CollectionSerializer(data=collection_description, many=True)
    serialized_task_name = CollectionSerializer(data=task_name, many=True)

    return Response(
        data={serialized_coll_name.initial_data, serialized_coll_desc.initial_data, serialized_task_name.initial_data},
        status=status.HTTP_200_OK
    )

# TODO: start from here
