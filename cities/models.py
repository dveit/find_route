from django.db import models
from django.urls import reverse

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse("cities:detail", kwargs={"pk": self.pk})
    