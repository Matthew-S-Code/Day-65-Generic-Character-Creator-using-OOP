import os, time

class character:
  name = None
  health = None 
  magicPoints = None

  def __init__(self, name, health, magicPoints):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
  
class player(character):
  lives = None
  alive = True

  def __init__(self, name, health, magicPoints, lives, alive):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.lives = lives 
    self.alive = alive
  
  def print(self):
    print("Player")
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nLives: {self.lives}\nAlive: {self.alive}")
    

nameP = input("Name: ").strip()
healthP = int(input("Health: "))
magicPointsP = int(input("Magic Points: "))
lives = int(input("Amount of lives: "))
alive = "Yes" if lives > 0 else "No"
print()

playerC = player(nameP, healthP, magicPointsP, lives, alive)
playerC.print()
time.sleep(1)
print()
class enemy(character):
  type = None
  strength = None

  def __init__(self, name, health, magicPoints, type, strength):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength

class orc(enemy):
  speed = None

  def __init__(self, name, health, magicPoints, type, strength, speed):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength
    self.speed = speed

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}")
    
orc1 = orc("Christopher", 70, 10, "Orc", 80, 90)
orc2 = orc("Edmund", 60, 15, "Orc", 83, 87)
orc3 = orc("Wilmur", 70, 25, "Orc", 73, 77)
orc1.print()
print()
orc2.print()
print()
orc3.print()
print()
time.sleep(2)

class vampire(enemy):
  day = None
  
  def __init__(self, name, health, magicPoints, type, strength, day):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength
    self.day = day

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.day}")

vamp1 = vampire("David", 47, 60, "Vampire", 80, "Night")
vamp2 = vampire("Gary", 50, 58, "Vampire", 83, "Day")

vamp1.print()
print()
vamp2.print()
