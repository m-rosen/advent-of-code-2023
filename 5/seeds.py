from sys import argv
import time
from interval import Interval

levels = [
  "seed->soil", 
  "soil->fertilizer",
  "fertilizer->water",
  "water->light",
  "light->temperature",
  "temperature->humidity",
  "humidity->location"
]

def read_input(f):
  seeds = [int(i) for i in f.readline().split(':')[1].split()]

  layers = []
  layer = []
  for line in f:
    if line.find("map:") > 0 or line == '\n':
      if layer:
        layers.append(sorted(layer))
        layer = []
    else:
      dst, src, rng = [int(i) for i in line.split()]
      layer.append([src, src + rng - 1, dst-src])
  
  layers.append(sorted(layer)) ## Add last layer
  return seeds, layers


def next_node(current, map):
  for start, end, diff in map:
    if start <= current <= end:
      return current + diff
  return current


def find_paths(seeds, layers):
  paths = [[s] for s in seeds]
  for i,layer in enumerate(layers):
    for path in paths:
      path.append(next_node(path[i], layer))  
  return paths


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  seeds, layers = read_input(open(argv[1]))

  paths = find_paths(seeds, layers)

  locations = [p[-1] for p in paths]
  print(min(locations))
  print(round(time.time() - start_t, 3), 's')


def read_input_2(f):
  seeds = [int(i) for i in f.readline().split(':')[1].split()]
  seed_intervals = []
  for i in range(0, len(seeds), 2):
    seed_intervals.append(Interval(seeds[i], seeds[i]+ seeds[i+1] - 1))
  seed_intervals.sort()

  layers = []
  layer = []
  for line in f:
    if line.find("map:") > 0 or line == '\n':
      if layer:
        layers.append(sorted(layer))
        layer = []
    else:
      dst, src, rng = [int(i) for i in line.split()]
      layer.append(Interval(src, src + rng - 1, dst-src))
  
  layers.append(sorted(layer)) ## Add last layer
  return seed_intervals, layers


def split(intervals, bins):
  new_intervals = []
  for i in intervals:
    new_intervals += i.split(bins)
  return new_intervals


def merge(intervals):
  intervals.sort()
  result = []
  i = 0; j = 1
  while i < len(intervals) and j < len(intervals):
    current = intervals[i]
    while new_interval := current.merge(intervals[j]):
      current = new_interval
      j += 1
    result.append(current)
    i = j
    j += 1

  result.append(intervals[i])
  return result


def find_paths_interval(intervals, layers):
  current = intervals
  for i, bins in enumerate(layers):
    current = split(current, bins)
    next = []
    for interval in current:
      next.append(interval.slide(interval.weight))
    current = merge(next)
  current.sort()
  return current[0].start


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  seeds, layers = read_input_2(open(argv[1]))
  print(find_paths_interval(seeds, layers))
  print(round(time.time() - start_t, 3), 's')
