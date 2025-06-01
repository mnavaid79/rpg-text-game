from assets.characters import *

heros = [Ranger, Knight, Mage]


# Character selection using your predefined hero list
print("Choose your character:")
for i, hero in enumerate(heros, 1):
    print(f"{i}. {hero.__name__}")

choice = int(input("Enter the number of your choice: ")) - 1
player = heros[choice]()
print(f"\nYour Choice: {player.name}")

# Enter Room 1
print(f"\nYou enter Room 1 and encounter two rats!\n")

# Encounter with rats
r1 = r2 = Rat()
rats = [r1, r2]
abilities = list(player.skills.keys())
print('Available abilities:')
for i, abilities in enumerate(abilities, 1):
    print(f"{i}. {abilities}")
ability = input("Choose an ability to use: \n")

# Target selection
print("Choose a target:")
for i, rat in enumerate(rats, 1):
    print(f"{i}. {rat.name}{i}")

target_choice = int(input("\nEnter the number of your choice: ")) - 1
target = rats[target_choice]

# Use ability
player.use_ability(ability, target)

print("\nThe battle continues...")