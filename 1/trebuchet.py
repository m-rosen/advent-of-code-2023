from sys import argv
import time


def read_input(f):
  return [l for l in f]
  

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  lines = read_input(open(argv[1]))
  
  numbers = []
  for line in lines:
    digits = [c for c in line if c.isdigit()]
    if digits:
      numbers.append(int(digits[0] + digits[-1]))
  
  print(sum(numbers))
  print(round(time.time() - start_t, 3), 's')


NUM = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
DIG = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def first(str):
  best = (100, 0)
  for i, n in enumerate(NUM):
    try:
      pos = str.index(n)
    except:
      pos = 100
    if pos < best[0]:
      best = (pos, i)
  for i in range(0, best[0]):
    if str[i].isdigit():
      return str[i]
  return DIG[best[1]]


def last(str):
  best = (0, 0)
  for i, n in enumerate(NUM):
    try:
      pos = str.rindex(n)
    except:
      pos = 0
    if pos > best[0]:
      best = (pos, i)
  for i in range(len(str)-1, best[0]-1, -1):
    if str[i].isdigit():
      return str[i]
  return DIG[best[1]]


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  lines = read_input(open(argv[1]))

  numbers = []
  for l in lines:
    a = first(l)
    b = last(l)
    print(a,b)
    numbers.append(int(a+b))
  
  print(numbers)
  print(sum(numbers))
  print(round(time.time() - start_t, 3), 's')
