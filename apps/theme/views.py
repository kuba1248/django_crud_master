from django.shortcuts import render

# from apps.books_cbv.models import Book

#
# def home(request, template_name='books_fbv/book_list.html'):
#     book = Book.objects.all()
#     data = {}
#     data['object_list'] = book
#     return render(request, template_name, data)


def home(request):
    return render(request, "home.html",)