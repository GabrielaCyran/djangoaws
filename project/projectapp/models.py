from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    tytul = models.CharField(max_length=200 )
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    tresc = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tytul
    
    def get_absolute_url(self):
        return reverse ('forum')
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=250)
    tresc = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.tytul, self.nazwa)
    