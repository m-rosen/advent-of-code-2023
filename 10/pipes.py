from sys import argv
import time

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
  path = []
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
  

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  board = read_input(open(argv[1]))

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
  print((len(path)+1)/2)
  print(round(time.time() - start_t, 3), 's')


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  read_input(open(argv[1]))
  print(round(time.time() - start_t, 3), 's')
