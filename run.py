from assets.characters import *
import random

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
rat1.name = 'Rat1'
rat2 = Rat()
rat2.name = 'Rat2'
enemies = [rat1, rat2]

while player.health > 0 and enemies:
    # Player Turn
    abilities = list(player.skills.keys())
    print("\n====== Player Turn ======")
    print("Available abilities:")
    for i, ability in enumerate(abilities, 1):
        print(f"{i}. {ability}")

    ability = int(input("\nChoose an ability to use: "))

    # Target selection
    print("\nChoose a target:")
    for i, enemy in enumerate(enemies, 1):
        print(f"{i}. {enemy.name}")

    target_choice = int(input("\nEnter the number of your choice: ")) - 1
    target = enemies[target_choice]

    # Use ability
    player.use_ability(ability, target)

    # Enemy defeat check
    if target.health <= 0:
        player.defeat_enemy(target)
        enemies.remove(target)  # Remove defeated enemy
        print(f"\n{target.name} has been defeated!")

    # Enemy Turn
    print("\n====== Enemy Turn ======")
    for enemy in enemies:
        if enemy.health > 0:
            enemy_ability = '1'
            enemy.use_ability(enemy_ability, player)
            print(f"{enemy.name} used {enemy_ability} on {player.name}!")

    # Player defeat check
    if player.health <= 0:
        print("\nYou have been defeated! Game Over.")
        break

    if not enemies:
        print("\nAll enemies defeated! Advance to next room...")
        break

    print("\nThe battle continues...\n")