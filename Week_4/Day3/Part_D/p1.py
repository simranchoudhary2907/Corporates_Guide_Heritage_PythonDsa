class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    # DIRECTED EDGE (IMPORTANT CHANGE)
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)   # only u -> v (no reverse edge)

    def display(self):
        print("\nDirected Graph (Adjacency List):")
        for node in self.graph:
            print(node, "->", self.graph[node])


# ---------------- TEST ----------------

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

g.display()