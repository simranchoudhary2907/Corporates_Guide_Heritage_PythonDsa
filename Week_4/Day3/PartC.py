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
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected graph

    def dfs(self, start):
        visited = set()
        order = []

        def dfs_recursive(node):
            visited.add(node)
            order.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)

        print("DFS Order:", " -> ".join(order))
        return order


# ---------------- RUN PART ----------------

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

g.dfs("A")