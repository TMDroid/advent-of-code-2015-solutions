import re
import networkx as nx
import random

with open("input") as f:
    content = f.readlines()


def tsp(G, weight='weight'):
    nodes = list(G.nodes)
    visited = []
    bestPath = []

    node = nodes[random.randint(0, len(nodes) - 1)]
    nodes.remove(node)
    while len(nodes) > 0:
        paths = []
        for n in nodes:
            if n not in visited:
                if n in G[node]:
                    w = {weight: G[node][n][weight]}
                    paths.append((node, n, w))

        if paths:
            best = min(paths, key=lambda x: x[2][weight])

            visited.append(best[0])
            visited.append(best[1])
            bestPath.append(best)
            nodes.remove(best[1])
            node = best[1]
        else:
            node = nodes[random.randint(0, len(nodes) - 1)]

    return bestPath


G = nx.Graph()
for line in content:
    data = list(re.findall(r'(\w+) to (\w+) = (\d+)', line)[0])
    data[2] = int(data[2])

    if data[0] not in G:
        G.add_node(data[0])

    if data[1] not in G:
        G.add_node(data[1])

    G.add_edge(data[0], data[1], weight=data[2])

best = tsp(G)
print(G.nodes)
print(best)

sum = 0
for path in best:
    sum += path[2]['weight']

print(sum)

'''
['Faerun', 'Tristram', 'Tambi', 'Norrath', 'Snowdin', 'Straylight', 'AlphaCentauri', 'Arbre']
['Faerun', 'Tambi', 'Norrath', 'Snowdin', 'Straylight', 'AlphaCentauri']
'''
