from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Город')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'
        ordering = ['name']