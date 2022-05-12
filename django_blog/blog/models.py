from distutils.command.upload import upload
from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    target = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]