def get_number_of_islands(binaryMatrix):
  M = len(binaryMatrix)
  N = len(binaryMatrix[0])

  number_of_islands = 0
  for i in range(M):
    for j in range(N):
      if binaryMatrix[i][j] == 1:
        binaryMatrix[i][j] = 0
        helper([i,j], binaryMatrix)
        number_of_islands += 1
  return number_of_islands

def helper(pos, matrix):
  i = pos[0]
  j = pos[1]
  M = len(matrix)
  N = len(matrix[0])
  # base case to return on here
  # if all the surrounding positions are zero then return
  
  # need checking for the i and j
  try: 
    a = matrix[i - 1][j]
  except:
    a = 0
  try:
    b = matrix[i][j-1]
  except:
    b = 0
  try:
    c = matrix[i][j+1] 
  except:
    c = 0
  try:
    d = matrix[i+1][j]
  except:
    d = 0
  if (a + b + c + d) == 0:
    return 
  
  if (i + 1) < M and (i + 1) > 0:
    if matrix[i+1][j] == 1:
      matrix[i+1][j] = 0
      helper([i + 1, j], matrix)
  if (i - 1) < M and (i + 1) > 0:
    if matrix[i-1][j] == 1:
      matrix[i-1][j] = 0
      helper([i - 1, j], matrix)
      
      # mark as island
  if (j + 1) < N and (j + 1) > 0:
    if matrix[i][j+1] == 1:
      matrix[i][j+1] = 0
      helper([i, j+1], matrix)
      
      # mark as island
  if (j - 1) < N and (j - 1) > 0:
    if matrix[i][j-1] == 1:
      matrix[i][j - 1] = 0
      helper([i, j - 1], matrix)


  
binaryMatrix = [ [0,    1,    0,    1,    0],
                 [0,    0,    1,    1,    1],
                 [1,    0,    0,    1,    0],
                 [0,    1,    1,    0,    0],
                 [1,    0,    1,    0,    1] ]
print get_number_of_islands(binaryMatrix)
# output = 6