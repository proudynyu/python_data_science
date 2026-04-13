import math

class SimpleMath:
    def sum(x, y):
        return x + y

    def sub(x, y):
        return x - y
    
    def mult(x, y):
        return x * y

    def div(x, y):
        return x / y

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(f"x: {self.x}, y: {self.y}")

    def sum(v1, v2):
        return Vector2d(v1.x + v2.x, v1.y + v2.y)

    def mult(v1, v2):
        return Vector2d( v1.x * v2.x, v1.y * v2.y)

    def div(v1, v2):
        return Vector2d(v1.x / v2.x, v1.y / v2.y)

    def scalar(v1, s):
        return Vector2d(v1.x * s, v1.y * s)
    
    def distance(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

class Matrix:
    def __init__(self, arr):
        if isinstance(arr[0], list):
            size_cols = len(arr[0])
            for row in arr:
                if len(row) != size_cols:
                    raise ValueError("Columns must have the same size")
            self.arr = arr
        else:
            self.arr = [arr]

    def print(self):
        print(f'Matrix: {self.arr}, shape: {self.shape()}')

    def shape(self):
        row = len(self.arr)
        col = len(self.arr[0])
        return (row, col)

    def transpose(self):
        original = self.arr
        rows = len(original)
        cols = len(original[0])
        shape = [[0 for _ in range(rows)] for _ in range(cols)]
        new = Matrix(shape)

        for i in range(rows):
            for j in range(cols):
                new.arr[j][i] = original[i][j]

        return new

    def mult(m1, m2):
        pass

    def inverse(self):
        pass

m = Matrix([[1, 2, 3], [4, 5, 6]])
m.print()

mt = m.transpose()
mt.print()
