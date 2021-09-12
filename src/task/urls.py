from django.urls import path
from .api_v1 import (
    CollectionListView,
    CollectionCreateView,
    CollectionRetrieveUpdateDeleteView,
    CollaboratorCreateView,
    CollaboratorUpdateView,
    CollaboratorDeleteView,
    TaskListView,
    TaskCreateView,
    CollectionListViewShort,
    TaskUpdateView,
    TaskDeleteView,
    TagListCreateView,
    TagUpdateRetrieveDeleteView,

    searchApiView
)

urlpatterns = [
    path('collections/', CollectionListViewShort.as_view()),
    path('collections/create/', CollectionCreateView.as_view()),
    path('collections/<int:pk>/', CollectionRetrieveUpdateDeleteView.as_view()),

    path('collections/<int:pk>/collaborators/<int:id>/', CollaboratorUpdateView.as_view()),
    path('collections/<int:pk>/collaborators/create/', CollaboratorCreateView.as_view()),
    path('collections/<int:pk>/collaborators/delete/<int:id>/', CollaboratorDeleteView.as_view()),

    path('collections/<int:pk>/tasks/', TaskListView.as_view()),
    path('collections/<int:pk>/tasks/create/', TaskCreateView.as_view()),
    path('collections/<int:pk>/tasks/update/<int:id>/', TaskUpdateView.as_view()),
    path('collections/<int:pk>/tasks/delete/<int:id>/', TaskDeleteView.as_view()),

    path('tags/', TagListCreateView.as_view()),
    path('tags/<int:pk>/', TagUpdateRetrieveDeleteView.as_view()),


    # path('search/', searchApiView),
    # TODO: uncomment

]
