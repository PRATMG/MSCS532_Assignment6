class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, value):
        self.data.append(value)  # Push to the top
    
    def pop(self):
        if not self.data:
            raise IndexError("Stack is empty")
        return self.data.pop()  # Remove the top element
    
    def peek(self):
        if not self.data:
            raise IndexError("Stack is empty")
        return self.data[-1]  # View the top element
    
    def is_empty(self):
        return len(self.data) == 0
    
    def display(self):
        return self.data

# Test stack implementation
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushes:", stack.display())  # [10, 20, 30]
stack.pop()  # Removes 30
print("Stack after pop:", stack.display())  # [10, 20]
print("Peek top element:", stack.peek())  # 20



class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, value):
        self.data.append(value)  # Add to the rear
    
    def dequeue(self):
        if not self.data:
            raise IndexError("Queue is empty")
        return self.data.pop(0)  # Remove from the front
    
    def front(self):
        if not self.data:
            raise IndexError("Queue is empty")
        return self.data[0]  # View the front element
    
    def is_empty(self):
        return len(self.data) == 0
    
    def display(self):
        return self.data

# Test queue implementation
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue after enqueues:", queue.display())  # [10, 20, 30]
queue.dequeue()  # Removes 10
print("Queue after dequeue:", queue.display())  # [20, 30]
print("Front element:", queue.front())  # 20
