from django.db import models
from cities.models import City

# Create your models here.


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название маршрута')
    route_travel_time = models.PositiveSmallIntegerField(verbose_name='Общее время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                    related_name='route_from_city_set',
                                    verbose_name='Откуда'
                                    )
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                    related_name='route_to_city_set',
                                    verbose_name='Куда'
                                    )

    trains = models.ManyToManyField('trains.Train', verbose_name='Список поездов')

    def __str__(self) -> str:
        return f'Маршрут {self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'маршрут'
        verbose_name_plural = 'маршруты'
        ordering = ['route_travel_time']