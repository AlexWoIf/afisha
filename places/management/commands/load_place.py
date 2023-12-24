import imghdr

import requests
from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from places.models import Place, Image


REPO_URL = 'https://github.com/devmanorg/where-to-go-places/' \
           'tree/master/places'
RAW_URL_PREFIX = 'https://raw.githubusercontent.com/' \
           'devmanorg/where-to-go-places/master/'


def load_place(place_url):
    try:
        response = requests.get(place_url)
        response.raise_for_status()
        payload = response.json()
        place, created = Place.objects.get_or_create(
            title=payload.get('title'),
            description_short=payload.get('description_short'),
            description_long=payload.get('description_long'),
            lng=payload.get('coordinates').get('lng'),
            lat=payload.get('coordinates').get('lat'),
        )
        if not created:
            return
    except IntegrityError:
        return
    except MultipleObjectsReturned:
        return
    except requests.exceptions.HTTPError:
        return
    for order, img_url in enumerate(payload['imgs'], start=1):
        try:
            response = requests.get(img_url)
            response.raise_for_status()
            img_bytes = response.content
            img_filename = f'image.{imghdr.what("",h=img_bytes)}'
            img = Image(place=place, order=order)
            img.image.save(img_filename,
                           ContentFile(img_bytes),
                           save=True, )
        except requests.exceptions.HTTPError:
            return


class Command(BaseCommand):
    help = 'Команда для загрузки данных из JSON-файлов'

    def add_arguments(self, parser):
        parser.add_argument('place_url', type=str, nargs='*')
        parser.add_argument('-r', '--repo', action='store_true', default=False)

    def handle(self, *args, **options):
        if not options['repo']:
            if not options['place_url']:
                raise CommandError('JSON-url not provided!!!')
            for url in options['place_url']:
                load_place(url)
            return
        response = requests.get(REPO_URL)
        response.raise_for_status()
        items = response.json()['payload']['tree']['items']
        from urllib.parse import quote
        for item in items:
            load_place(RAW_URL_PREFIX + quote(item['path']))

        return
