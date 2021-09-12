from django.urls import path
from .api_v1 import (
    CollectionListView,
    CollectionCreateView,
    CollectionRetrieveUpdateDeleteView,
    CollaboratorCreateView,
    CollaboratorUpdateView,
    CollaboratorDeleteView
)


urlpatterns = [
    path('collections/', CollectionListView.as_view()),
    path('collections/create/', CollectionCreateView.as_view()),
    path('collections/<int:pk>/', CollectionRetrieveUpdateDeleteView.as_view()),

    path('collections/<int:pk>/collaborators/<int:id>/', CollaboratorUpdateView.as_view()),
    path('collections/<int:pk>/collaborators/create/', CollaboratorCreateView.as_view()),
    path('collections/<int:pk>/collaborators/delete/<int:id>/', CollaboratorDeleteView.as_view()),

]



