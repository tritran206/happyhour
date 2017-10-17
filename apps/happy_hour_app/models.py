from django.db import models
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

class Restaurant_Manager(models.Manager):

    def find_restaurants_address(self, current_location, distance):

        geolocator = Nominatim()
        current_location = geolocator.geocode(current_location)
        lat_lng_current_location = (current_location.latitude, current_location.longitude)
        all_restaurants = Restaurant.objects.all()
        local_restaurant_list = []

        for restaurant in all_restaurants:
            db_restaurant_lat_lng = (restaurant.lat, restaurant.lng)

            if vincenty(db_restaurant_lat_lng, lat_lng_current_location).miles < float(distance):
                local_restaurant_list.append(restaurant)
        return local_restaurant_list

    def restaurant_json(self, current_location, local_restaurant_list):

        all_drinks = Drink.objects.all()
        local_restaurants_ids = []
        geolocator = Nominatim()
        current_location = geolocator.geocode(current_location)
        lat_lng_current_location = (current_location.latitude, current_location.longitude)
        JSON_Data = []

        for restaurant in local_restaurant_list:
            local_restaurants_ids.append(restaurant.id)

        for drink in all_drinks:

            if drink.restaurant_id_id in local_restaurants_ids:

                restaurant = Restaurant.objects.get(id=drink.restaurant_id_id)
                restaurant_location = geolocator.geocode(restaurant.address)
                lat_lng_restaurant_location = (restaurant_location.latitude, restaurant_location.longitude)
                distance = vincenty(lat_lng_current_location, lat_lng_restaurant_location).miles
                print(distance)

                new_data = {
                                "restaurant_id" : drink.restaurant_id_id,
                                "restaurant_name" : drink.restaurant_name,
	                            "drink_name" : drink.name,
	                            "price" : drink.price,
	                            "distance" : distance
                }
                JSON_Data.append(new_data)

        return JSON_Data



class Restaurant(models.Model):
    name = models.CharField(max_length = 255, default='SOME STRING')
    address = models.CharField(max_length = 255)
    lat = models.FloatField()
    lng = models.FloatField()
    happy_hour_start = models.TimeField()
    happy_hour_end = models.TimeField()
    rating = models.DecimalField(max_digits = 5, decimal_places = 1)
    objects = Restaurant_Manager()

class Drink(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, related_name='restaurant')
    name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    restaurant_name = models.CharField(max_length = 255, default='SOME STRING')



    # location_b = geolocator.geocode("20814 31st Ave W. Lynnwood, WA 98036")
    # lat_long_a = (location_a.latitude, location_a.longitude)
    # lat_long_b = (location_b.latitude, location_b.longitude)
    #
    # print("location A: " + location_a.address)
    #
    # print("location B: " + location_b.address)
    # print("distance from A and B is: " + str(vincenty(lat_long_a, lat_long_b).miles))

# class User(models.Model):
#     user_name = models.CharField(max_length = 255)
#     email = models.CharField(max_length = 255)
#     password = models.CharField(max_length = 255)
#
# class Favorites(models.Model):
#     user = models.ForeignKey(User, related_name='user')
#     fav_restaurants = models.ForeignKey(Restaurant, related_name='restaurant')
