library_A = {"Rahul", "Amit", "Priya", "Sneha"}
library_B = {"Priya", "Karan", "Amit", "Vikram"}

print("Both Libraries:",
      library_A.intersection(library_B))

print("Either Library:",
      library_A.union(library_B))

print("Only Library A:",
      library_A.difference(library_B))