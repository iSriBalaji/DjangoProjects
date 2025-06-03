from django.db import models

class Moviedata(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Rating out of 10")
    genre = models.CharField(max_length=255, default='action')
    poster = models.ImageField(upload_to='movie_posters/', default='movie_posters/poster.jpg')

    def __str__(self):
        return self.name
