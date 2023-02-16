import uuid

class User:
  def __init__(self):
    self.id = uuid.uuid4()
    self.health = 100
    self.position = ['some', 'vector', 'stuff', 'probably']
    self.inventory = ['random', 'loot']
    self.position ={'x': 0, 'y': 0, 'z': 0}
    self.stamina = 100
    self.ammo = 100

  def getAll(self):
    return self

  def damage(self, d):
    self.health -= d

  def heal(self, h):
    self.health += h

  def addAmo(self, a):
    self.ammo += a

  def addStamina(self, s):
    self.stamina += s
