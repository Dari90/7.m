from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from p_library.models import Book, Author, Friend, Publishing_house, UserProfile
from p_library.forms import FriendForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory  
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils import timezone
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def index(request):
    template = loader.get_template('base.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    
    return HttpResponse(template.render(biblio_data, request))

def library(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def redaction_list(request):
    template = loader.get_template('redaction_list.html')
    redactions = Publishing_house.objects.all()
    publishers_data = {"data": {publishing_hous.name: 
						list(Book.objects.filter(publishing_house=publishing_hous.id).values_list("title", flat=True))
						 for publishing_hous in redactions}}
    return HttpResponse(template.render(publishers_data, request))

def friend_list(request):
	template = loader.get_template('friend_list.html')
	friends = Friend.objects.all()
	data = {"friends": friends,}
	return HttpResponse(template.render(data, request))	
    
class FriendList(ListView):
	model = Friend
	template_name = 'friend_form.html'

def user_profil(request):
    template = loader.get_template('user_profil.html')
    if request.user.is_authenticated:
        profile_data = {
        "title": "Профиль",
        "username": request.user.username,
        }
        return HttpResponse(template.render(profile_data, request))
        
def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')
        


