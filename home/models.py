from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class input_post(models.Model):
    heading = models.CharField(max_length=150, null=False)
    desc = models.CharField(max_length=2000, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    time = models.DateTimeField(default=datetime.now())
    like = models.PositiveIntegerField(default=0)
    user_like = models.JSONField(default=list)
    user_comment = models.JSONField(default=list)

    def __str__(self):
        return self.heading