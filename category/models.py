from django.db import models
from django.shortcuts import get_object_or_404, reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    @classmethod
    def get_category_by_id(cls, id):
        return get_object_or_404(cls, pk=id)
