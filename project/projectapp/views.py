from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from email.mime import message
from os import name
from pdb import post_mortem
from urllib import response
from django.contrib import messages
from django.forms import Form
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from pkg_resources import require
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')

# def forumm(request):
#     return render(request,'forum_glowne.html')

# def baza(request):
#     return render(request, 'baza.html')

# def galeria(request):
#     return render(request, 'galeria.html')

# def gruba(request):
#     return render(request, 'gruba.html')

# def kolo(request):
#     return render(request, 'koło.html')

# def drobna(request):
#     return render(request,'drobna.html' )

# def rejestracja(request):
#     form = RejestracjaForm()
    
#     if request.method == 'POST':
#         form = RejestracjaForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower() 
#             user.save()
#             login (request, user)
#             return redirect('index')
            
#     return render(request, 'rejestracja.html', {'form': form})


# def logowanie(request):

#     page = 'login'
#     if request.user.is_authenticated:
#         return redirect('index')
    
#     if request.method == 'POST':
#         username = request.POST.get('username').lower()
#         password = request.POST.get('password')
        
#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'User does not exist')
            
#         user = authenticate(request, username=username, password=password)   
        
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             messages.error(request, 'Username or password does not exist')
                       
#     context = {'page': page}
#     return render(request, 'logowanie.html', context)

# def wylogowanie(request):
#     logout(request)
#     return redirect('index')

class Forum(ListView):
    model = Post
    template_name= 'forum.html'

# @login_required
# def profil (request, email):
#     customer = User.objects.get(email=email)
#     return render(request, 'profil.html', {"customer" : customer})

# class PostSzczegoly(DetailView):
#     model = Post 
#     template_name = 'post-szczegoly.html'
    
class DodajPostView(CreateView):
    model = Post
    template_name = 'dodaj-post.html'
    fields = '__all__'
    success_url = reverse_lazy('forum')
    
# class DodajKomentarzView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'dodaj-komentarz.html'
    
#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)
    
#     success_url = reverse_lazy('forum')
    
def rejestracja(request):
        form = RejestracjaForm()
    
        if request.method == 'POST':
            form = RejestracjaForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower() 
            user.save()
            login (request, user)
            return redirect('index')
            
        return render(request, 'rejestracja.html', {'form': form})


def logowanie(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, username=username, password=password)   
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password does not exist')
                       
    context = {'page': page}
    return render(request, 'logowanie.html', context)

def wylogowanie(request):
    logout(request)
    return redirect('index')