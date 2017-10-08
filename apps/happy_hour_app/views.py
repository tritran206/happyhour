from django.shortcuts import render, redirect
import googlemaps

def index(request):

    return render(request, 'happy_hour_app/search_form.html')

def results(request):
    key = "AIzaSyBvbKFWJu80KQ1yxgxfP4k9hMVEaVBYamc"
    location = request.POST
    gmaps = GoogleMaps(key)

    directions = gmaps.directions("18817 1st Ave W. Bothell, WA 98012", "20814 31st Ave W. Lynnwood, WA 98036")
    print(directions['Distance'])
    return redirect('/')

# Create your views here.
