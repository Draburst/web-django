import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BaseMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    publiched_date = models.DateTimeField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.published_date = timezone.now()
        super().save()

    class Meta:
         abstract = True

# Create your models here.

class Question(BaseMessage):

    title = models.CharField(max_length=128)


    def __str__(self):
            return self.title
    

class Answer(BaseMessage):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)


    def __str__(self):
        return self.text
    