from .map import WarsawGraph
from .priority_queue import PriorityQueue
from .a_star_node import AStarNode
from math import cos, sin, sqrt, pi, atan2

def find_path(start_point: tuple[float, float], end_point: tuple[float, float], graph: WarsawGraph):

    start_id = graph.get_node_id(start_point)
    start_node = graph.get_node(start_id)

    end_id = graph.get_node_id(end_point)
    end_node = graph.get_node(end_id)

    open = PriorityQueue()
    closed = {}

    start = AStarNode(start_node, None, 0, start_id)
    end = AStarNode(end_node, None, 0, end_id)
    open.put(start, 0)
    while not open.empty():

        current_node = open.get()
        closed[current_node.id] = current_node

        if (current_node.id == end.id):
            return __get_route(current_node, start)

        neighbors = find_neighbors(current_node, graph.edges)
        for next_id in neighbors:
            neighbor = __get_neighbor(graph, current_node, next_id)

            node_in_closed = closed.get(neighbor.id)
            if node_in_closed is not None and node_in_closed.cost <= neighbor.cost:
                continue

            if should_consider(open, neighbor):
                dist = distance((neighbor.node['y'], neighbor.node['x']), (end.node['y'], end.node['x']))
                open.put(neighbor, neighbor.cost + dist)
    # Return empty if can't find any 
    return []

def __get_route(current_node: AStarNode, start: AStarNode):
    path = []
    while current_node.id != start.id:
        path.append((current_node.node['y'], current_node.node['x']))
        current_node = current_node.previous
    return path[::-1]

def __get_neighbor(graph, current_node, neighbor_id):
    neighbor = AStarNode(graph.get_node(neighbor_id), current_node, 0, neighbor_id)
    neighbor.time = current_node.time + graph.get_travel_time(current_node.id, neighbor.id)

    if current_node.previous is not None:
        neighbor.left_cost = current_node.left_cost + check_turn(current_node, neighbor)
    else:
        neighbor.left_cost = 0

    neighbor.cost = neighbor.left_cost + neighbor.time
    return neighbor

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

left_turn_cost = 60

def find_neighbors(node, edges):
    return [ v for u, v, k, d in edges if u == node.id]

def check_first_turn(node1, node2):
    if node1['x']>node2['x'] and node1['y'] <node2['y'] or node1['x'] <node2['x'] and node1['y'] >node2['y']:
        return 60
    else:
        return 0


def check_turn(node1, node2):
    v1x = float(node1.node['x']) - float(node1.previous.node['x'])
    v1y = float(node1.node['y']) - float(node1.previous.node['y'])
    v2x = float(node2.node['x']) - float(node1.node['x'])
    v2y = float(node2.node['y']) - float(node1.node['y'])
    if v1x * v2y - v1y * v2x > 0.0:
        return left_turn_cost
    elif float(node1.previous.node['x'])== float(node2.node['x']) and float(node1.previous.node['y'])==float(node2.node['y']):
        return left_turn_cost
    else:
        return 0


def should_consider(open, node):
    for n in open.elements:
        if (n[1].id == node.id and node.cost >= n[1].cost):
            return False
    return True










