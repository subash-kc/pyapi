#!/usr/bin/python3


"""Author: Subash KC
Date: 2020-09-28"""

hero =  {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}


answer= " "

while answer != "q":
  try:
    char_name= input("Which character do you want to know about? (Flash, Batman, Superman) ").lower()
    char_stat= input("What statistic do you want to know about? (strength, speed, or intelligence) ").lower()

    print(f"{char_name.capitalize()}'s {char_stat} is: {hero[char_name][char_stat].capitalize()}")
  except:
    print("You provided incorrect input.")

  answer= input("Press ENTER to choose another hero, or press Q to quit!").lower()




