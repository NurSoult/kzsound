from django.db import models

# Create your models here.


class Track(models.Model):
    title = models.CharField('Track name', max_length=40)
    artist = models.CharField('Artist nickname', max_length=50)
    description = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Тректер"
        ordering = ['title']


class Contact(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    telnumber = models.IntegerField('Telephone number')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контактілер"
        ordering = ['name', 'surname']


class Rapper(models.Model):
    nick = models.CharField('Nickname', max_length=30)
    label = models.CharField('Label', max_length=30)
    genre = models.CharField('Genre', max_length=15)
    tracks = models.TextField('Tracks', max_length=100)

    def __str__(self):
        return self.nick

    class Meta:
        verbose_name = "Орындаушы"
        verbose_name_plural = "Орындаушылар"
        ordering = ['nick']