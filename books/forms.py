from django import forms

from books.models import Books


class BooksModelForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
