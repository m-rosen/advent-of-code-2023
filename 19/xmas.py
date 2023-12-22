from sys import argv
import time
import re
from queue import Queue
import copy

OP = { '>' : (lambda x, y: x > y), '<': (lambda x, y: x < y), 'nop': (lambda x, y: True) }

def read_input(f):
  parsed_workflows = {}
  while workflow := f.readline().strip():
    name, rules_tmp = workflow.split('{')
    rules =  re.findall("(.)([<>])([0-9]*):([a-z, A-Z]*),", rules_tmp)
    rules += re.findall(",([a-z, A-Z]*)}", rules_tmp)

    parsed_rules = [ (var, OP[comp], int(val), next) for var, comp, val, next in rules[:-1]]
    parsed_rules.append(('x', OP['nop'], 0, rules[-1]))
    parsed_workflows[name] = parsed_rules

  # for flow in parsed_workflows.items():
  #   print(flow)

  items = [re.findall("(.)=([0-9]*)", line) for line in f]
  parsed_items = [{var : int(val) for var, val in item } for item in items]

  # for item in parsed_items:
  #   print(item)

  return parsed_workflows, parsed_items


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  workflows, items = read_input(open(argv[1]))

  accepted = []
  for item in items:
    curent_flow = 'in'
    while curent_flow != 'A' and curent_flow != 'R':
      for var, op, val, next in workflows[curent_flow]:
        if op(item[var], val):
          curent_flow = next
          break

      if curent_flow == 'A':
        accepted.append(item)

  total = 0
  for item in accepted:
    total += sum(item.values())
  print(total)
  print(round(time.time() - start_t, 3), 's')


def split_lt(range, val):
  if range[0] < val < range[1]:
    return (range[0], val-1), (val, range[1])
  if range[1] < val:
    return range, (0,0)
  return (0,0), range

def split_gt(range, val):
  if range[0] < val < range[1]:
    return (val + 1, range[1]), (range[0], val)
  if range[1] > val:
    return range, (0,0)
  return (0,0), range


OP_2 = { '>' : split_gt, '<' : split_lt, 'nop': (lambda range, y: (range, range)) }

def read_input_2(f):
  parsed_workflows = {}
  while workflow := f.readline().strip():
    name, rules_tmp = workflow.split('{')
    rules =  re.findall("(.)([<>])([0-9]*):([a-z, A-Z]*),", rules_tmp)
    rules += re.findall(",([a-z, A-Z]*)}", rules_tmp)

    parsed_rules = [ (var, OP_2[comp], int(val), next) for var, comp, val, next in rules[:-1]]
    parsed_rules.append(('x', OP_2['nop'], 0, rules[-1]))
    parsed_workflows[name] = parsed_rules

  return parsed_workflows


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  workflows = read_input_2(open(argv[1]))

  accepted = []
  ranges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}

  q = Queue()
  q.put(('in', ranges))

  while not q.empty():
    curent_flow, current_ranges = q.get()

    if curent_flow == 'A':
      accepted.append(current_ranges)
      continue
    
    if curent_flow == 'R':
      continue

    for var, op, val, next in workflows[curent_flow]:
      tr, fr = op(current_ranges[var], val)
      current_ranges[var] = fr

      if tr[1] - tr[0] > 0:
        true_path = copy.copy(current_ranges)
        true_path[var] = tr
        q.put((next, true_path))
      
      if fr[1] - fr[0] == 0:
        break
  
  total = 0
  for item in accepted:
    comb = 1
    for range in item.values():
      comb *= range[1] - range[0] + 1
    total += comb
  print(total)
         
  print(round(time.time() - start_t, 3), 's')
