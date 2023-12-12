from django.shortcuts import render, redirect
from django.views import View
from .forms import BookForm
from .models import BookModal


# Create your views here.


class BooksView(View):
  def get(self, request):
    form = BookForm()
    books = BookModal.objects.all()
    return render(request, "index.html", {"form": form, "books": books})

  def post(self, request):
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect("book")


class BookDetailsView(View):
  def get(self, request, id):
    book = BookModal.objects.get(id=id)
    return render(request, "bookdetails.html", {"book": book})


class BookDeleteView(View):
  def get(self, request, id):
    book = BookModal.objects.get(id=id)
    book.delete()
    return redirect('book')
