class AI:
  valid_actions = {
    "ATTACK": "ATTACK",
    "BLOCK": "BLOCK",
    "POTION": "POTION",
    "PASS": "PASS",
  }

  def __init__(self, strategy):
    self.strategy = strategy

  def take_action(self, you, oppt, turn_number):
    action = self.strategy(you.current_health, you.potion_ct, oppt.current_health, turn_number)

    if action == AI.valid_actions["ATTACK"]:
      you.attack(oppt)
    elif action == AI.valid_actions["BLOCK"]:
      you.block()
    elif action == AI.valid_actions["POTION"]:
      you.potion()
    elif action == AI.valid_actions["PASS"]:
      you.pass_turn()
    else:
      print("INVALID ACTION")