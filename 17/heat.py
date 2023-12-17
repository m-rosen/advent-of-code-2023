from sys import argv
import time
from queue import PriorityQueue

def read_input(f):
  return [line.strip() for line in f]

COL_LEN = 0
LINE_LEN = 0

def move(pos, dir):
  return tuple(p + d for p,d in zip(pos, dir))

def in_bounds(pos):
  i, j = pos
  return 0 <= i < COL_LEN and 0 <= j < LINE_LEN

DIRS = [(0,1), (0,-1), (1, 0), (-1, 0)]

def best_path(start, end, board, min_len, max_len):
  queue = PriorityQueue()
  queue.put((0, start, None, 1, [start]))
  best = 10000000000
  visited = {} # (node, prev, in_line) : heatloss
  while not queue.empty():
    heat_loss, node, prev, in_line, path = queue.get()

    if node == end and in_line > min_len:
      # for i in range(COL_LEN):
      #   print(''.join([board[i][j] if (i,j) not in path else '.' for j in range(LINE_LEN)]))
      # print()
      # print(heat_loss, len(path))
      # print(path)
      best = min(best, heat_loss)
      continue
    
    if heat_loss >= best:
      continue

    state = (node, prev, in_line)
    if state in visited and heat_loss >= visited[state]:
      continue
    else:
      visited[state] = heat_loss

    for dir in DIRS:
      next = move(node, dir)
      if next != prev and in_bounds(next):
        loss = int(board[next[0]][next[1]])
        if not prev or move(prev, move(dir, dir)) == next:
          if in_line < max_len + 1:
            queue.put((heat_loss + loss, next, node, in_line + 1, path + [next]))
        elif in_line > min_len:
          queue.put((heat_loss + loss, next, node, 2, path + [next]))
  return best


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  board = read_input(open(argv[1]))
  
  COL_LEN = len(board)
  LINE_LEN = len(board[0])
  
  print(best_path((0,0), (COL_LEN-1, LINE_LEN-1), board, 1, 3))

  print(round(time.time() - start_t, 3), 's')


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  board = read_input(open(argv[1]))
  
  COL_LEN = len(board)
  LINE_LEN = len(board[0])
  
  print(best_path((0,0), (COL_LEN-1, LINE_LEN-1), board, 4, 10))
  print(round(time.time() - start_t, 3), 's')
