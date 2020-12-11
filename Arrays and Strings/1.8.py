import numpy

def zeromatrix(matrix):
  row_zero = False
  col_zero = False

# first row Zero
  for i in range (len(matrix[0])):
    if matrix[0][i] == 0:
      row_zero = True
      break

# first col zero
  for i in range (len(matrix)):
    if matrix[i][0] == 0:
      col_zero = True
      break

# all zero
  for i in range (1, len(matrix)):
    for j in range (1, len(matrix[0])):
      if matrix[i][j] == 0:
        matrix [i][0] = 0
        matrix [0][j] = 0

#row zero nullify
  for i in range (1,len(matrix)):
    if matrix[i][0] == 0:
      row_nullify(matrix, i)

#col zero nullify
  for i in range (1,len(matrix[0])):
    if matrix[0][i] == 0:
      col_nullify(matrix, i)

  if row_zero:
    for i in range (len(matrix[0])):
      matrix[0][i] = 0

  if col_zero:
    for i in range (len(matrix)):
      matrix[i][0] = 0

  return matrix

def row_nullify(matrix, row):
  for i in range (1, len(matrix[0])):
      matrix[row][i] = 0

def col_nullify(matrix, col):
  for i in range (1, len(matrix)):
      matrix[i][col] = 0

matrix = numpy.array([[1,2,6,4],[8,0,0,7],[6,5,6,4]])
print(matrix)
print (zeromatrix(matrix))