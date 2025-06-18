from assets.items import healthPotionSmall, healthPotionBig, healthPotionLarge, healthOrb, manaPotionSmall, manaPotionBig, manaPotionLarge, manaOrb, Orb, Potion
#### ==== Stage 0 ==== ####

    # == Room 1 == #

def level1_stage0_room1(player, enemies):
    # Enter Room 1
    print(f"\nYou enter Room 1 and encounter two rats!\n")

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
        lp = list(player.skills.keys())
        print(f"{player.name} used {lp[ability - 1]} on {enemy.name}!")

        # Enemy defeat check
        if target.health <= 0:
            player.defeat_enemy(target)
            enemies.remove(target)  # Remove defeated enemy
            print(f"\n{target.name} has been defeated!")

        # Enemy Turn
        print("\n====== Enemy Turn ======")
        for enemy in enemies:
            if enemy.health > 0:
                enemy_ability = 0
                enemy.use_ability(enemy_ability, player)
                le = list(enemy.skills.keys())
                print(f"{enemy.name} used {le[enemy_ability]} on {player.name}!")

        # Player defeat check
        if player.health <= 0:
            print("\nYou have been defeated! Game Over.")
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")

## Stage 1
## Room 1

def level1_stage1_room1(player, enemies):
    # Enter Room 1
    print(f"\nYou enter Room 1 and encounter two rats!\n")

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
        lp = list(player.skills.keys())
        print(f"{player.name} used {lp[ability - 1]} on {enemy.name}!")

        # Enemy defeat check
        if target.health <= 0:
            player.defeat_enemy(target)
            enemies.remove(target)  # Remove defeated enemy
            print(f"\n{target.name} has been defeated!")

        # Enemy Turn
        print("\n====== Enemy Turn ======")
        for enemy in enemies:
            if enemy.health > 0:
                enemy_ability = 0
                enemy.use_ability(enemy_ability, player)
                le = list(enemy.skills.keys())
                print(f"{enemy.name} used {le[enemy_ability]} on {player.name}!")

        # Player defeat check
        if player.health <= 0:
            print("\nYou have been defeated! Game Over.")
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")

## Room 2

def level1_stage1_room2(player, enemies):
    # Enter Room 2
    print(f"\nYou enter Room 2 and encounter one rat and one ogre!\n")

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
        lp = list(player.skills.keys())
        print(f"{player.name} used {lp[ability - 1]} on {enemy.name}!")

        # Enemy defeat check
        if target.health <= 0:
            player.defeat_enemy(target)
            enemies.remove(target)  # Remove defeated enemy
            print(f"\n{target.name} has been defeated!")

        # Enemy Turn
        print("\n====== Enemy Turn ======")
        for enemy in enemies:
            if enemy.health > 0:
                enemy_ability = 0
                enemy.use_ability(enemy_ability, player)
                le = list(enemy.skills.keys())
                print(f"{enemy.name} used {le[enemy_ability]} on {player.name}!")

        # Player defeat check
        if player.health <= 0:
            print("\nYou have been defeated! Game Over.")
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")

## Stage 2
## Room 1

def level1_stage2_room1(player, enemies):
    # Enter Room 1
    print(f"\nYou enter Room 1 and encounter two ogres!\n")

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
        lp = list(player.skills.keys())
        print(f"{player.name} used {lp[ability - 1]} on {enemy.name}!")

        # Enemy defeat check
        if target.health <= 0:
            player.defeat_enemy(target)
            enemies.remove(target)  # Remove defeated enemy
            print(f"\n{target.name} has been defeated!")

        # Enemy Turn
        print("\n====== Enemy Turn ======")
        for enemy in enemies:
            if enemy.health > 0:
                enemy_ability = 0
                enemy.use_ability(enemy_ability, player)
                le = list(enemy.skills.keys())
                print(f"{enemy.name} used {le[enemy_ability]} on {player.name}!")

        # Player defeat check
        if player.health <= 0:
            print("\nYou have been defeated! Game Over.")
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")


## Stage 3
## Room 1

def level1_stage3_room1(player, enemies):
    # Enter Room 1
    print(f"\nYou enter Room 1 and encounter three rats!\n")

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
        lp = list(player.skills.keys())
        print(f"{player.name} used {lp[ability - 1]} on {enemy.name}!")

        # Enemy defeat check
        if target.health <= 0:
            player.defeat_enemy(target)
            enemies.remove(target)  # Remove defeated enemy
            print(f"\n{target.name} has been defeated!")

        # Enemy Turn
        print("\n====== Enemy Turn ======")
        for enemy in enemies:
            if enemy.health > 0:
                enemy_ability = 0
                enemy.use_ability(enemy_ability, player)
                le = list(enemy.skills.keys())
                print(f"{enemy.name} used {le[enemy_ability]} on {player.name}!")

        # Player defeat check
        if player.health <= 0:
            print("\nYou have been defeated! Game Over.")
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")

## Treasure room
def level1_stage3_room2(player):
    print(f"\nYou enter room 2 and find the treasure room!\n")
    print(f"\nSelect one item to take with you:\n")

    treasures = [
        manaPotionBig("Big Mana Potion"),
        healthPotionBig("Big Health Potion"),
        manaOrb("Mana Orb"),
        healthOrb("Health Orb")
    ]

    for i, item in enumerate(treasures, 1):
        print(f"{i}. {item.name} (+{item.val})")

    choice = input("\nEnter the number of the item you want to take: ")

    if choice.isdigit() and 1 <= int(choice) <= len(treasures):
        chosen_item = treasures[int(choice) - 1]
        player.items[chosen_item.name] = chosen_item
        chosen_item.apply_effect(player)
        print(f"\nYou picked up: {chosen_item.name} (+{chosen_item.val})")
        player.draw_health_bar()
        player.draw_mana_bar()
    else:
        print("Invalid choice. No item selected.")

## Room 3

def level1_stage3_room3(player, enemies):
    # Enter Room 3
    print(f"\nYou enter Room 3 and encounter three ogres!\n")

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
        lp = list(player.skills.keys())
        print(f"{player.name} used {lp[ability - 1]} on {enemy.name}!")

        # Enemy defeat check
        if target.health <= 0:
            player.defeat_enemy(target)
            enemies.remove(target)  # Remove defeated enemy
            print(f"\n{target.name} has been defeated!")

        # Enemy Turn
        print("\n====== Enemy Turn ======")
        for enemy in enemies:
            if enemy.health > 0:
                enemy_ability = 0
                enemy.use_ability(enemy_ability, player)
                le = list(enemy.skills.keys())
                print(f"{enemy.name} used {le[enemy_ability]} on {player.name}!")

        # Player defeat check
        if player.health <= 0:
            print("\nYou have been defeated! Game Over.")
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")


## Stage 4: Boss Room
def level1_stage4_room1(player, enemies):

    print(f"\nBoss Battle!\n")

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
        lp = list(player.skills.keys())
        print(f"{player.name} used {lp[ability - 1]} on {enemy.name}!")

        # Enemy defeat check
        if target.health <= 0:
            player.defeat_enemy(target)
            enemies.remove(target)  # Remove defeated enemy
            print(f"\n{target.name} has been defeated!")

        # Enemy Turn
        print("\n====== Enemy Turn ======")
        for enemy in enemies:
            if enemy.health > 0:
                enemy_ability = 0
                enemy.use_ability(enemy_ability, player)
                le = list(enemy.skills.keys())
                print(f"{enemy.name} used {le[enemy_ability]} on {player.name}!")

        # Player defeat check
        if player.health <= 0:
            print("\nYou have been defeated! Game Over.")
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nMoving on to level 2!\n")