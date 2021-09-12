from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import Collection, Collaborator
from .serializers import CollectionSerializer, CollaboratorSerializer


class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.filter(user=2)
    serializer_class = CollectionSerializer
    permission_classes = (AllowAny,)


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
            return Response({'error': 'user is required'}, status=status.HTTP_400_BAD_REQUEST)
        collection = Collection.objects.get(pk=kwargs['pk'])
        collaborator = Collaborator(user_id=request.data['user'], collection=collection)
        collaborator.save()
        serializer = CollaboratorSerializer(collaborator)
        return Response(serializer.data)


class CollaboratorUpdateView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        if 'user' not in request.data:
            return Response({'error': 'user is required'}, status=status.HTTP_400_BAD_REQUEST)
        collaborator = Collaborator.objects.get(pk=kwargs['id'])
        print(collaborator.user)
        serializer = CollaboratorSerializer(instance=collaborator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollaboratorDeleteView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        collaborator = Collaborator.objects.get(pk=kwargs['id'])
        collaborator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
