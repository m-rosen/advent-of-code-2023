from sys import argv
import time

def read_input(f):
  return [[int(i) for i in l.split()] for l in f]

def constant(seq):
  return len(set(seq)) == 1

def differences(seq):
  result = []
  for i in range(1, len(seq)):
    result.append(seq[i] - seq[i-1])
  return result

def build_tree(seq):
  tree = [s]; i = 0
  while not constant(tree[i]):
    tree.append(differences(tree[i]))
    i += 1
  tree.reverse()
  return tree

def predict(tree):
  tree[0].append(tree[0][0])
  for i in range(1, len(tree)):
    tree[i].append(tree[i][-1] + tree[i-1][-1])
  return(tree[-1][-1])
    

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  seqs = read_input(open(argv[1]))
  predictions = []
  for s in seqs:
    tree = build_tree(s)
    predictions.append(predict(tree))
  
  print(sum(predictions))

  print(round(time.time() - start_t, 3), 's')


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  seqs = read_input(open(argv[1]))
  predictions = []
  for s in seqs:
    seq = s.reverse()
    tree = build_tree(seq)
    predictions.append(predict(tree))
  
  print(sum(predictions))

  print(round(time.time() - start_t, 3), 's')
