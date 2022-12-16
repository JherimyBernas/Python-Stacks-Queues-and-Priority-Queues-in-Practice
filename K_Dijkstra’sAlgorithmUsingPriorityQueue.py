import networkx as nx
from GRAPH import City, load_graph, dijkstra_shortest_path

print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2")
print("Dijkstra’s Algorithm Using a Priority Queue")

print("\n-----------------------------------------------------------------------------------------------------------\n")
nodes, graph = load_graph("roadmap.dot", City.from_dict)
city1 = nodes["london"]
city2 = nodes["edinburgh"]


def distance(weights):
    return float(weights["distance"])


for city in dijkstra_shortest_path(graph, city1, city2, distance):
    print(city.name)


def weight(node1, node2, weights):
    return distance(weights)


for city in nx.dijkstra_path(graph, city1, city2, weight):
    print(city.name)