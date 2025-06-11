from assets.characters import *
from levels import level_1

heros = [Ranger, Knight, Mage]

# Character selection using your predefined hero list
print("Choose your character:")
for i, hero in enumerate(heros, 1):
    print(f"{i}. {hero.__name__}")

choice = int(input("Enter the number of your choice: ")) - 1
player = heros[choice]()
print(f"\nYour Choice: {player.name}")

## Stage 0
level_1.level1_stage0_room1(player, enemies=[Rat("Rat1"), Rat("Rat2")])

## Stage 1
room = int(input("Pick a room (1-2): "))

match room:
    case 1:
        level_1.level1_stage1_room1(player, enemies=[Rat("Rat1"), Ogre("Ogre1")])
    case 2:
        level_1.level1_stage1_room2(player, enemies=[Rat("Rat1"), Ogre("Ogre1")])
    case _:
        print("Invalid room number.")

## Stage 2
level_1.level1_stage2_room1(player, enemies=[Ogre("Ogre1"), Ogre("Ogre2")])

## Stage 3
room = int(input("Pick a room (1-3): "))

match room:
    case 1:
        level_1.level1_stage3_room1(player, enemies=[Rat("Rat1"), Rat("Rat2"), Rat("Rat3")])
    case 2:
        print("") ## Treasure room
    case 3:
        level_1.level1_stage3_room3(player, enemies=[Ogre("Ogre1"), Ogre("Ogre2"), Rat("Rat1")])
    case _:
        print("Invalid room number.")