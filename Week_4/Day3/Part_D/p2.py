from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)   # directed graph

    # ---------------- HAS PATH (BFS) ----------------
    def has_path(self, src, dest):
        if src not in self.graph or dest not in self.graph:
            return False

        visited = set()
        queue = deque([src])

        while queue:
            node = queue.popleft()

            if node == dest:
                return True

            if node not in visited:
                visited.add(node)

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return False


# ---------------- TEST ----------------

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

print("A -> D :", g.has_path("A", "D"))
print("C -> B :", g.has_path("C", "B"))