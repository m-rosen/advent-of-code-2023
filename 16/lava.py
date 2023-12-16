from sys import argv
import time

def read_input(f):
  return [line.strip() for line in f]

LINE_LEN = 0
COL_LEN = 0

def inside_board(pos):
  i, j = pos
  return 0 <= i < COL_LEN and 0 <= j < LINE_LEN

def move(pos, dir):
  return (pos[0] + dir[0], pos[1] + dir[1])

def follow_beam(start, start_dir, board):
  visited = set()
  prev_states = set()
  beams = {(start, start_dir)}
  while len(beams) > 0:
    new_beams = set()
    for pos, dir in beams:
      if not inside_board(pos) or (pos, dir) in prev_states:
        continue
      visited.add(pos)
      prev_states.add((pos, dir))
      
      i, j = pos
      di, dj = dir
      tile = board[i][j]

      dirs = []
      if tile == '.':
        dirs.append(dir)
        
      elif tile == '\\':
        dirs.append((dj, di))
      
      elif tile == '/':
        dirs.append((-dj, -di))
      
      elif tile == '|':
        if di == 0: # Horizontal beam
          dirs.append((-1, 0))
          dirs.append(( 1, 0))
        else:
          dirs.append(dir)

      elif tile == '-':
        if dj == 0: # Vertical beam
          dirs.append((0,-1))
          dirs.append((0, 1))
        else:
          dirs.append(dir)
      
      for d in dirs:
        new_beams.add((move(pos, d), d))
    
    beams = new_beams
  return visited



''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  board = read_input(open(argv[1]))
  LINE_LEN = len(board[0])
  COL_LEN = len(board)

  visited = follow_beam((0,0), (0,1), board)
  print(len(visited))

  # for i in range(COL_LEN):
  #   line = ''.join(['#' if (i,j) in visited else '.' for j in range(LINE_LEN)])
  #   print(line)
  
  print(round(time.time() - start_t, 3), 's')

''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  board = read_input(open(argv[1]))
  LINE_LEN = len(board[0])
  COL_LEN = len(board)

  starts = [((0, j),(1, 0)) for j in range(LINE_LEN)] \
         + [((LINE_LEN - 1, j),(-1, 0)) for j in range(LINE_LEN)] \
         + [((i, 0),(0, 1)) for i in range(COL_LEN) ] \
         + [((i, COL_LEN - 1),(0, -1)) for i in range(COL_LEN) ]
  
  best = 0
  for pos, dir in starts:
    visited = follow_beam(pos, dir, board)
    best = max(best, len(visited))

  print(best)

  print(round(time.time() - start_t, 3), 's')
