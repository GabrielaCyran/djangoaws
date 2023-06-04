from django.contrib import admin
from django.urls import path, include

from django.urls import URLPattern, path
from .import views 

urlpatterns= [

path('', views.index, name="index"),

path('index/',views.index,name="index"),
path('forum/',views.Forum.as_view(), name="forum"),
path('dodaj-post/', views.DodajPostView.as_view(), name="dodaj-post"),
path ('logowanie/',views.logowanie,name="logowanie"),
path('rejestracja',views.rejestracja,name="rejestracja"),
path('wylogowanie/',views.wylogowanie, name="wylogowanie"),
]
