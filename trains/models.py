from django.core.exceptions import ValidationError
from django.db import models
from cities.models import City


# Create your models here.


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Номер поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='from_city_set',
                                  verbose_name='Откуда'
                                  )
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                related_name='to_city_set',
                                verbose_name='Куда'
                                )

    def __str__(self) -> str:
        return f'Поезд №{self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'поезд'
        verbose_name_plural = 'поезда'
        ordering = ['travel_time']

    def clean(self) -> None:
        if self.from_city == self.to_city:
            raise ValidationError('Города отправления и прибытия совпадают')
        qs = Train.objects.filter(
            from_city=self.from_city, to_city=self.to_city,
            travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Измените время в пути')

    def save(self, *args, **kwargs) -> None:
        self.clean()
        super().save(*args, **kwargs)
