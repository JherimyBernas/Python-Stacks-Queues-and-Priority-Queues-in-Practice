import networkx as nx
from GRAPH import City, load_graph, shortest_path, connected


print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2")
print("Shortest Path Using Breadth-First Traversal")


def by_latitude(city):
    return -city.latitude


print("\n-----------------------------------------------------------------------------------------------------------\n")
nodes, graph = load_graph("roadmap.dot", City.from_dict)
city1 = nodes["aberdeen"]
city2 = nodes["perth"]
for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))

print("\n-----------------------------------------------------------------------------------------------------------\n")
print(" → ".join(city.name for city in shortest_path(graph, city1, city2)))
print()

print(" → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)
))

print("\n-----------------------------------------------------------------------------------------------------------\n")
print(connected(graph, nodes["belfast"], nodes["glasgow"]))
print(connected(graph, nodes["belfast"], nodes["derry"]))
