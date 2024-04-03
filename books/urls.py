from django.urls import path
from books.views import books, book, delete_book, create_book, update_book

urlpatterns = [
    path("", books, name="books"),
    path("<int:id>", book, name="books.book"),
    path("<int:id>/delete", delete_book, name="books.delete"),
    path("create", create_book, name="books.create"),
    path("<int:id>/update", update_book, name="books.update"),
]
