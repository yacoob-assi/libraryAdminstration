from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import bookForm, categoryForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = bookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")

        formCategory = categoryForm(request.POST)
        if formCategory.is_valid():
            formCategory.save()
            return redirect("index")
    else:
        form = bookForm()

    return render(
        request,
        "index.html",
        {
            "books": Book.objects.all(),
            "categories": Category.objects.all(),
            "form": form,
            "booksCount": Book.objects.all().count(),
            "soldBooks": Book.objects.filter(status="sold").count(),
            "rentalBooks": Book.objects.filter(status="rental").count(),
            "avaliableBooks": Book.objects.filter(status="avaliable").count(),
            "categoryForm": categoryForm,
        },
    )


def books(request):
    books = Book.objects.all()
    if "search_name" in request.GET:
        text = request.GET["search_name"]
        if text:
            books = books.filter(title__icontains=text)

    return render(
        request,
        "books.html",
        {
            "books": books,
            "booksCount": Book.objects.all().count(),
            "soldBooks": Book.objects.filter(status="sold").count(),
            "rentalBooks": Book.objects.filter(status="rental").count(),
            "avaliableBooks": Book.objects.filter(status="avaliable").count(),
            "categories": Category.objects.all(),
            "categoryForm": categoryForm,
        },
    )


def update(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == "POST":
        form = bookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = bookForm(instance=book)

    return render(
        request,
        "update.html",
        {
            "form": form,
            "booksCount": Book.objects.all().count(),
            "soldBooks": Book.objects.filter(status="sold").count(),
            "rentalBooks": Book.objects.filter(status="rental").count(),
            "avaliableBooks": Book.objects.filter(status="avaliable").count(),
            "categoryForm": categoryForm,
        },
    )


def delete(request, pk):
    item = Book.objects.get(pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("index")

    return render(
        request,
        "delete.html",
        {
            "booksCount": Book.objects.all().count(),
            "soldBooks": Book.objects.filter(status="sold").count(),
            "rentalBooks": Book.objects.filter(status="rental").count(),
            "avaliableBooks": Book.objects.filter(status="avaliable").count(),
            "categoryForm": categoryForm,
        },
    )
