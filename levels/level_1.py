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
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")

## Room 2

def level1_stage1_room2(player, enemies):
    # Enter Room 2
    print(f"\nYou enter Room 2 and encounter two rats!\n")

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
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")

## Stage 2
## Room 1

def level1_stage2_room1(player, enemies):
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
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")


## Stage 3
## Room 1

def level1_stage3_room1(player, enemies):
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
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")
## Room 2: Treasure Room


## Room 3

def level1_stage3_room3(player, enemies):
    # Enter Room 3
    print(f"\nYou enter Room 3 and encounter two rats!\n")

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
            exit()

        if not enemies:
            print("\nAll enemies defeated! Advance to next room...")
            break

        print("\nThe battle continues...\n")


## Stage 4: Boss Room