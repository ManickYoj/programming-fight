import random

from ai import AI

def cici_strategy(your_health, your_potion_ct, oppt_health, turn_number):
  actions = [
    AI.valid_actions["ATTACK"],
    AI.valid_actions["BLOCK"],
    AI.valid_actions["POTION"],
    AI.valid_actions["PASS"],
  ]

  if your_health <= 10 and your_potion_ct > 0:
  	return "POTION"

  if your_health >= oppt_health + 3:
  	return "ATTACK"

  if turn_number%4 == 0:
  	return "ATTACK"

  return "BLOCK"