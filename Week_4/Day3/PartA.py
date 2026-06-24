# Graph Class using Adjacency List

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store vertices and neighbors

    # Add a new vertex
    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    # Add an undirected edge
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)

        self.graph[u].append(v)
        self.graph[v].append(u)

    # Display adjacency list
    def display(self):
        print("Adjacency List:")
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")


# Create Graph
g = Graph()

# Add edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")
g.add_edge("E", "F")

# Display graph
g.display()


print("\nGraph Structure:")
print("""
      A
     / \\
    B   C
     \\ /
      D
      |
      E
      |
      F
""")