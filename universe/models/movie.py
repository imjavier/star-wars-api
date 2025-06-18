from django.db import models

class Movie(models.Model):
    opening_crawl = models.TextField()
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=30)
    producers = models.TextField()
    created_date = models.DateField()
    planets = models.ManyToManyField('universe.Planet', related_name='movies')
    characters = models.ManyToManyField('universe.Character', related_name='movies')
