from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='anonymous')
    current_city = models.CharField(max_length=100, default='N/A')
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, user):
        return cls(user=user)

class City(models.Model):
    image = models.URLField(max_length=200)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1500)
    
    def __str__(self):
        return str(self.author) + self.title

    class Meta:
        ordering = ['created_at']