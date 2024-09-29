class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[None] * cols for _ in range(rows)]
    
    def insert(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.data[row][col] = value
    
    def access(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        return self.data[row][col]
    
    def display(self):
        for row in self.data:
            print(row)

# Test matrix implementation
matrix = Matrix(3, 3)
matrix.insert(0, 0, 1)
matrix.insert(0, 1, 2)
matrix.insert(1, 1, 5)
print("Matrix:")
matrix.display()  # Should display the matrix with the inserted elements
print("Access element at (1,1):", matrix.access(1, 1))  # 5
