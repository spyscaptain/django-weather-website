from django.shortcuts import render
import urllib.request
import json

def index(request):

    if request.method == 'POST':
        city=request.POST['city']

        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city +'&units=metirc&appid=bcb96485f8dd4599f3b8642eb6b9ce79').read()

        list_of_data=json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °F',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        # print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)