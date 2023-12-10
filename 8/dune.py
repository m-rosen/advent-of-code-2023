from sys import argv
import time
import math

def read_input(f):
  moves = f.readline().strip()
  f.readline() # Remove empty line
  look_up = {}
  for line in f:
    node, neighbours =  line.split('=')
    node = node.strip()
    neighbours = neighbours.replace('(', ' ').replace(')', ' ').split(',')
    look_up[node] = [neighbours[0].strip(), neighbours[1].strip()]

  return moves, look_up


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  moves, look_up = read_input(open(argv[1]))

  DIR = {'L': 0, 'R': 1}
  i = 0
  current =  'AAA'
  while current != 'ZZZ':
    current = look_up[current][DIR[moves[i % len(moves)]]]
    i += 1
  print(i)
  print(round(time.time() - start_t, 3), 's')


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  moves, look_up = read_input(open(argv[1]))

  DIR = {'L': 0, 'R': 1}
  current = [n for n in look_up.keys() if n[-1] == 'A']
  
  cycles = []
  for node in current:
    i = 0
    cur = node
    steps = None
    while cur[-1] != 'Z':
      cur = look_up[cur][DIR[moves[i % len(moves)]]]
      i += 1
    cycles.append(i)
  
  res = math.lcm(*cycles)
    
  print(res)
  
  print(round(time.time() - start_t, 3), 's')
