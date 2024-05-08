# This is a virtual coin toss program. It will randomly tell users Heads or Tails.

import random

# 1 = Heads
# 0 = Tails

Heads_or_Tails = random.randint(0, 1)

if Heads_or_Tails == 0:
    print('Tails')
else:
    print('Heads')
