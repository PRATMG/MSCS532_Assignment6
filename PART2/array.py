class Array:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of the array
        self.size = 0  # Current number of elements
        self.data = [None] * capacity  # Initialize array with None values
    
    def insert(self, index, value):
        if self.size == self.capacity:
            raise Exception("Array is full")
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        # Shift elements to the right to make room for the new element
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1
    
    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        # Shift elements to the left to fill the gap
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.data[self.size - 1] = None
        self.size -= 1
    
    def access(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]
    
    def display(self):
        return [self.data[i] for i in range(self.size)]

# Test array implementation
array = Array(5)
array.insert(0, 10)
array.insert(1, 20)
array.insert(2, 30)
array.insert(1, 15)  # Insert at index 1
print("Array after insertions:", array.display())  # [10, 15, 20, 30]
array.delete(2)  # Delete element at index 2
print("Array after deletion:", array.display())  # [10, 15, 30]
print("Access element at index 1:", array.access(1))  # 15
