from sys import argv
import time

def read_input(f):
  return [token for token in f.readline().strip().split(',')]


def hash(str):
  current = 0
  for c in str:
    current = ((current + ord(c)) * 17) % 256
  return current

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  lines = read_input(open(argv[1]))

  total = 0
  for str in lines:
    total += hash(str)
  print(total)

  print(round(time.time() - start_t, 3), 's')


def focal_power(box, nr):
  list, map = box
  power = 0
  for i, label in enumerate(list):
    power += (nr + 1) * (i + 1) * map[label]
  return power


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  lines = read_input(open(argv[1]))

  boxes = [([],{}) for i in range(256)]
  for str in lines:
    if str[-1] == '-':
      label = str[:-1]
      box_nr = hash(label)
      list, map = boxes[box_nr]
      if label in map:
        list.remove(label)
        del map[label]

    else:
      label, lens = str.split('=')
      box_nr = hash(label)
      list, map = boxes[box_nr]
      if label not in map:
        list.append(label)
      map[label] = int(lens)

  total = 0
  for i, box in enumerate(boxes):
    total += focal_power(box, i)
  print(total)
  
  print(round(time.time() - start_t, 3), 's')
