"""Jimmy Clark
Turn-based combat
A program that focuses on turn-based comabt.
"""
import random
import tbc

# Hero class has low armor but better chance at doing damage. Lower hit points.


def main():
    hero = tbc.Character()
    hero.name = "Joe"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
   
# Villain class has higher hit points, but no armor. Lower chance at hitting Hero.

    villain = tbc.Character("Bill", 20, 30, 5, 0)
    
    hero.printStats()
    villain.printStats()
    
    tbc.fight(hero, villain)


randomNumber = random.randint(0,5)

print = "Joe will attack first. Bill will attack second."
    
attack= input("Type attack to attack Bill: ")

while
if action == attack:
    print("You attack Bill for (randomNumber)")
    print("Bill attacks you for (randomNumber)")
    
    hero.printStats()
    villain.printStats()
    
if villain.hitPoints < 1:
    print("You win!")
if hero.hitPoints < 1:
    print("You lose!")
