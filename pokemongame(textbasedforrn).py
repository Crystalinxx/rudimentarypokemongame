#rudimentary pokemon game.
from random import randint
Crithitchance = randint(1,16)
if Crithitchance == 16:
    move1 = randint(1,25)*1.5
    move2 = randint(26,50)*1.5
    move3 = randint(51,75)*1.5
    move4 = randint(1,89)*1.5
else:
    move1 = randint(1,25)
    move2 = randint(26,50)
    move3 = randint(51,75)
    move4 = randint(1,89)
health = 100
#dialouge options
print("You are a pokemon trainer 'Red'")
print("Greninja is your Pokemon")
print("Your opponent is Incineroar")
print("1 for move")
print("2 for move")
print("3 for move")
print("4 for move")
print("items not implemented yet")
#move selection
move = input("")
if move == "1":
    print("move1")
    print("Incineroar took "+str(move1),"dmg")
    print("Opponent health = "+str(health-move1))
    print("number was "+str(Crithitchance))
elif move == "2":
    print("move2")
    print("Incineroar took "+str(move2),"dmg")
    print("Opponent health = "+str(health-move2))
    print(Crithitchance)
elif move == "3":
    print("move3")
    print("Incineroar took "+str(move3),"dmg")
    print("Opponent health = "+str(health-move3))
    print(Crithitchance)
elif move == "4":
    print("move4")
    print("Incineroar took "+str(move4),"dmg")
    print("Opponent health = "+str(health-move4))
    print(Crithitchance)