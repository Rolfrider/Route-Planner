import osmnx as ox
import networkx as nx
ox.config(use_cache=True, log_console=True)

def get_graph():
    warsaw_streets = ox.graph_from_place("Warsaw", network_type="drive")
    warsaw_streets = ox.add_edge_speeds(warsaw_streets)
    warsaw_streets = ox.add_edge_travel_times(warsaw_streets)
    start_node = ox.get_nearest_node(warsaw_streets, (52.1634477, 21.0221398))
    end_node = ox.get_nearest_node(warsaw_streets, (52.1614477, 21.1211398))
    route = nx.shortest_path(warsaw_streets, start_node, end_node, weight='travel_time')
    node_start = []
    node_end = []
    X_to = []
    Y_to = []
    X_from = []
    Y_from = []
    length = []
    travel_time = []

    for u, v in zip(route[:-1], route[1:]):
        node_start.append(u)
        node_end.append(v)
        length.append(round(warsaw_streets.edges[(u, v, 0)]['length']))
        travel_time.append(round(warsaw_streets.edges[(u, v, 0)]['travel_time']))
        X_from.append(warsaw_streets.nodes[u]['x'])
        Y_from.append(warsaw_streets.nodes[u]['y'])
        X_to.append(warsaw_streets.nodes[v]['x'])
        Y_to.append(warsaw_streets.nodes[v]['y'])

    response_data = {}
    response_data['X'] = X_to
    response_data['Y'] = Y_to
    return response_data