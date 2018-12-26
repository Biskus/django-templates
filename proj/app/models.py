from django.db import models
from django.contrib.auth  import get_user_model
from django.urls import reverse
import datetime

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
        )
    title = models.CharField(max_length=50)
    content = models.TextField()
    

class Lecture(models.Model):
    class Meta():
        ordering = ['-pub_date']
    url = models.CharField(max_length=200, verbose_name='Url', help_text='Til Google-docs presentasjon')
    title = models.CharField(max_length=200, verbose_name='Tittel')
    undertitle = models.CharField(max_length=200, null=True, blank=True, verbose_name='Undertittel')
    target_audience = models.CharField(max_length=200, null=True, blank=True, verbose_name='Målgruppe')
    pub_date = models.DateField(default=datetime.date.today)
    tags = models.ManyToManyField('app.Tag', related_name='lectures', blank=True)
    tasks = models.IntegerField(null=True, blank=True, verbose_name='Oppgaver')
    
    def get_absolute_url(self):
        return reverse('lecture_update', args=[str(self.id)])
    
    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.__repr__()


class Tag(models.Model):
    class Meta():
        ordering = ['-label']
    name = models.CharField(max_length=50, verbose_name='Navn')
    #https://getbootstrap.com/docs/4.0/components/badge/
    #Primary Secondary Success Danger Warning Info Light Dark
    label = models.CharField(max_length=20, verbose_name='Bootstrap-klasse')
    
    def __repr__(self):
        return (str(self.pk) + " " + self.name)
    
    def __str__(self):
        return self.__repr__()
    
