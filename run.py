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
rat1 = Rat()
rat2 = Rat()
enemies = [rat1, rat2]

while player.health > 0:

    abilities = list(player.skills.keys())
    print('Available abilities:')
    for i, abilities in enumerate(abilities, 1):
        print(f"{i}. {abilities}")
    ability = input("Choose an ability to use: \n")

    # Target selection
    print("Choose a target:")
    for i, enemy in enumerate(enemies, 1):
        print(f"{i}. {enemy.name}{i}")

    target_choice = int(input("\nEnter the number of your choice: ")) - 1
    target = enemies[target_choice]

    # Use ability
    player.use_ability(ability, target)

    # Gain experience if target is defeated
    if target.health <= 0:
        player.defeat_enemy(target)
        enemies.remove(target) # Remove enemy from list of enemies alive

    print("\nThe battle continues...\n")