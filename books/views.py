from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from books.forms import BooksModelForm
from books.models import Books


# Create your views here.


def books(request):
    _books = Books.objects.all()
    return render(request, "books/books.html", context={"books": _books})


def book(request, id):
    _books = get_object_or_404(Books, pk=id)
    return render(request, "books/book_detail.html", context={"book": _books})


@login_required
def delete_book(request, id):
    _books = get_object_or_404(Books, pk=id)
    _books.delete()
    url = reverse("books")
    return redirect(url)


@login_required
def create_book(request):
    form = BooksModelForm()
    if request.method == "POST":
        books = BooksModelForm(request.POST, request.FILES)
        if books.is_valid():
            new_book = books.save()
            return redirect(reverse_lazy("books.book", args=[new_book.id]))
        else:
            # Pass form with errors to template
            return render(request, "books/create.html", {"form": books})

    return render(request, "books/create.html", {"form": form})


@login_required
def update_book(request, id):
    _book = get_object_or_404(Books, pk=id)

    if request.method == "POST":
        form = BooksModelForm(request.POST, request.FILES, instance=_book)
        if form.is_valid():
            form.save()
            return redirect("books.book", id=id)
    else:
        form = BooksModelForm(instance=_book)

    return render(request, "books/update.html", {"form": form, "book": _book})


def contactus_us(request):
    return render(request, "books/contactus.html")


def about_us(request):
    return render(request, "books/aboutus.html")
