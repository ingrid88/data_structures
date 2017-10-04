# ['1', '2', '.', '.', '.']

import numpy as np 

def sudoku_solve(board):
  # print board
  # if the board is filled check if its solved
  # if solved return
  if '.' not in set(np.array(board).flatten()):
  	if is_solved(board):
		print "True"
		print board
		return True
	else:
	    # print "False"
	    return False
  # Algorithm: 
  # 1. add value to each position that has a . recursively till board is filled 
  		# and check if board is solved
  # 2. if not, continue by adding another value to board
  for row in range(9):
    for col in range(9):
      if board[row][col] == '.':
        # input some value
        for i in range(1,10):
          board[row][col] = str(i)
          print "adding value {}".format(i)
          if sudoku_solve(board) == True:
            return True
          else:
            board[row][col] = "."
      
  
def is_solved(board):
  # is filled up 
  # if '.' in set(np.array(board).flatten()):
  # 	return False
  for row in range(9):
  	rs = []
  	cs = []
  	# rows and columns
  	# import pdb; pdb.set_trace()
  	for col in range(9):
		rs.append(board[row][col])
		cs.append(board[col][row])
  	# import pdb; pdb.set_trace()

	if len(set(rs)) != 9:
		return False
	if len(set(cs)) != 9:
		return False
	# box 0 - 3, 3 - 6, 6 - 9 unique values
	for x in range(0,9,3):
		for y in range(0,9,3):
			s = set([
			  board[x][y], 
			  board[x+1][y], 
			  board[x+2][y],
			  board[x][y+1], 
			  board[x][y+2], 
			  board[x+1][y+1], 
			  board[x+1][y+2], 
			  board[x+2][y+2], 
			  board[x+2][y+1]
			])
        if len(s) != 9:
          return False
  return True


board = [ 
	[ "6", "4", "8", "5", "3", "9", "7", "1", "2"], #5
	[ "5", ".", ".", "7", ".", "2", "6", "4", "8"], #3
	[ "7", "1", ".", "6", "4", "8", "5", "3", "9"],
	[ "4", "8", "5", "3", "9", "7", "1", "2", "6"],
	[ "3", ".", "7", "1", "2", "6", "4", "8", "5"],
	[ "1", "2", "6", "4", "8", "5", "3", "9", "7"],
	[ "8", "5", "3", "9", "7", "1", "2", "6", "4"], #7
	[ "9", "7", "1", "2", "6", "4", "8", "5", "3"],
	[ "2", "6", "4", "8", "5", "3", "9", "7", "1"],
]

sudoku_solve(board)