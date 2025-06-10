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

level_1.level1_stage0_room1(player, enemies=[Rat("Rat1"), Rat("Rat2")])