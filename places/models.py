from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200, )
    short_description = models.TextField('Краткое описание', blank=True, )
    long_description = HTMLField('Полное описание', blank=True, )
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        unique_together = ['lng', 'lat', ]

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="images",
        verbose_name='Локация',
    )
    order = models.IntegerField('Позиция', default=0, db_index=True, )
    image = models.ImageField('Изображение', )

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return f'{self.order} {self.place.title}'
