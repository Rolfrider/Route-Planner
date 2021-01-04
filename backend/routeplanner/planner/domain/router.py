from .map import get_graph, get_stub_path
from math import cos, sin, sqrt, pi, atan2
from .a_star import find_path

def route_for(places):
    # sort places by distance
    sorted_places = sort_by_dist(places)
    # find nodes between points
    nodes = []
    for p, next_p in zip(sorted_places[:-1], sorted_places[1:]):
        nodes.append(p)
        nodes += find_path(p, next_p)
    return get_stub_path() # TODO: return nodes when find_path implemented

def sort_by_dist(places):
    sorted_places = [places.pop(0)]
    while len(places) != 0:
        index = find_nearest_index(sorted_places[-1], places)
        sorted_places.append(places.pop(index))
    return sorted_places

def find_nearest_index(place, places):
    nearest = 0
    dist = distance(place, places[nearest])
    for i in range(1, len(places)):
        new_dist = distance(place, places[i])
        if new_dist <= dist:
            nearest = i
            dist = new_dist
    return nearest

def distance(p1, p2):
    earth_radius = 6371*10**3 # in km
    lat1 = to_radians(p1[0])
    lat2 = to_radians(p2[0])
    delta_lat = to_radians(p2[0] - p1[0])
    delta_lan = to_radians(p2[1] - p1[1])
    a = (sin(delta_lat / 2)**2) + cos(lat1) * cos(lat2) * (sin(delta_lan / 2)**2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return earth_radius * c

def to_radians(value):
    return value * pi / 180