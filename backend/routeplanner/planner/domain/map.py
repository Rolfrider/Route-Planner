import osmnx as ox
import networkx as nx
from os.path import isfile
ox.config(use_cache=True, log_console=True)

def save_graph():
    warsaw_streets = ox.graph_from_place('Warsaw', network_type='drive')
    warsaw_streets = ox.add_edge_speeds(warsaw_streets)
    warsaw_streets = ox.add_edge_travel_times(warsaw_streets)
    ox.save_graphml(warsaw_streets, "warsaw.graphml")

def load_graph():
    return ox.load_graphml("warsaw.graphml")

def check_graph():
    return isfile("warsaw.graphml")

class WarsawGraph:

    def __init__(self):
        self.graph = load_graph()
        self.edges = graph.edges(keys=True, data=True)

    def get_travel_time(self, node1_id, node2_id):
        return self.graph.edges[(node1_id, node2_id, 0)]['travel_time']
        
    def get_node_id(self, point):
        return ox.get_nearest_node(self.graph, point)

    def get_node(self, node_id):
        return self.graph.nodes[node_id]