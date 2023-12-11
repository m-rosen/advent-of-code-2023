from sys import argv
import time
import math

def read_input(f):
  return [line.strip() for line in f]

def add(a, b):
  return (a[0] + b[0], a[1] + b[1])

def in_board(n, board):
  return 0 <= n[0] <= len(board) and 0 <= n[1] <= len(board[0])

NEIGHBOR = {  '|': [(-1,0), (1, 0)], '-': [( 0,-1), (0, 1)],
              'L': [(-1,0), (0, 1)], 'J': [(-1, 0), (0,-1)],
              '7': [( 1,0), (0,-1)], 'F': [( 1, 0), (0, 1)],
              'S': [], '.': []
}

def dfs(start, end, board):
  current = start
  prev = end
  path = [end]
  while current != end:
    if not in_board(current, board):
      return []
    path.append(current)
    pipe = board[current[0]][current[1]]

    n_offsets = NEIGHBOR[pipe]
    neighbors = [add(current, offset) for offset in n_offsets]

    if prev in neighbors:
      neighbors.remove(prev)
      prev = current
      current = neighbors[0]
    else:
      return []
    
  return path
  
def find_cycle(board):
  start = None
  for i, line in enumerate(board):
    if (j := line.find('S')) >= 0:
      start = (i,j)
      break
  start_nodes = [add(start, (-1,0)), add(start, (0,-1)), add(start, (0,1)), add(start, (1,0))]      
  for n in start_nodes:
    path = dfs(n, start, board)
    if path:
      break
  return path

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  board = read_input(open(argv[1]))
  path = find_cycle(board)
  print((len(path))/2)
  print(round(time.time() - start_t, 3), 's')


def inside_loop_2(i, j, loop, board):
  if (i,j) in loop:
    return 0
  intersect = 0
  ci = i-1; cj = j-1
  while ci >= 0 and cj >= 0:
    pipe = board[ci][cj]
    if (ci, cj) in loop and pipe != 'L' and pipe != '7':
      intersect += 1
    ci -= 1; cj -= 1
  return intersect % 2

''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  board = read_input(open(argv[1]))
  path = find_cycle(board)
  path = set(path)
  inside = 0
  for i, row in enumerate(board):
    for j, pipe in enumerate(row):
      if inside_loop(i,j, path, board):
        inside += 1
  print(inside)
  print(round(time.time() - start_t, 3), 's')

