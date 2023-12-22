from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
    place_id = models.CharField(
        'PlaceID', max_length=200, blank=True, null=True
    )
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="images",
    )
    order = models.IntegerField('Позиция')
    image = models.ImageField(
        'Изображение', null=True, blank=True,
    )

    def __str__(self):
        return f'{self.order} {self.place.title}'
