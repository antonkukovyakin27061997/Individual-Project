from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    release = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    duration = models.IntegerField() # продолжительность фильма 
    poster = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.title


class Role(models.Model):
    role_types =models.CharField(max_length=50,choices=[
        ('no name','неизвестно'),
        ('actor', 'Актер'),
        ('director', 'Режиссер'),
        ('writer', 'Сценарист'),
    ], default='неизвестно')
    
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.name} - {self.role_type} в {self.title.title}"


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class TitleStudio(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)


class Title(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    duration = models.IntegerField() # продолжительность фильма 
    poster = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.title