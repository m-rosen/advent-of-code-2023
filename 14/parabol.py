from sys import argv
import time

def read_input(f):
  return [[c for c in line.strip()] for line in f]

LINE_LEN = 0
COL_LEN = 0

def tilt_north(board):
  for i in range(1, COL_LEN):
    for j in range(LINE_LEN):
      if board[i][j] == 'O':
        board[i][j] = '.'
        for k in range(i-1, -1, -1):
          if board[k][j] == '#' or board[k][j] == 'O':
            board[k+1][j] = 'O'
            break
          elif k == 0:
            board[k][j] = 'O'


def count_load(board):
  load = 0
  beam_len = COL_LEN
  for i, row in enumerate(board):
    load += row.count('O') * (beam_len - i)
  return load


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  board = read_input(open(argv[1]))
  LINE_LEN = len(board[0])
  COL_LEN = len(board)
  
  tilt_north(board)
  print(count_load(board))
  
  print(round(time.time() - start_t, 3), 's')


def tilt_south(board):
  for i in range(COL_LEN - 2, -1, -1):
    for j in range(LINE_LEN):
      if board[i][j] == 'O':
        board[i][j] = '.'
        for k in range(i+1, COL_LEN):
          if board[k][j] == '#' or board[k][j] == 'O':
            board[k-1][j] = 'O'
            break
          elif k == COL_LEN - 1:
            board[k][j] = 'O'


def tilt_west(board):
  for i in range(COL_LEN):
    for j in range(1, LINE_LEN):
      if board[i][j] == 'O':
        board[i][j] = '.'
        for k in range(j-1, -1, -1):
          if board[i][k] == '#' or board[i][k] == 'O':
            board[i][k+1] = 'O'
            break
          elif k == 0:
            board[i][k] = 'O'


def tilt_east(board):
  for i in range(COL_LEN):
    for j in range(LINE_LEN - 2, -1, -1):
      if board[i][j] == 'O':
        board[i][j] = '.'
        for k in range(j+1, LINE_LEN):
          if board[i][k] == '#' or board[i][k] == 'O':
            board[i][k-1] = 'O'
            break
          elif k == LINE_LEN - 1:
            board[i][k] = 'O'


def print_board(board):
  for line in board:
    print(''.join(line))
  print()


def spin(board, cycles):
  states = {}
  
  for i in range(cycles):
    current = ''.join([str_line for str_line in [''.join(line) for line in board]])
    if current in states:
      return i - states[current], i
    else:
      states[current] = i
    
    tilt_north(board)
    tilt_west(board)
    tilt_south(board)
    tilt_east(board)
  
  return cycles


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  board = read_input(open(argv[1]))
  LINE_LEN = len(board[0])
  COL_LEN = len(board)

  nr_cycles = 1000000000
  repetition_len, done = spin(board, nr_cycles)
  spin(board, (nr_cycles - done) % repetition_len)

  # print_board(board)
  print(count_load(board))
  
  print(round(time.time() - start_t, 3), 's')
