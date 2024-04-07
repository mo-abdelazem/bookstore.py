from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import reverse
from category.models import Category

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    page_numbers = models.IntegerField(blank=True)
    image = models.ImageField(upload_to="books/images", blank=True)
    author = models.CharField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="all_books",
    )

    def __str__(self):
        return f"{self.name}"

    @property
    def show_url(self):
        url = reverse("books.book", args=[self.id])
        return url

    @property
    def delete_url(self):
        url = reverse("books.delete", args=[self.id])
        return url

    @property
    def image_url(self):
        return f"/media/{self.image}"
