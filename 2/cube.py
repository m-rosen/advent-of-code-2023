from sys import argv
import time

COLORS = ["red", "green", "blue"]

def read_input(f):
  games = []
  for l in f:
    game_raw = l.replace(',', '').split(':')[1].split(';')
    game = []
    for d in game_raw:
      tokens = d.split()
      draw = [0, 0, 0]
      for i in range(1, len(tokens), 2):
        if tokens[i] == "red":
          draw[0] = int(tokens[i-1])
        elif tokens[i] == "green":
          draw[1] = int(tokens[i-1])
        elif tokens[i] == "blue":
          draw[2] = int(tokens[i-1])
      game.append(draw)
    games.append(game)
  return games


def color_max(game):
  res = [0, 0, 0]
  for draw in game:
    for i in range(0,3):
      if draw[i] > res[i]:
        res[i] = draw[i]
  return res


def possible(a,b):
  return a[0] <= b[0] and a[1] <= b[1] and a[2] <= b[2]


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  games = read_input(open(argv[1]))
  cubes = [12, 13, 14]
  sum_id = 0
  for i, game in enumerate(games):
    res = color_max(game)
    if possible(res, cubes):
      sum_id += i+1
  print(sum_id)
  print(round(time.time() - start_t, 3), 's')


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  games = read_input(open(argv[1]))
  power_sum = 0
  for game in games:
    res = color_max(game)
    power = res[0] * res[1] * res[2]
    power_sum += power
  print(power_sum)
  print(round(time.time() - start_t, 3), 's')
