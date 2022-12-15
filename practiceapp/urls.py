from django.urls import path, include
from .views import HelloAPI, BooksAPI, BookAPI

urlpatterns = [
    path('', HelloAPI.as_view()),
    path('books/', BooksAPI.as_view()),
    path('books/<int:bid>/', BookAPI.as_view()),
]
