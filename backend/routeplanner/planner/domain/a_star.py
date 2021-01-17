import osmnx as ox
import networkx as nx
from . import router
from .map import WarsawGraph
from .priority_queue import PriorityQueue

from .router import distance


class AStarNode:

    def __init__(self, node, previous, cost, id):
        self.node = node
        self.id = id
        self.previous = previous
        self.time = 0
        self.left_cost = 0  # Left turns cost
        self.cost = cost  # Total cost


    def __eq__(self, other):
        return self.id == other.id


    def __lt__(self, other):
        return self.id < other.id


    def __le__(self, other):
        return self.id <= other.id


    def __gt__(self, other):
        return self.id > other.id




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
    result = []
    while not open.empty():

        current_node = open.get()
        closed[current_node.id] = current_node

        if (current_node.id == end.id):
            path = []
            while current_node.id != start.id:
                path.append((current_node.node['y'], current_node.node['x']))
                current_node = current_node.previous
            result = path[::-1]
            return result

        neighbors = find_neighbors(current_node, graph.edges)
        for next_id in neighbors:
            neighbor = AStarNode(graph.get_node(next_id), current_node, 0, next_id)
            neighbor.time = current_node.time + graph.get_travel_time(current_node.id, neighbor.id)

            if (current_node.previous is not None):
                neighbor.left_cost = current_node.left_cost + check_turn(current_node, neighbor)
            else:
                neighbor.left_cost = 0

            neighbor.cost = neighbor.left_cost + neighbor.time

            tmp = closed.get(neighbor.id)
            if tmp is not None and tmp.cost <= neighbor.cost:
                continue

            if (should_consider(open, neighbor)):
                dist = distance((current_node.node['y'], current_node.node['x']), (end.node['y'], end.node['x']))
                open.put(neighbor, neighbor.cost + dist)

    return result


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










