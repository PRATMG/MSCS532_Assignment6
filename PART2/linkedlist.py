class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if not self.head:
            raise Exception("List is empty")
        
        # If the head node is to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return
        
        # Find the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next
        else:
            raise ValueError(f"Node with data {data} not found")
    
    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Test linked list implementation
linked_list = SinglyLinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
print("Linked list after insertions:", linked_list.traverse())  # [10, 20, 30]
linked_list.insert_at_beginning(5)
print("Linked list after insertion at beginning:", linked_list.traverse())  # [5, 10, 20, 30]
linked_list.delete(20)
print("Linked list after deletion of 20:", linked_list.traverse())  # [5, 10, 30]
