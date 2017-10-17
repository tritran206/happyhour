from django.shortcuts import render, redirect
from .models import Restaurant, Drink
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from django.http import JsonResponse

def index(request):

    return render(request, 'happy_hour_app/index.html')

def results(request):

    address_location = request.GET['address_location']
    distance = request.GET['distance']
    local_restaurant_list = Restaurant.objects.find_restaurants_address(address_location, distance)

    JSON_Data = Restaurant.objects.restaurant_json(address_location, local_restaurant_list)

    print(JSON_Data)

    return JsonResponse(JSON_Data, safe=False)

def restaurant(request, restaurant_id):

    restaurant = Restaurant.objects.get(id = restaurant_id)
    drinks = Drink.objects.filter(restaurant_id = restaurant_id)

    JSON_Data = {
                	"id" : restaurant.id,
                	"name" : restaurant.name,
                	"rating" : restaurant.rating,
                	"address" : restaurant.address,
                	"happy_hour_start" : restaurant.happy_hour_start,
                	"happy_hour_end" : restaurant.happy_hour_end,
                	"drinks" : []
                }

    for drink in drinks:
        JSON_Data["drinks"].append({"drink_name" : drink.name, "price" : drink.price})

    print(JSON_Data)

    return JsonResponse(JSON_Data, safe=False)



    #
    # return render(request, '/results.html', JSON_Data)

# Create your views here.
