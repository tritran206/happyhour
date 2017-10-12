from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length = 255, default='SOME STRING')
    address = models.CharField(max_length = 255)
    lat = models.FloatField()
    lng = models.FloatField()
    happy_hour_start = models.TimeField()
    happy_hour_end = models.TimeField()
    rating = models.DecimalField(max_digits = 5, decimal_places = 1)

class Drink(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, related_name='restaurant')
    name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

# class User(models.Model):
#     user_name = models.CharField(max_length = 255)
#     email = models.CharField(max_length = 255)
#     password = models.CharField(max_length = 255)
#
# class Favorites(models.Model):
#     user = models.ForeignKey(User, related_name='user')
#     fav_restaurants = models.ForeignKey(Restaurant, related_name='restaurant')
