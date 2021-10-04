from django.db import models
import datetime

# Create your models here.
class Artist(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
    

class Piece(models.Model):
    YEAR_CHOICES = [(r,r) for r in range (0,datetime.date.today().year+1)]
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    year_completed = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    medium = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    genre = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        value = 'Title: ' + self.title
        return value


    