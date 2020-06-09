from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    path = models.CharField(max_length=100)
    time = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    message = models.TextField(max_length=500)
    time = models.DateTimeField(default=timezone.now)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    replay = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True, related_name = 'replies')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.message}"
