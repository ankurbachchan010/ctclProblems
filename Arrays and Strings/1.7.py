import numpy

def rotate(matrix):
  N = len(matrix)
  for layer in range(N//2):
    first = layer
    last = N-1-first
    for i in range(first,last):
      offset = i-first
      top = matrix[first][i]
      matrix[first][i] = matrix[last-offset][first]
      matrix[last-offset][first] = matrix[last][last-offset]
      matrix[last][last-offset] = matrix[i][last]
      matrix[i][last] = top
  return matrix


matrix = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
print(matrix)
print(rotate(matrix))