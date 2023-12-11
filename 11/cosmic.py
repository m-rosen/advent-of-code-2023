from sys import argv
import time

def read_input(f):
  image = [line.strip() for line in f]

  galaxies = []
  empty_rows = [True for _ in range(len(image[0]))]
  empty_cols = [True for _ in range(len(image))]
  
  for i, line in enumerate(image):
    for j, c in enumerate(line):
      if c == '#':
        galaxies.append((i,j))
        empty_rows[i] = False  
        empty_cols[j] = False

  empty_rows = {i for i,v in enumerate(empty_rows) if v }
  empty_cols = {i for i,v in enumerate(empty_cols) if v }
  
  return galaxies, empty_rows, empty_cols


def dist(a, b, empty_rows, empty_cols, expansion):
  dy = abs(b[0] - a[0]) \
      + sum([expansion for e in empty_rows if (b[0] < e <  a[0] or a[0] < e <  b[0])])

  dx = abs(b[1] - a[1]) \
      + sum([expansion for e in empty_cols if (b[1] < e <  a[1] or a[1] < e <  b[1])])
  return dy + dx


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  galaxies, e_rows, e_cols = read_input(open(argv[1]))

  total_dist = 0
  for i, g1 in enumerate(galaxies[:-1]):
    for g2 in galaxies[i+1:]:
      total_dist += dist(g1, g2, e_rows, e_cols, 1)

  print(total_dist)
  print(round(time.time() - start_t, 3), 's')


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  galaxies, e_rows, e_cols = read_input(open(argv[1]))

  total_dist = 0
  for i, g1 in enumerate(galaxies[:-1]):
    for g2 in galaxies[i+1:]:
      total_dist += dist(g1, g2, e_rows, e_cols, 1000000 - 1)

  print(total_dist)
  print(round(time.time() - start_t, 3), 's')
