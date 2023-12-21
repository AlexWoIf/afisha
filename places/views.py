from django.shortcuts import render

# Create your views here.


def index(request):
    def createFeature(lng, lat, title, placeId, detailsUrl):
        return {
            'type': 'Feature',
            'geometry': {
                    'type': 'Point',
                    'coordinates': [lng, lat, ],
            },
            'properties': {
                'title': title,
                'placeId': placeId,
                'detailsUrl': detailsUrl,
            },
        }

    context = {
        'geo_json': {
            'type': 'FeatureCollection',
            'features': [
                createFeature(
                    37.62, 55.793676, 'Легенды Москвы',
                    'moscow_legends', './static/places/moscow_legends.json',
                ),
                createFeature(
                    37.64, 55.753676, 'Крыши24.рф',
                    'roofs24', './static/places/roofs24.json',
                ),
            ]
        }
    }

    return render(request, 'index.html', context)
