from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from places.models import Place


class UTF8JsonResponse(JsonResponse):
    def __init__(self, *args, json_dumps_params=None, **kwargs):
        json_dumps_params = {
            "ensure_ascii": False,
            **(json_dumps_params or {})
        }
        super().__init__(*args, json_dumps_params=json_dumps_params, **kwargs)


def index(request):
    def create_feature(lng, lat, title, place_id, details_url):
        return {
            'type': 'Feature',
            'geometry': {
                    'type': 'Point',
                    'coordinates': [lng, lat, ],
            },
            'properties': {
                'title': title,
                'placeId': place_id,
                'detailsUrl': details_url,
            },
        }

    context = {'geo_json': {'type': 'FeatureCollection', 'features': []}}
    for place in Place.objects.all():
        lng = place.lng
        lat = place.lat
        title = place.title
        place_id = place.id
        details_url = reverse('place', args=[place.id, ])
        context['geo_json']['features'].append(
            create_feature(lng, lat, title, place_id, details_url)
        )
    return render(request, 'index.html', context)


def show_place(request, id):
    place = get_object_or_404(Place.objects.select_related(), id=id)
    place_json_dict = {
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        },
    }
    return UTF8JsonResponse(place_json_dict, json_dumps_params={'indent': 2})
