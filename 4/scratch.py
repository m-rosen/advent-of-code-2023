from sys import argv
import time

def read_input(f):
  cards = []
  for line in f:
    winners, yours = line.strip().split(':')[1].split('|')
    winners = set(winners.split())
    yours = set(yours.split())
    cards.append([winners, yours])
  return cards


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()

  cards = read_input(open(argv[1]))

  total = 0
  for win, you in cards:
    wins = len(you.intersection(win))
    if wins:
      total += pow(2, wins - 1)
  print(total)

  print(round(time.time() - start_t, 3), 's')


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  
  cards = read_input(open(argv[1]))

  copies = [1 for i in cards]
  for i, [win, you] in enumerate(cards):
    wins = len(you.intersection(win))
    for j in range(1, wins + 1):
      copies[i+j] += copies[i]
  print(sum(copies))

  print(round(time.time() - start_t, 3), 's')
