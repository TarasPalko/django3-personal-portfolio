from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    text = models.TextField(max_length=100000)