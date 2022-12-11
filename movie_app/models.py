from django.db import models
from django.contrib.auth.models import User


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


STARS = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****')
)


class Movie(object):
    pass


class Review(models.Model):
    text = models.CharField(max_length=100, null=True)
    movie_list = models.ForeignKey(Movie, on_delete=models.CASCADE)
    starts = models.IntegerField(null=True, choices=STARS)

    def __str__(self):
        return self.text


class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    duration = models.IntegerField(null=True)
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE)
    reviews_list = models.ManyToManyField(Review, related_name='reviews')

    def __str__(self):
        return self.title
