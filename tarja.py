import networkx as nx

# Construir grafo exemplo
G = nx.Graph()
# Comunidade A (escola)
A = [f"A{i}" for i in range(1,7)]
# Comunidade B (empresa)
B = [f"B{i}" for i in range(1,7)]
# Comunidade C (asilo)
C = [f"C{i}" for i in range(1,4)]

# conectar internamente (quase-clique)
for group in [A,B]:
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            G.add_edge(group[i], group[j])

# asilo menos conectado
for i in range(len(C)):
    for j in range(i+1, len(C)):
        G.add_edge(C[i], C[j])

# Pontes entre comunidades
G.add_edge("A6", "B1")  # ponte A-B
G.add_edge("B5", "C1")  # ponte B-C

# Encontrar bridges (pontes)
bridges = list(nx.bridges(G))
print("Pontes detectadas:", bridges)

# Encontrar articulation points (vértices articuladores)
articulation = list(nx.articulation_points(G))
print("Articulation points:", articulation)
