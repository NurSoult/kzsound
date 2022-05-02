from django.db import models
from django.template.defaultfilters import date


# Create your models here.


class Article(models.Model):
    title = models.CharField('Title', max_length=50)
    full_text = models.TextField('Makala')
    genre = models.CharField('Genre', max_length=50, default=None)
    language = models.CharField('Language', max_length=2, default=None)
    date = models.DateField('Publication date')
    author = models.CharField('Author', max_length=50, default=None)
    location = models.CharField('Location', max_length=50, default=None)

    # @property
    # def lifespan(self):
    #     return '%s - present' % self.date.strftime('%d/%m/%Y')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Мақала"
        verbose_name_plural = "Мақалалар"