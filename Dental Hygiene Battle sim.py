## Dental Hygiene Battle sim
# By: Matthew Holdaway
# On: 29/08/19
# V0.1: 29/08/19
# v0.5: 02/09/19
# v0.62: 09/09/19

import random
import time

def battle(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana):
    """The function that is called when the player is in a battle"""

    def enemy_turn(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana):
        """Simulates the enemy's turn in the battle"""
        if player_hp < enemy_dmg - enemy_dmg*(player_rst/100)-5:
            enemy_attack = random.randint(-5, 5)+ enemy_dmg
            enemy_attack -= round((player_rst/100)*enemy_attack)
            player_hp -= enemy_attack
            print("{} attacked you and dealt {} damage!".format(enemy_name, enemy_attack))
        elif enemy_hp <= player_dmg*(enemy_rst/100)-5 and enemy_mana >= 5:
            enemy_mana -= 5
            enemy_hp += 20
            print("{} healed for 20 hp!".format(enemy_name))
        else:
            enemy_attack = random.randint(-5, 5)+ enemy_dmg
            enemy_attack -= round((player_rst/100)*enemy_attack)
            player_hp -= enemy_attack
            print("{} attacked you and dealt {} damage!".format(enemy_name, enemy_attack))
        return player_hp, player_mana, enemy_hp, enemy_mana
    again = True
    while again:
        player_move = input("""------------------------------
PLAYER STATS:
    Health: {}
    Resistance: {}
    Damage: {}
    Mana: {}

{} STATS:
    Health: {}
    Resistance: {}
    Damage: {}
    Mana: {}


CHOOSE AN OPTION:
    1) Attack
    2) Heal
    3) Special Ability
    4) Info
------------------------------
""".format(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana)).strip().lower()

        # Attack Move
        if player_move == "1" or player_move == "attack":
            attack_dmg = random.randint(-5, 5)+ player_dmg
            attack_dmg -= round((enemy_rst/100)* attack_dmg)
            print("You attacked {} and dealt {} damage!".format(enemy_name, attack_dmg))
            enemy_hp -= attack_dmg
            player_hp, player_mana, enemy_hp, enemy_mana = enemy_turn(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana)

        # Heal Move
        elif player_move == "2" or player_move == "heal":
            yes = True
            while yes:
                heal_move = input("""------------------------------
CHOOSE A HEAL:

    1) Brush Teeth
    2) Mouthwash
    3) Visit Dentist

    4) Info
    5) Cancel
    
------------------------------
""").strip().lower()

                # Brush Teeth move
                if heal_move == "1":
                    if player_mana >= 5:
                        player_mana -= 5
                        player_hp += 20
                        print("You used Brush Teeth and regenerated 20 Health!")
                        yes = False
                        player_hp, player_mana, enemy_hp, enemy_mana = enemy_turn(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana)
                    else:
                        print("You do not have enough mana to use this heal")

                # Mouthwash Move
                elif heal_move == "2":
                    if player_mana >= 10:
                        player_mana -= 10
                        player_hp += 40
                        print("You used Mouthwash and regenerated 40 Health!")
                        yes = False
                        player_hp, player_mana, enemy_hp, enemy_mana = enemy_turn(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana)
                    else:
                        print("You do not have enough mana to use this heal")

                # Visit Dentist Move
                elif heal_move == "3":
                    if player_mana >= 15:
                        player_mana -= 15
                        player_hp += 60
                        print("You used Visit Dentist and regenerated 60 Health!")
                        yes = False
                        player_hp, player_mana, enemy_hp, enemy_mana = enemy_turn(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana)
                    else:
                        print("You do not have enough mana to use this heal")
                        
                elif heal_move == "4":
                    print("""------------------------------
    1) Brush Teeth
       - Costs 5 mana
       - Regenerates 20 Health
       
    2) Mouthwash
       - Costs 10 mana
       - Regenerates 40 Health
       
    3) Visit Dentist
       - Costs 15 mana
       - Regenerates 60 Health
       """)
                elif heal_move == "5":
                    #player_move = 0
                    yes = False
                    
                else:
                    print("Please enter 1, 2 or 3")
        # Special Ability Move
        elif player_move == "3" or player_move == "specialability":
            special_move = input("""------------------------------
CHOOSE AN ABILITY:
    1) Floss
    2) Restock Toothpaste
    3) Reduce Sugar

    4) Info
    5) Cancel
------------------------------
""").strip().lower()

            # Floss Move
            if special_move == "1":
                if player_mana >= 15:
                    player_mana -= 15
                    enemy_hp -= 30
                    print("You used Floss and dealt 30 damage!")
                    player_hp, player_mana, enemy_hp, enemy_mana = enemy_turn(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana)
                else:
                    print("You do not have enough mana to use this ability")

            # Restock Toothpast Move
            elif special_move == "2":
                player_mana += 10
                print("You used Restock Toothpaste and regenerated 10 mana!")
                player_hp, player_mana, enemy_hp, enemy_mana = enemy_turn(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana)

            # Reduce Sugar Move
            elif special_move == "3":
                if player_mana >= 20:
                    player_mana -= 20
                    player_hp += 15
                    enemy_hp -= 15
                    print("You used Reduce Sugar, regenerated 15 health and dealt 15 damage!")
                    player_hp, player_mana, enemy_hp, enemy_mana = enemy_turn(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana)
                else:
                    print("You do not have enough mana to use this ability")

        # Info panel
        elif player_move == "4" or player_move == "info":
            print("""------------------------------
Health -> How much health the unit has, when this is 0, the unit dies.

Resistance -> The percentage that damage received is reduced by, special abilities are not affected by this.

Damage -> How much damage regular attacks deal, this can vary by up to 5 damage higher or lower than the shown value.

Mana -> Special abilities use mana, if the unit does not have enough mana to use a special ability then it cannot be used.
------------------------------
""")
        else:
            print("Please enter either 1, 2, 3 or 4")

        # Conditions to end battle
        if player_hp <= 0:
            again = False
            print("You lost the battle!")
            return player_hp, player_rst, player_dmg, player_mana
        elif enemy_hp <= 0:
            again = False
            print("You won the battle!")
            return player_hp, player_rst, player_dmg, player_mana

        

