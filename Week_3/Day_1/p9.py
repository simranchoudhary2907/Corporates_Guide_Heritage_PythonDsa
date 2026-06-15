event1 = {"Aman", "Riya", "Karan", "Neha"}
event2 = {"Neha", "Riya", "Vikas", "Rohan"}

print("Both Events:",
      event1.intersection(event2))

print("Exactly One Event:",
      event1.symmetric_difference(event2))

print("Total Unique Attendees:",
      len(event1.union(event2)))