from django.urls import path
from .views import index, books, delete, update

urlpatterns = [
    path("", index, name="index"),
    path("books", books, name="booksPage"),
    path("delete/<int:pk>>", delete, name="deletePage"),
    path("update/<int:pk>", update, name="updatePage"),
]
