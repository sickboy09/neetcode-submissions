class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        prefix_matrix = [[0] * (cols+1) for _ in range(rows+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                prefix_matrix[i+1][j+1] = prefix_matrix[i][j+1] + prefix_matrix[i+1][j] + matrix[i][j] - prefix_matrix[i][j]
        self.matrix = prefix_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # sum = self.matrix[row2+1][col2+1] - self.matrix[row1][col1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] + 2*self.matrix[row1][col1]
        sum = self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] + self.matrix[row1][col1]
        return sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)