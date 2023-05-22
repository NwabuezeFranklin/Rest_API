from django.db import models

# Create your models here.

class Article(models.Model):
    topic = models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.topic
    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=255)
    occupation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
