import osmnx as ox
import networkx as nx
from . import router
from .map import get_graph, load_graph
from .priority_queue import PriorityQueue

from .router import distance


class AStarNode:

    def __init__(self, node, previous, cost, id):
        self.node = node
        self.id = id
        self.previous = previous
        self.start_dist = 0  # Distance to start node
        self.end_dist = 0  # Distance to goal node
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




def find_path(node1, node2):

    graph= load_graph()

    start_id = ox.get_nearest_node(graph, node1)
    start_node = graph.nodes[start_id]

    end_id = ox.get_nearest_node(graph, node2)
    end_node = graph.nodes[end_id]

    open = PriorityQueue()
    closed = {}

    start = AStarNode(start_node, None, 0, start_id)
    end = AStarNode(end_node, None, 0, end_id)
    open.put(start, 0)
    result = []
    while not open.empty():

        #print('Open count: %d, Closed count: %d' % (len(open.elements), len(closed)))
        current_node = open.get()
        closed[current_node.id] = current_node

        if (current_node.id == end.id):
            path = []
            while current_node.id != start.id:
                # y to lat a y to lng
                #print((current_node.node['y'], current_node.node['x']))
                path.append((current_node.node['y'], current_node.node['x']))
                current_node = current_node.previous
            result = path[::-1]
            return result

        neighbors = find_neighbors(current_node, graph)
        for next_id in neighbors:
            neighbor = AStarNode(graph.nodes[next_id], current_node, 0, next_id)
            neighbor.time = current_node.time + graph.edges[(current_node.id, neighbor.id, 0)]['travel_time']

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




def find_neighbors(node, graph):
    neighbours= []

    neighbours=([ v for u, v, k, d in graph.edges(keys=True, data=True) if u == node.id])



    return neighbours

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
        return 60
    elif float(node1.previous.node['x'])== float(node2.node['x']) and float(node1.previous.node['y'])==float(node2.node['y']):
        return 60
    else:
        return 0


def should_consider(open, node):
    for n in open.elements:
        if (n[1].id == node.id and node.cost >= n[1].cost):
            return False
    return True










