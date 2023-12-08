from sys import argv
import time

def read_input(f):
  hands = []
  for line in f:
    hand, bet = line.strip().split()
    hands.append([hand, int(bet)])
  return hands

CARD = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
        '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A' : 12}


def score(game):
  hand, bet = game
  numeric_hand = []

  count = [0 for _ in range(13)]
  for card in hand:
    count[CARD[card]] += 1
    numeric_hand.append(CARD[card])
  count.sort(reverse=True)

  if count[0] == 5: # Five of a Kind
    return [6, numeric_hand]
  if count[0] == 4: # Four of a Kind
    return [5, numeric_hand]
  if count[0] == 3: 
    if count[1] == 2: # Full House
      return [4, numeric_hand]
    return [3, numeric_hand] # Three of a Kind
  if count[0] == 2:
    if count[1] == 2: # Two Pair
      return [2, numeric_hand]
    return [1, numeric_hand] # One Pair
  return [0, numeric_hand] # High Card


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  hands = read_input(open(argv[1]))
  hands.sort(key=lambda x: score(x))

  winnings = 0
  for i, (hand, bet) in enumerate(hands):
    winnings += bet * (i + 1)

  print(winnings)
  print(round(time.time() - start_t, 3), 's')


def score_joker(game):
  hand, bet = game
  numeric_hand = []

  count = [0 for _ in range(13)]
  for card in hand:
    count[CARD[card]] += 1
    if card == 'J':
      numeric_hand.append(-1)
    numeric_hand.append(CARD[card])
  jokers = count[CARD['J']]
  count[CARD['J']] = 0
  count.sort(reverse=True)

  if count[0] + jokers == 5: # Five of a Kind
    return [6, numeric_hand]
  if count[0] + jokers == 4: # Four of a Kind
    return [5, numeric_hand]
  if count[0] + jokers == 3: 
    if count[1] + (count[0] + jokers - 3) == 2: # Full House
      return [4, numeric_hand]
    return [3, numeric_hand] # Three of a Kind
  if count[0] + jokers == 2:
    if count[1]  + (count[0] + jokers - 2) == 2: # Two Pair
      return [2, numeric_hand]
    return [1, numeric_hand] # One Pair
  return [0, numeric_hand] # High Card


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  hands = read_input(open(argv[1]))
  hands.sort(key=lambda x: score_joker(x))

  winnings = 0
  for i, (hand, bet) in enumerate(hands):
    winnings += bet * (i + 1)

  print(winnings)
  print(round(time.time() - start_t, 3), 's')
