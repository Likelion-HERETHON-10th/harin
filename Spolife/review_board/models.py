from django.db import models
from django.contrib.auth.models import User


class Review_Post(models.Models):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    score = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to='review_photo')


    def __str__(self):
        return self.title


class Review_Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Review_Post, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.comment