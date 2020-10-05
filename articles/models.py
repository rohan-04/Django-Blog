from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...' 