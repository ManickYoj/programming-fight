import random

class Game:
  def __init__(self, char1, char2, max_turns):

    self.char1 = char1
    self.char2 = char2

    self.max_turns = max_turns

  def start(self):
    char_list = [self.char1, self.char2]
    random.shuffle(char_list)

    char1 = char_list[0]
    char2 = char_list[1]

    print("--- Game Started! ---")
    print(char1.name + " has been randomly selected to go first.")
    turn_counter = 1

    while True:
      print("--- Turn " + str(turn_counter) + " --- ")
      print(char1.name + " health " + str(char1.current_health) + ", " + char2.name + " health " +  str(char2.current_health) + ".")
      has_winner = self.update(turn_counter)
      turn_counter += 1
      if has_winner:
        print("--- Game won. Game Over ---")
        break

      if turn_counter > self.max_turns:
        print("--- Maximum turns exceeded. Game Over ---")
        break

  def update(self, turn_number):
    char1 = self.char1
    char2 = self.char2

    char1.ai.take_action(char1, char2, turn_number)
    char2.block_active = False
    if not char2.alive:
      print(char2.name + " is DED! " + char1.name + " wins!")
      return True

    char2.ai.take_action(char2, char1, turn_number)
    char1.block_active = False
    if not char1.alive:
      print(char1.name + " is DED! " + char2.name + " wins!")
      return True

    return False