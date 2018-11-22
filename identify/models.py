from django.db import models
from django.urls import reverse



class Flower(models.Model):
    flower_name = models.CharField(max_length=250)
    flower_image = models.FileField()

    def get_absolute_url(self):
        return reverse('identify:index')

    def __str__(self):
        return self.flower_name

