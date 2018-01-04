from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from django.forms.models import model_to_dict
from .models import Book
from .models import Post




def book_info(request):
	if request.method == 'POST':

		print request.POST
		book=Book()
		book.Book_name= request.POST.get('bname')
		book.author=  request.POST.get('author')
		book.isbn= request.POST.get('num')
		book.desc= request.POST.get('about')

		book.save()

	
	books = Book.objects.values()
	print books
	return render(request, 'book_info.html', {'books': books})	

def author_info(request):
	if request.method == 'POST':
		print request.POST
		post=Post()
		post.author= request.POST.get('author')
		post.age= request.POST.get('age')
		post.gender= request.POST.get('gender')
		post.Born_in= request.POST.get('Born_in')
		post.abt_author= request.POST.get('abt_author')
		post.save()
	authors = Post.objects.values()
	print authors
	return render(request,'author_info.html', {'authors': authors})


def bookdetail(request, bookname):

	book = get_object_or_404(Book, Book_name = bookname)
	print model_to_dict(book)
	return render(request,'bookdetail.html', {'book': model_to_dict(book)})


def authordetail(request, authorname):
	print("hello",authorname)
	authorObject = get_object_or_404(Post, author = authorname)
	print("hello",authorname)
	book1 = Book.objects.filter(author = authorObject.author).values
	return render(request,'authordetail.html', {'books':book1,'author':authorObject})


# Create your views here.
