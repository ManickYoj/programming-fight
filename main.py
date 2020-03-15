from alice_strategy import alice_strategy
from cici_strategy import cici_strategy
from ai import AI
from character import Character
from game import Game

if __name__ == "__main__":

  alice_ai = AI(alice_strategy)
  cici_ai = AI(cici_strategy)

  alice = Character("Alice", 15, 3, 3, alice_ai)
  cici = Character("Cici", 15, 3, 3, cici_ai)

  game = Game(alice, cici , 50)

  game.start()