print("""  _____             _        _   _    _             _
 |  __ \           | |      | | | |  | |           (_)                        
 | |  | | ___ _ __ | |_ __ _| | | |__| |_   _  __ _ _  ___ _ __   ___         
 | |  | |/ _ \ '_ \| __/ _` | | |  __  | | | |/ _` | |/ _ \ '_ \ / _ \        
 | |__| |  __/ | | | || (_| | | | |  | | |_| | (_| | |  __/ | | |  __/        
 |_____/ \___|_| |_|\__\__,_|_| |_|__|_|\__, |\__, |_|\___|_| |_|\___|        
 |  _ \      | | | | | |       / ____(_) __/ | __/ |   | |     | |            
 | |_) | __ _| |_| |_| | ___  | (___  _ |___/_|___/   _| | __ _| |_ ___  _ __ 
 |  _ < / _` | __| __| |/ _ \  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
 | |_) | (_| | |_| |_| |  __/  ____) | | | | | | | |_| | | (_| | || (_) | |   
 |____/ \__,_|\__|\__|_|\___| |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
                                                                              
                                                                              """)
print("Welcome to the Dental Hygiene Battle Simulator")
time.sleep(1.5)
print("Look out!\nYou are being attacked by an Evil Milkshake!")
time.sleep(2)
player_hp, player_rst, player_dmg, player_mana = battle(100, 10, 20, 50, "Evil Milkshake", 50, 10, 15, 25)
print("""PLAYER STATS:
    Health: {}
    Resistance: {}
    Damage: {}
    Mana: {}
""".format(player_hp, player_rst, player_dmg, player_mana))
