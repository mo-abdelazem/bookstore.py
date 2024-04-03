from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse

from books.models import Books


# Create your views here.


def books(request):
    _books = Books.objects.all()
    return render(request, "books/books.html", context={"books": _books})


def book(request, id):
    _books = get_object_or_404(Books, pk=id)
    return render(request, "books/book_detail.html", context={"book": _books})


def delete_book(request, id):
    _books = get_object_or_404(Books, pk=id)
    _books.delete()
    url = reverse("books")
    return redirect(url)


def create_book(request):
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        print(request.POST)
        books = Books(
            name=request.POST["name"],
            author=request.POST["author"],
            price=request.POST["price"],
            page_numbers=request.POST["pages"],
            image=image,
        )
        books.save()
        return redirect(books.show_url)

    return render(request, "books/create.html")


def update_book(request, id):
    _book = get_object_or_404(Books, pk=id)

    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = _book.image

        _book.name = request.POST["name"]
        _book.author = request.POST["author"]
        _book.price = request.POST["price"]
        _book.page_numbers = request.POST["pages"]
        _book.image = image
        _book.save()

        return redirect("books.book", id=id)

    return render(request, "books/update.html", {"book": _book})


def contactus_us(request):
    return render(request, "books/contactus.html")


def about_us(request):
    return render(request, "books/aboutus.html")
