from django.urls import path
from books.views import books, book

urlpatterns = [
    path("", books, name="books"),
    path("<int:id>", book, name="books.book"),
]
