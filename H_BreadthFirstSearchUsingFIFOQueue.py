import networkx as nx
from GRAPH import City, load_graph

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
    else:
        print("Not found")
print()



def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
    else:
        print("Not found")
print()



from GRAPH import (
    City,
    load_graph,
    breadth_first_traverse1,
    breadth_first_search1 as bfs,
)
def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
city.name
print()
for city in breadth_first_traverse1(graph, nodes["edinburgh"]):
    print(city.name)
print()



from GRAPH import (
    City,
    load_graph,
    breadth_first_traverse2,
    breadth_first_search2 as bfs,
)
def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
city.name
print()
for city in breadth_first_traverse2(graph, nodes["edinburgh"]):
    print(city.name)
print()

