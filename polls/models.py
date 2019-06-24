from django.db import models

# Create your models here.
class Poll(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    sub=models.TextField()

    def __str__(self):
        return self.fname
