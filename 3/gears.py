from sys import argv
import time

def read_input(f):
  return [l.strip() for l in f]


def is_adjacent(row, col, schematic):
  for r in [-1, 0, 1]:
    for c in [-1, 0, 1]:
      ri = min(len(schematic) - 1, max(0, row + r))
      ci = min(len(schematic[0]) - 1, max(0, col + c))
      symbol = schematic[ri][ci]
      if symbol and not symbol.isdigit() and not symbol == '.':
        return True
  return False


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  schematic = read_input(open(argv[1]))
  parts = []
  for i, line in enumerate(schematic):
    part_nr = ""
    is_part = False
    for j, c in enumerate(line):
      if c.isdigit():
        part_nr += c
        is_part |= is_adjacent(i, j, schematic)

      if not c.isdigit() or j == len(line)-1:
        if is_part:
          parts.append(int(part_nr))
        part_nr = ""
        is_part = False

  print(sum(parts))
  print(round(time.time() - start_t, 3), 's')


def build_schematic(lines):
  parts = []
  part_id = 0
  schematic = [["" for j in range(0, len(lines[0]))] for i in range(0, len(lines))]
  for i, line in enumerate(lines):
    number = ""
    start = -1
    for j, c in enumerate(line):
      if c.isdigit():
        number += c
        if start < 0:
          start = j
      else:
        schematic[i][j] = c

      if not c.isdigit() or j == len(line)-1:
        is_last = j == len(line)-1
        if number:
          for jj in range(start, j + is_last):
            schematic[i][jj] = part_id
          part_id += 1
          parts.append(int(number))
        number = ""
        start = -1
  return schematic, parts


def gear_ratio(i, j, schematic, parts):
  found_parts = set()
  for r in [-1, 0, 1]:
    for c in [-1, 0, 1]:
      ri = min(len(schematic) - 1, max(0, i + r))
      ci = min(len(schematic[0]) - 1, max(0, j + c))
      if type(schematic[ri][ci]) is int:
        found_parts.add(schematic[ri][ci])
  if len(found_parts) == 2:
    l = list(found_parts)
    return int(parts[l[0]]) * int(parts[l[1]])
  return -1


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  schematic, parts = build_schematic(read_input(open(argv[1])))

  # for line in schematic:
  #   print(line)
  # print(parts)

  ratios = 0
  for i, line in enumerate(schematic):
    for j, c in enumerate(line):
      if c == '*':
        ratio = gear_ratio(i,j, schematic, parts)
        if ratio > 0:
          ratios += ratio
  print(ratios)

  print(round(time.time() - start_t, 3), 's')
