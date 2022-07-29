from django.db import models
from django.contrib.auth.models import User

class Recruit_Post(models.Models):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    gender_choices = [
        ('F', '여자'),
        ('M', '남자'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    activity_time = models.DateTimeField()
    is_recruit = models.BooleanField()


    def __str__(self):
        return self.title
        

class Recruit_Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Recruit_Post, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.comment