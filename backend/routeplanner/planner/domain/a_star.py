
import osmnx as ox
import networkx as nx

from . import router
from .map import get_graph
from .router import distance


class AStarNode:

    def __init__(self, node, parent: (), f):
        self.node= node
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.lc = 0  # Left turns cost
        self.f = f # Total cost

        # # Compare nodes
        # def __eq__(self, other):
        #     return self.node['osmid'] == other.node['osmid']

# nie kończy nigdy wyszukiwać, nie wiem gdzie błąd
def find_path(node1, node2):


    # skąd graf ? wszystkie sąsiednie nody muszę być w grafie, aby obliczać g w 97 linii
    graph= get_graph("Warszawa", 'drive')

    # graph = ox.add_edge_speeds(graph, fallback = 50)
    # graph = ox.add_edge_travel_times(graph)

    node3=graph.nodes[ox.get_nearest_node(graph,(node1[1],node1[0]), method='haversine')]



    node4 = graph.nodes[ox.get_nearest_node(graph, (node2[1], node2[0]), method='haversine')]



    #route = nx.shortest_path(graph, node3['osmid'], node4['osmid'], weight='travel_time')





    open =[]
    closed =[]

    start= AStarNode(node3,  None, 0)
    end= AStarNode(node4,  None, 0)
    open.append( start)


    while len(open)>0:
       # print("node")

        open.sort(key=lambda x: x.f, reverse=False)

        current_node =open.pop(0)
        closed.append(current_node)
        print(current_node.node)


        if(current_node.node['osmid']== end.node['osmid']):
            path = []
            while current_node.node != start.node:
                    path.append((current_node.node['x'], current_node.node['y']))
                    print(current_node.node['osmid'])
                    current_node = current_node.parent
            return path[::-1]

        neighbors= find_neighbors(current_node, graph)
        for next in neighbors:

            neighbor= AStarNode(graph.nodes[next], current_node.node, 0)
            #neighbor.node musi być w grafie
            neighbor.g = current_node.g + graph.edges[(current_node.node['osmid'], neighbor.node['osmid'], 0)]['travel_time']

            neighbor.h =(distance((current_node.node['y'], current_node.node['x']), (end.node['y'], end.node['x'])))/60

            if(current_node.parent is not None):
                neighbor.lc = current_node.lc + check_turn(current_node, neighbor)
            else:
                neighbor.lc = current_node.lc + check_first_turn(current_node.node, neighbor.node)

            neighbor.f = neighbor.g + neighbor.h + neighbor.lc

            is_in_closed = False
            for c in closed:
                if c.node['osmid'] == neighbor.node['osmid'] and c.f <= neighbor.f:
                    is_in_closed = True
                    break
            if is_in_closed:
                break

            if (add_to_open(open, neighbor) == True):
                open.append(( neighbor))



    return []


def find_neighbors(node, graph):
    neighbours= []

    neighbours=([ v for u, v, k, d in graph.edges(keys=True, data=True) if u== node.node['osmid']])



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
        if (n.node['osmid'] == node.node['osmid'] and node.f >= n.f):
            return False
    return True












