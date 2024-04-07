from django.shortcuts import render, redirect, reverse
from category.forms import CategoryModelForm
from category.models import Category


# Create your views here.
def create_category(request):

    form = CategoryModelForm()
    if request.method == "POST":
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            category = form.save()
            url = reverse("category")
            return redirect(url)
    return render(request, "category/create.html", {"form": form})


def category_index(request):
    categories = Category.get_all_categories()
    return render(request, "category/cateogries.html", {"categories": categories})


def update_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryModelForm(instance=category)
    if request.method == "POST":
        form = CategoryModelForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category")
    return render(request, "category/update.html", {"form": form})


def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == "POST":
        category.delete()
        return redirect("category")
    return render(request, "category/delete.html", {"category": category})


def show_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, "category/show.html", {"category": category})
