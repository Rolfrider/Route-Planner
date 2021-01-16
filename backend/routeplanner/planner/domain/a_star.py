
import osmnx as ox
import networkx as nx

from . import router
from .map import get_graph
from .router import distance


class AStarNode:

    def __init__(self, node, parent: (), f, id):
        self.node= node
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.lc = 0  # Left turns cost
        self.f = f # Total cost
        self.id= id

        # # Compare nodes
        # def __eq__(self, other):
        #     return self.node['osmid'] == other.node['osmid']


def find_path(node1, node2):

    graph= get_graph("Warszawa", 'drive')

    # graph = ox.add_edge_speeds(graph, fallback = 50)
    # graph = ox.add_edge_travel_times(graph)

    start_id=ox.get_nearest_node(graph, (node1[0], node1[1]))
    start_node=graph.nodes[start_id]

    goal_id =ox.get_nearest_node(graph, (node2[0], node2[1]))
    goal_node = graph.nodes[goal_id]




    print("route")
    route=nx.shortest_path(graph, start_id, goal_id, weight='travel_time')
    for r in route:
        print(graph.nodes[r])





    open =[]
    closed =[]

    start= AStarNode(start_node,  None, 0, start_id)
    end= AStarNode(goal_node,  None, 0, goal_id)
    open.append( start)




    while len(open)>0:

        open.sort(key=lambda x: x.f, reverse=False)

        current_node =open.pop(0)
        closed.append(current_node)
        print(current_node.id)
        print(goal_id)


        if(current_node.id== goal_id):
            print("goaaaaaaaaaaaaaaaaal")
            path = []
            while (current_node.id != start_id):
                    path.append((current_node.node['y'], current_node.node['x']))
                    print(current_node.id)
                    current_node = current_node.parent
            return path[::-1]

        neighbors= find_neighbors(current_node, graph)
        for next in neighbors:

            neighbor= AStarNode(graph.nodes[next], current_node, 0,next)
            #neighbor.node musi być w grafie
            neighbor.g = current_node.g + graph.edges[(current_node.id, neighbor.id, 0)]['travel_time']
            neighbor.h =(distance((current_node.node['y'], current_node.node['x']), (end.node['y'], end.node['x'])))

            # if(current_node.parent is not None):
            #     neighbor.lc = current_node.lc + check_turn(current_node, neighbor)
            # else:
            #     neighbor.lc = current_node.lc + check_first_turn(current_node.node, neighbor.node)

            neighbor.f = neighbor.g + neighbor.h + neighbor.lc

            is_in_closed = False
            for c in closed:
                if c.id == neighbor.id and c.f <= neighbor.f:
                    is_in_closed = True
                    break
            if is_in_closed:
                print("continue")
                continue

            if (add_to_open(open, neighbor) == True):
                open.append(( neighbor))

    return []


def find_neighbors(node, graph):
    neighbours= []

    neighbours=([ v for u, v, k, d in graph.edges(keys=True, data=True) if u== node.id])



    return neighbours

def check_first_turn(node1, node2):
    if node1['x']>node2['x'] and node1['y'] <node2['y'] or node1['x'] <node2['x'] and node1['y'] >node2['y']:
        return 0.1
    else:
        return 0


def check_turn(node1, node2):
    v1x = float(node1.node['x']) - float(node1.parent['x'])
    v1y = float(node1.node['y']) - float(node1.parent['y'])
    v2x = float(node2.node['x']) - float(node1.node['x'])
    v2y = float(node2.node['y']) - float(node1.node['y'])
    if v1x * v2y - v1y * v2x > 0.0:
        return 0.1
    else:
        return 0


def add_to_open(open, node):
    for n in open:
        if (n.id == node.id and node.f >= n.f):
            return False
    return True












