from django.shortcuts import render, redirect
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

def index(request):

    return render(request, 'happy_hour_app/search_form.html')

def results(request):
    # key = "AIzaSyBvbKFWJu80KQ1yxgxfP4k9hMVEaVBYamc"
    # location = request.POST
    # gmaps = GoogleMaps(key)
    #
    # directions = gmaps.directions("18817 1st Ave W. Bothell, WA 98012", "20814 31st Ave W. Lynnwood, WA 98036")
    # print(directions['Distance'])

    geolocator = Nominatim()
    location_a = geolocator.geocode("18817 1st Ave W. Bothell, WA 98012")
    location_b = geolocator.geocode("20814 31st Ave W. Lynnwood, WA 98036")
    lat_long_a = (location_a.latitude, location_a.longitude)
    lat_long_b = (location_b.latitude, location_b.longitude)

    print("location A: " + location_a.address)

    print("location B: " + location_b.address)
    print("distance from A and B is: " + str(vincenty(lat_long_a, lat_long_b).miles))

    return redirect('/')

# Create your views here.
