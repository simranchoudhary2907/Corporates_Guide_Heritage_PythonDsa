# insert_at_end()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head


def print_list(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create list
head = Node(3)
head = insert_at_end(head, 16)
head = insert_at_end(head, 9)
head = insert_at_end(head, 21)

# Print list
print_list(head)