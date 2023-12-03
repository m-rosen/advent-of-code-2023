from sys import argv
import time

def read_input(f):
  pass

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  read_input(open(argv[1]))
  print(round(time.time() - start_t, 3), 's')

''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  read_input(open(argv[1]))
  print(round(time.time() - start_t, 3), 's')
