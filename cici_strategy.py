import random

from ai import AI

def cici_strategy(your_health, your_potion_ct, oppt_health, turn_number):
  actions = [
    AI.valid_actions["ATTACK"],
    AI.valid_actions["BLOCK"],
    AI.valid_actions["POTION"],
    AI.valid_actions["PASS"],
  ]

  return random.choice(actions)