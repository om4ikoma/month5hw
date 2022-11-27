from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    duration = models.IntegerField(null=True)
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.CharField(max_length=100, null=True)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)
