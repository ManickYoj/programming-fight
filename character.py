class Character:
  def __init__ (self, name, max_health, strength, potion_ct, ai):
    self.ai = ai
    self.max_health = max_health
    self.name = name
    self.current_health = max_health
    self.alive = True
    self.heal_amt = 0

    self.block_active = False
    self.potion_ct = potion_ct
    self.strength = strength

  def attack(self, opponent):
    print(self.name + " tries to attack for " + str(self.strength) + " damage.")
    opponent.take_damage(self.strength)

  def block(self):
    print(self.name + " prepares to block.")
    self.block_active = True

  def potion(self):
    if self.potion_ct > 0:
      healed = self.change_health(5)
      print(self.name + " drinks a potion and heals " +  str(healed) + " health.")
      self.potion_ct -= 1
      print(self.name + " has " + str(self.potion_ct) + " potion(s) remaining.")
    else:
      print(self.name + " goes to drink a potion but none are left!")

  def pass_turn(self):
    print(self.name + " passes their turn.")

  def take_damage(self, damage):
    if not self.alive:
      print("You can't do anything when you are dead.")
      return

    if self.block_active:
      print (self.name + " blocks the attack!")
      return

    self.damage = damage
    self.change_health(-damage)
    print(self.name + " takes " + str(damage) + " damage and has " + str(self.current_health) + " health remaining.")

  def change_health(self, health_change):
    if not self.alive:
      print("You can't do anything when you are dead.")
      return

    if self.current_health + health_change > self.max_health:
      eff_change = self.max_health - self.current_health
      self.current_health = self.max_health
      return eff_change

    elif self.current_health + health_change <= 0:
      eff_change = -self.current_health
      self.current_health = 0
      self.alive = False
      return eff_change

    else:
      self.current_health += health_change
      return health_change