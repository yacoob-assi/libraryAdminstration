from django import forms
from .models import Book, Category


class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "auther",
            "price",
            "rent_price",
            "rent_period",
            "pages",
            "book_photo",
            "author_photo",
            "status",
            "category",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "auther": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "rent_price": forms.NumberInput(attrs={"class": "form-control"}),
            "rent_period": forms.NumberInput(attrs={"class": "form-control"}),
            "pages": forms.NumberInput(attrs={"class": "form-control"}),
            "book_photo": forms.FileInput(attrs={"class": "form-control"}),
            "author_photo": forms.FileInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
