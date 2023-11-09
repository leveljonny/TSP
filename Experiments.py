# initialize geolocator
import geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="my_app")

# ask user for three postcodes
postcode1 = input("Enter first postcode: ")
postcode2 = input("Enter second postcode: ")
postcode3 = input("Enter third postcode: ")

# get latitude and longitude of each postcode
location1 = geolocator.geocode(postcode1)
location2 = geolocator.geocode(postcode2)
location3 = geolocator.geocode(postcode3)

# calculate distance between the first and second points
distance1_2 = geodesic((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).miles

# calculate distance between the second and third points
distance2_3 = geodesic((location2.latitude, location2.longitude), (location3.latitude, location3.longitude)).miles

# calculate distance between the first and third points
distance1_3 = geodesic((location1.latitude, location1.longitude), (location3.latitude, location3.longitude)).miles

print(f"Distance between {postcode1} and {postcode2}: ", distance1_2)
print(f"Distance between {postcode2} and {postcode3}: ", distance2_3)
print(f"Distance between {postcode1} and {postcode3}: ", distance1_3)

