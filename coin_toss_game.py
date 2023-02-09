import numpy as np
np.random.seed(42)

def toss():
    return np.random.randint(0, 2, 2)

def play_game(max_earnings=4):
  earnings = 0
  first_strike = False
  strike_type = None
  while True:
    res = toss()
    if res[0] == res[1]:
      if not first_strike:
        first_strike = True
        strike_type = res[0]
      elif res[0] != strike_type:
        return 0
    earnings += 1
    if earnings >= max_earnings and first_strike:
      return earnings

def simulate(num_games=1000, max_earnings=4):
  earnings = []
  for _ in range(num_games):
    earnings.append(play_game(max_earnings))
  print('Average earnings if stopping at {}: {}'.format(max_earnings, np.mean(earnings)))

if __name__ == '__main__':
  for i in range(1, 6):
    simulate(100000, i)

