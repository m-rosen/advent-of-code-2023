from sys import argv
import time

def read_input(f):
  return [line.strip().split() for line in f]


DIR = { 'R' : (0, 1), 'L' : (0, -1), 'U' : (-1, 0), 'D' : (1, 0)}


def move(pos, dir, steps = 1):
  return tuple(p + d * steps for p,d in zip(pos, dir))


def is_corner(pos, border):
  i, j = pos
  return ((i-1, j) in border and (i, j+1) in border) \
      or ((i+1, j) in border and (i, j-1) in border)
    

def inside(pos, border, min_i, min_j):
  if pos in border:
    return 1
  intersect = 0
  i, j = pos; ci = i-1; cj = j-1
  while ci >= min_i and cj >= min_j:
    if (ci, cj) in border and not is_corner((ci, cj), border):
      intersect += 1
    ci -= 1; cj -= 1
  return intersect % 2


def inside_loop(i, j, loop, board):
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


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  moves = read_input(open(argv[1]))

  current = (0,0)
  path = { current }
  for dir, steps, color in moves:
    for step in range(int(steps)):
      current = move(current, DIR[dir])
      path.add(current)

  i_s, j_s = zip(*path)
  i_s = set(i_s); j_s = set(j_s)

  # for i in i_s:
  #   print(''.join(['#' if (i,j) in path else '.' for j in j_s]))
  # print()

  lagoon = set()
  for i in i_s:
    for j in j_s:
      if inside((i,j), path, min(i_s), min(j_s)):
        lagoon.add((i,j))

  # for i in set(i_s):
  #   print(''.join(['#' if (i,j) in lagoon else '.' for j in set(j_s)]))

  print(len(lagoon))

  print(round(time.time() - start_t, 3), 's')

''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  read_input(open(argv[1]))
  print(round(time.time() - start_t, 3), 's')
