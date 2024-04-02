from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

_books = [
    {
        "id": 1,
        "name": "Iliana Villarreal",
        "image": "1.jpg",
        "author": "Dolore in eum facere",
        "pages": 21,
        "price": 833,
    },
    {
        "id": 2,
        "name": "Galena Munoz",
        "image": "1.jpg",
        "author": "Facere eveniet et a",
        "pages": 43,
        "price": 973,
    },
    {
        "id": 3,
        "name": "Farrah Mccormick",
        "image": "1.jpg",
        "author": "Non in in quia volup",
        "pages": 56,
        "price": 539,
    },
    {
        "id": 4,
        "name": "Howard Clay",
        "image": "1.jpg",
        "author": "Omnis ut facere sed ",
        "pages": 2,
        "price": 669,
    },
    {
        "id": 41,
        "name": "Irene Richardson",
        "image": "1.jpg",
        "author": "In nostrum ad qui co",
        "pages": 67,
        "price": 282,
    },
    {
        "id": 411,
        "name": "Yardley Thompson",
        "image": "1.jpg",
        "author": "Itaque aut ab id per",
        "pages": 75,
        "price": 634,
    },
    {
        "id": 4111,
        "name": "Cadman Rasmussen",
        "image": "1.jpg",
        "author": "Occaecat culpa nemo ",
        "pages": 87,
        "price": 894,
    },
]


def books(request):
    return render(request, "books/books.html", context={"books": _books})


def book(request, id):
    filtered_books = filter(lambda book: book["id"] == id, _books)
    filtered_books = list(filtered_books)
    if filtered_books:
        _book = filtered_books[0]
        return render(request, "books/book_detail.html", context={"book": _book})

    return HttpResponse("book not found")


def contactus_us(request):
    return render(request, "books/contactus.html")


def about_us(request):
    return render(request, "books/aboutus.html")
