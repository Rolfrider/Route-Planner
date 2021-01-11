import osmnx as ox
import networkx as nx
from os.path import isfile
ox.config(use_cache=True, log_console=True)

def get_graph(place: str = 'Warsaw', type: str = 'drive'):
    warsaw_streets = ox.graph_from_place(place, network_type=type)
    warsaw_streets = ox.add_edge_speeds(warsaw_streets)
    warsaw_streets = ox.add_edge_travel_times(warsaw_streets)
    return warsaw_streets

def save_graph():
    warsaw_streets = ox.graph_from_place('Warsaw', network_type='drive')
    warsaw_streets = ox.add_edge_speeds(warsaw_streets)
    warsaw_streets = ox.add_edge_travel_times(warsaw_streets)
    ox.save_graphml(warsaw_streets, "warsaw.graphml")

def load_graph():
    return ox.load_graphml("warsaw.graphml")

def check_graph():
    return isfile("warsaw.graphml")

# TODO: remove when not needed
def get_stub_path():
    warsaw_streets = load_graph()
    start_node = ox.get_nearest_node(warsaw_streets, (52.1634477, 21.0221398))
    end_node = ox.get_nearest_node(warsaw_streets, (52.1614477, 21.1211398))
    route = nx.shortest_path(warsaw_streets, start_node, end_node, weight='travel_time')
    return [{"lng": warsaw_streets.nodes[node]['x'], "lat": warsaw_streets.nodes[node]['y']} for node in route]