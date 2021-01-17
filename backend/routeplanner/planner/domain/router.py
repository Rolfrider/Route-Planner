from .map import WarsawGraph
from .a_star import find_path, distance

def route_for(places):
    # sort places by distance
    sorted_places = sort_by_dist(places)
    # find nodes between points
    nodes = []
    graph = WarsawGraph()
    for p, next_p in zip(sorted_places[:-1], sorted_places[1:]):
        nodes.append(p)
        nodes += find_path(p, next_p, graph)
    return list(map(lambda x: {"lat": x[0], "lng": x[1]}, nodes))

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