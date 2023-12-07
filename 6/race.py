from sys import argv
import time
import math


def read_input(f):
  times = [int(i) for i in f.readline().split(':')[1].split()]
  distances = [int(i) for i in f.readline().split(':')[1].split()]
  return times, distances


def solve(t, r):
  root = math.sqrt(t**2/4 - r)
  start = math.ceil(-root + t/2)
  end = math.floor(root + t/2)
  return end - start + 1


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  times, records = read_input(open(argv[1]))
  charges = []
  for i in range(len(times)):
    t = times[i]; r = records[i] + 1
    charges.append(solve(t, r))
  print(charges)
  res = 1
  for c in charges:
    res *= c
  print(res)
  print(round(time.time() - start_t, 3), 's')


def read_input_2(f):
  time = int(f.readline().split(':')[1].replace(" ", ""))
  dist = int(f.readline().split(':')[1].replace(" ", ""))
  return time, dist


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  t, r = read_input_2(open(argv[1]))
  print(solve(t, r))
  print(round(time.time() - start_t, 3), 's')
