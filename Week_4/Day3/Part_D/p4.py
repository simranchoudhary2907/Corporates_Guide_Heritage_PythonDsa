class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)   # undirected graph

    # ---------------- DFS helper ----------------
    def _dfs(self, node, visited):
        visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    # ---------------- COUNT COMPONENTS ----------------
    def count_components(self):
        visited = set()
        count = 0

        for node in self.graph:
            if node not in visited:
                self._dfs(node, visited)
                count += 1

        print("\nNumber of disconnected components:", count)
        return count


# ---------------- TEST ----------------

g = Graph()

# Component 1
g.add_edge("A", "B")
g.add_edge("B", "C")

# Component 2
g.add_edge("D", "E")

# Component 3 (isolated node)
g.add_vertex("F")

# Run
g.count_components()