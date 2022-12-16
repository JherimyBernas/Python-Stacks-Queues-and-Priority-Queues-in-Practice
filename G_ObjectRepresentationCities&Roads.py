import networkx as nx
from GRAPH import City, load_graph

print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2")
print("Object Representation of the Cities and Roads")

print("\n-----------------------------------------------------------------------------------------------------------\n")
print(nx.nx_agraph.read_dot("roadmap.dot"))

print("\n-----------------------------------------------------------------------------------------------------------\n")
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])

print("\n-----------------------------------------------------------------------------------------------------------\n")
nodes, graph = load_graph("roadmap.dot", City.from_dict)
print(nodes["london"])
print()
print(graph)

print("\n-----------------------------------------------------------------------------------------------------------\n")
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)

print("\n-----------------------------------------------------------------------------------------------------------\n")
for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)

print("\n-----------------------------------------------------------------------------------------------------------\n")


def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))


def by_distance(weights):
    return float(weights["distance"])


for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")