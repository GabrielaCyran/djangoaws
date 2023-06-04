from dataclasses import fields
import email
from pdb import post_mortem
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NowyKomentarzForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        # model = Comment
        fields = ('nazwa', 'tresc')
        
class RejestracjaForm(UserCreationForm):
    email = models.EmailField()
    imie = forms.CharField(max_length=100)
    nazwisko = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'imie', 'nazwisko', 'password1', 'password2')# 