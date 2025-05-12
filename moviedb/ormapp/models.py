from django.db import models
from django.contrib import admin

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)  # Custom primary key
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    date_of_release = models.DateField()
    rating = models.IntegerField()
    
class MovieAdmin(admin.ModelAdmin):
    list_display=('movie_id','title','genre','date_of_release','rating')

