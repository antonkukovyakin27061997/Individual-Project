from django.db import models
from django.contrib.auth.models import User
from movies.models import Title


# профиль пользователя

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField() # фото профиля
    bio = models.TextField(blank=True) # биография
    favorite_genres = models.CharField(max_length=255, blank=True) # любимые жанры

    def __str__(self):
        return self.user


# статистика просмотров

class UserMovieStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Title, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False) # просмотрено
    watch_later = models.BooleanField(default=False) # будет просмотрено позже
    watch_count = models.IntegerField(default=0) # количество просмотров
 