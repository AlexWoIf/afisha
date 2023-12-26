from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from places.models import Place


def index(request):
    def create_feature(place):
        return {
            'type': 'Feature',
            'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat, ],
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place', args=[place.id, ]),
            },
        }

    context = {
        'geo_json': {
            'type': 'FeatureCollection',
            'features': [
                create_feature(place) for place in Place.objects.all()
            ]
        }
    }
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
    return JsonResponse(
        place_json_dict,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
