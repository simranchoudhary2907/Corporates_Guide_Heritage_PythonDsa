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
        self.graph[v].append(u)   # undirected for social network

    # ---------------- 2-CONNECTION BFS ----------------
    def within_2_connections(self, start):
        visited = set([start])
        queue = deque([(start, 0)])  # (node, level)

        result = []

        while queue:
            node, level = queue.popleft()

            if level == 2:
                continue

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    result.append(neighbor)
                    queue.append((neighbor, level + 1))

        print(f"\nPeople within 2 connections of {start}:")
        print(result)
        return result


# ---------------- SOCIAL NETWORK ----------------

g = Graph()

# 6 people network
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("B", "F")
g.add_edge("E", "F")

# Run query
g.within_2_connections("A")