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

# Python

from itertools import permutations

# Create a list of all locations
locations = [location1, location2, location3]
postcodes = [postcode1, postcode2, postcode3]

# Create a list of all possible permutations of these locations
perms = permutations(range(len(locations)))

# Initialize variables to keep track of the shortest route and its distance
shortest_route = None
shortest_distance = None

# For each permutation, calculate the total distance of the route
for perm in perms:
    total_distance = 0
    for i in range(len(perm) - 1):
        total_distance += geodesic((locations[perm[i]].latitude, locations[perm[i]].longitude), (locations[perm[i+1]].latitude, locations[perm[i+1]].longitude)).miles
    # Add distance from last location back to the first
    total_distance += geodesic((locations[perm[-1]].latitude, locations[perm[-1]].longitude), (locations[perm[0]].latitude, locations[perm[0]].longitude)).miles

    # If this route is shorter than the current shortest, update shortest_route and shortest_distance
    if shortest_distance is None or total_distance < shortest_distance:
        shortest_route = perm
        shortest_distance = total_distance

# Print the shortest route and its distance
print("Shortest route: ", end="")
for i in shortest_route:
    print(postcodes[i], end=" -> ")
print(postcodes[shortest_route[0]])
print(f"Distance of shortest route: {shortest_distance}")



# Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/shortest_route', methods=['POST'])
def shortest_route():
    postcodes = request.json['postcodes']
    # existing logic to calculate shortest route and distance
    # ...
    return jsonify({'shortest_route': shortest_route, 'distance': shortest_distance})

if __name__ == '__main__':
    app.run(debug=True)