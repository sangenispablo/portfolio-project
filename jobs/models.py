from django.db import models

class Job(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    summary = models.CharField(max_length=200)