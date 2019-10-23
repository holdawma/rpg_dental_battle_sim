## Dental Hygiene Battle sim
# By: Matthew Holdaway
# On: 29/08/19
# V0.10: 29/08/19
# v0.50: 02/09/19
# v0.62: 09/09/19
# v0.65: 10/09/19
# v0.66: 23/09/19
# v0.67: 15/10/19
# v0.70: 19/10/19
# v0.80: 20/10/19
# v0.81: 21/10/19
# v0.82: 22/10/19
# v1.00: 22/10/19

import random
import time
import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

def battle(player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mp):
    """The function that is called when the player is in a battle"""

    def enemy_turn(player_hp, player_rst, player_dmg, player_mp, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mp):
        """Simulates the enemy's turn in the battle"""
        if player_hp < enemy_dmg - enemy_dmg*(player_rst/100)-5:
            enemy_attack = random.randint(-5, 5)+ enemy_dmg
            enemy_attack -= round((player_rst/100)*enemy_attack)
            player_hp -= enemy_attack
            print("{} attacked you and dealt {} damage!".format(enemy_name, enemy_attack))
        elif enemy_hp <= player_dmg*(enemy_rst/100)-5 and enemy_mp > 4:
            enemy_mp -= 5
            enemy_hp += 20
            print("{} healed for 20 hp!".format(enemy_name))
        else:
            enemy_attack = random.randint(-5, 5)+ enemy_dmg
            enemy_attack -= round((player_rst/100)*enemy_attack)
            player_hp -= enemy_attack
            print("{} attacked you and dealt {} damage!".format(enemy_name, enemy_attack))
        input("Enter to continue")
        return player_hp, player_mp, enemy_hp, enemy_mp

    enemy_max_hp = enemy_hp
    enemy_max_mp = enemy_mp
    again = True
    while again:
        player_move = input("""------------------------------
PLAYER STATS:
    Health: {player_hp}/{player_max_hp}
    Resistance: {player_rst}
    Damage: {player_dmg}
    Mana: {player_mp}/{player_max_mp}

{enemy_name} STATS:
    Health: {enemy_hp}/{enemy_max_hp}
    Resistance: {enemy_rst}
    Damage: {enemy_dmg}
    Mana: {enemy_mp}/{enemy_max_mp}


CHOOSE AN OPTION:
    1) Attack
    2) Heal
    3) Special Ability
    4) Info
------------------------------
""".format(player_hp = player_hp, player_max_hp = player_max_hp, player_rst = player_rst, player_dmg = player_dmg,
           player_mp = player_mp, player_max_mp = player_max_mp, enemy_name = enemy_name, enemy_hp = enemy_hp, enemy_max_hp = enemy_max_hp,
           enemy_rst = enemy_rst, enemy_dmg = enemy_dmg, enemy_mp = enemy_mp, enemy_max_mp = enemy_max_mp)).strip().lower()

#--------------------------------------------------------------------------------------Attack Move-------------------------------------------------------------------------------------------
        if player_move == "1" or player_move == "attack":
            attack_dmg = random.randint(-5, 5)+ player_dmg
            attack_dmg -= round((enemy_rst/100)* attack_dmg)
            print("You attacked {} and dealt {} damage!".format(enemy_name, attack_dmg))
            enemy_hp -= attack_dmg
            player_hp, player_mp, enemy_hp, enemy_mp = enemy_turn(player_hp, player_rst, player_dmg, player_mp, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mp)

#---------------------------------------------------------------------------------------Heal Move--------------------------------------------------------------------------------------------
        elif player_move == "2" or player_move == "heal":
            heal_again = True
            while heal_again:
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
                    if player_mp >= 5:
                        player_mp -= 5
                        player_hp += 20
                        if player_hp >= player_max_hp:
                            player_hp = player_max_hp
                        print("You used Brush Teeth and regenerated 20 Health!\nYou now have {} Health!".format(player_hp))
                        heal_again = False
                        player_hp, player_mp, enemy_hp, enemy_mp = enemy_turn(player_hp, player_rst, player_dmg, player_mp, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mp)
                    else:
                        print("You do not have enough mana to use this heal")

                # Mouthwash Move
                elif heal_move == "2":
                    if player_mp >= 10:
                        player_mp -= 10
                        player_hp += 40
                        if player_hp >= player_max_hp:
                            player_hp = player_max_hp
                        print("You used Mouthwash and regenerated 40 Health!\nYou now have {} Health!".format(player_hp))
                        heal_again = False
                        player_hp, player_mp, enemy_hp, enemy_mp = enemy_turn(player_hp, player_rst, player_dmg, player_mp, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mp)
                    else:
                        print("You do not have enough mana to use this heal")

                # Visit Dentist Move
                elif heal_move == "3":
                    if player_mp >= 15:
                        player_mp -= 15
                        player_hp += 60
                        if player_hp >= player_max_hp:
                            player_hp = player_max_hp
                        print("You used Visit Dentist and regenerated 60 Health!\nYou now have {} Health!".format(player_hp))
                        heal_again = False
                        player_hp, player_mp, enemy_hp, enemy_mp = enemy_turn(player_hp, player_rst, player_dmg, player_mp, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mp)
                    else:
                        print("You do not have enough mana to use this heal")

                # Healing Info Panel
                elif heal_move == "4":
                    print("""------------------------------
    1) Brush Teeth
       - Costs 5 Mana
       - Regenerates 20 Health
       
    2) Mouthwash
       - Costs 10 Mana
       - Regenerates 40 Health
       
    3) Visit Dentist
       - Costs 15 Mana
       - Regenerates 60 Health
    NOTE: Healing is significantly less effective when above max hp
""")
                # Cancel Option
                elif heal_move == "5":
                    heal_again = False

                # Input error detection
                else:
                    print("Please enter 1, 2, 3, 4 or 5")

#---------------------------------------------------------------------------------Special Ability Move---------------------------------------------------------------------------------------

        elif player_move == "3" or player_move == "specialability":
            spec_again = True
            while spec_again:
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
                    if player_mp >= 10:
                        player_mp -= 10
                        enemy_hp -= 30
                        print("You used Floss and dealt 30 damage!")
                        player_hp, player_mp, enemy_hp, enemy_mp = enemy_turn(player_hp, player_rst, player_dmg, player_mp, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mp)
                        spec_again = False
                    else:
                        print("You do not have enough mana to use this ability")

                # Restock Toothpaste Move
                elif special_move == "2":
                    player_mp += 15
                    if player_mp >= player_max_mp:
                        player_mp = player_max_mp
                    print("You used Restock Toothpaste and regenerated 10 mana!\nYou now have {} mana".format(player_mp))
                    player_hp, player_mp, enemy_hp, enemy_mp = enemy_turn(player_hp, player_rst, player_dmg, player_mp, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mp)
                    spec_again = False

                # Reduce Sugar Move
                elif special_move == "3":
                    if player_mp >= 15:
                        player_mp -= 15
                        player_hp += 20
                        enemy_hp -= 20
                        print("You used Reduce Sugar, regenerated 20 health and dealt 20 damage!")
                        player_hp, player_mp, enemy_hp, enemy_mp = enemy_turn(player_hp, player_rst, player_dmg, player_mp, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mp)
                        spec_again = False
                    else:
                        print("You do not have enough mana to use this ability")

                # Special Ability Info Panel
                elif special_move == "4":
                    print("""------------------------------

    1) Floss
        - Costs 10 Mana
        - Deals 30 Damage

    2) Restock Toothpaste
        - Regenerates 15 Mana

    3) Reduce Sugar
        - Costs 15 Mana
        - Deals 20 Damage
        - Regenerates 20 Health
""")
                elif special_move == "5":
                    spec_again = False
                    
                # Input error detection
                else:
                    print("Please enter 1, 2, 3, 4 or 5")

#------------------------------------------------------------------------------------------Info panel----------------------------------------------------------------------------------------
        elif player_move == "4" or player_move == "info":
            print("""------------------------------
Health -> How much health the unit has, when this is 0, the unit dies.

Resistance -> The percentage that damage received is reduced by, special abilities are not affected by this.

Damage -> How much damage regular attacks deal, this can vary by up to 5 damage higher or lower than the shown value.

Mana -> Special abilities and heals use mana, if the unit does not have enough mana to use an ability then it cannot be used.
------------------------------
""")
        else:
            print("Please enter either 1, 2, 3 or 4")

        # Conditions to end battle
        if player_hp <= 0:
            again = False
            print("You lost the battle!")
            for i in range(25):
                print("\n")
            print("Try again!")
            for i in range(12):
                print("\n")
            time.sleep(2)
            for i in range(25):
                print("\n")
            main()
        
        elif enemy_hp <= 0:
            again = False
            print("You won the battle!")
            return player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp

#----------------------------------------------------------------------------------------Items-----------------------------------------------------------------------------------------------

def items(player_max_hp, player_rst, player_dmg, player_max_mp):
    """A function to let the user choose items to upgrade their character"""
    
    # Dictionary with all items in it
    all_items = {1 : ("Toothbrush of the Strong", 20, 5, -5, 0), 2 : ("Sharp Fillings", 0, 0, 10, -10),
                 3 : ("Hardened Braces", 15, 0, 0, -10), 4 : ("Arcane Floss", 0, -5, 0, 15),
                 5 : ("Mouthwash of Resistance", -20, 15, 0, 0), 6 : ("Ethereal Floss", 0, 15, -5, -10),
                 7 : ("Soul Fillings", -15, 0, 10, 0), 8 : ("Braces of Power", -10, 0, 0, 20),
                 9 : ("Toothbrush of the Magi", 0, -5, -5, 25), 10 : ("Rite of the Orthodontist", 20, 10, 15, player_max_mp*-1)}
    selected_items = []
    final_items = []
    
    # While loop to choose which items to display to the player
    again = True
    while again:
        i = random.randint(1, 10)
        # If statement to make sure the same item isn't displayed multiple times
        if i not in selected_items:
            selected_items.append(i)
            if len(selected_items) == 3:
                again = False
                
    # Print statement for items
    item_printing = """------------------------------
Choose one of the items displayed below:

    1) {item1}
        Max Health :{currenthp} -> {i1hp}
        Resistance :{currentrst} -> {i1rst}
        Damage     :{currentdmg} -> {i1dmg}
        Max Mana   :{currentmp} -> {i1mp}
        
    2) {item2}
    
        Max Health :{currenthp} -> {i2hp}
        Resistance :{currentrst} -> {i2rst}
        Damage     :{currentdmg} -> {i2dmg}
        Max Mana   :{currentmp} -> {i2mp}

    3) {item3}
    
        Max Health :{currenthp} -> {i3hp}
        Resistance :{currentrst} -> {i3rst}
        Damage     :{currentdmg} -> {i3dmg}
        Max Mana   :{currentmp} -> {i3mp}
------------------------------""".format(item1 = all_items[selected_items[0]][0], item2 = all_items[selected_items[1]][0], item3 = all_items[selected_items[2]][0],
                                         i1hp = player_max_hp + all_items[selected_items[0]][1], i1rst = player_rst + all_items[selected_items[0]][2],
                                         i1dmg = player_dmg + all_items[selected_items[0]][3], i1mp = player_max_mp + all_items[selected_items[0]][4],
                                         i2hp = player_max_hp + all_items[selected_items[1]][1], i2rst = player_rst + all_items[selected_items[1]][2],
                                         i2dmg = player_dmg + all_items[selected_items[1]][3], i2mp = player_max_mp + all_items[selected_items[1]][4],
                                         i3hp = player_max_hp + all_items[selected_items[2]][1], i3rst = player_rst + all_items[selected_items[2]][2],
                                         i3dmg = player_dmg + all_items[selected_items[2]][3], i3mp = player_max_mp + all_items[selected_items[2]][4],
                                         currenthp = player_max_hp, currentrst = player_rst, currentdmg =  player_dmg, currentmp =  player_max_mp)

    # Item selection
    again = True
    while again:
        print(item_printing)
        item_choice = input()
        if item_choice == "1":
            player_max_hp += all_items[selected_items[0]][1]
            player_rst += all_items[selected_items[0]][2]
            player_dmg += all_items[selected_items[0]][3] 
            player_max_mp += all_items[selected_items[0]][4]
            again = False
        elif item_choice == "2":
            player_max_hp += all_items[selected_items[1]][1]
            player_rst += all_items[selected_items[1]][2]
            player_dmg += all_items[selected_items[1]][3]
            player_max_mp += all_items[selected_items[1]][4]
            again = False
        elif item_choice == "3":
            player_max_hp += all_items[selected_items[2]][1]
            player_rst += all_items[selected_items[2]][2]
            player_dmg += all_items[selected_items[2]][3]
            player_max_mp += all_items[selected_items[2]][4]
            again = False
        else:
            print("Please enter either 1, 2, or 3")

    # To make sure that the player's mana is not in the negatives
    if player_max_mp < 0:
        player_max_mp = 0
        
    print("""PLAYER STATS:
        Max Health: {}
        Resistance: {}
        Damage: {}
        Max Mana: {}
    """.format(player_max_hp, player_rst, player_dmg, player_max_mp))
    return player_max_hp, player_rst, player_dmg, player_max_mp


#----------------------------------------------------------------------------------------Main------------------------------------------------------------------------------------------------

def main():
    """Main"""
    player_max_hp = 100
    player_hp = 100
    player_rst = 20
    player_dmg = 20
    player_max_mp = 50
    player_mp = 50
    
    print(""" _____             _        _   _    _             _
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

    # First Battle
    print("Welcome to the Dental Hygiene Battle Simulator")
    time.sleep(1.5)
    print("You are defending Dental Hygiene from evil foods!")
    time.sleep(1.5)
    print("Look out!\nYou are being attacked by an Evil Milkshake!")
    time.sleep(1.5)
    player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp = battle(player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp, "Evil Milkshake", 50, 15, 15, 25)
    
    player_max_hp, player_rst, player_dmg, player_max_mp = items(player_max_hp, player_rst, player_dmg, player_max_mp)
    player_hp = player_max_hp
    player_mp = player_max_mp

    # Second Battle
    print("I hope you're ready for another battle")
    time.sleep(1)
    print("Because there is no time to rest when fighting for dental hygiene!")
    time.sleep(1.5)
    print("You are being attacked by a Corrupt Soda!")
    time.sleep(1)
    player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp = battle(player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp, "Corrupt Soda", 50, 40, 20, 40)

    player_max_hp, player_rst, player_dmg, player_max_mp = items(player_max_hp, player_rst, player_dmg, player_max_mp)
    player_hp = player_max_hp
    player_mp = player_max_mp

    # Third Battle
    print("You better have found that easy!")
    time.sleep(1)
    print("Because the job is not done yet! There are still many threats to Dental Hygiene for you to defeat!")
    time.sleep(1.5)
    print("Here comes a Rotten Snack Bar!")
    time.sleep(1)
    player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp = battle(player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp, "Rotten Snack Bar", 100, 20, 30, 50)
    
    player_max_hp, player_rst, player_dmg, player_max_mp = items(player_max_hp, player_rst, player_dmg, player_max_mp)
    player_hp = player_max_hp
    player_mp = player_max_mp

    # Fourth Battle
    print("You truly are the best Dental Health defender we have ever seen")
    time.sleep(1.5)
    print("But the enemies are only going to get tougher!")
    time.sleep(2)
    print("You are under attack by a Wicked Bag of Crisps!")
    time.sleep(1.5)
    player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp = battle(player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp, "Wicked Bag of Crisps", 200, 0, 25, 20)

    player_max_hp, player_rst, player_dmg, player_max_mp = items(player_max_hp, player_rst, player_dmg, player_max_mp)
    player_hp = player_max_hp
    player_mp = player_max_mp

    # Final Boss
    print("You may have found that easy")
    time.sleep(1)
    print("But the biggest challenge is yet to come")
    time.sleep(1)
    print("You must now go and face the final boss")
    time.sleep(1)
    print("You are being attacked by Deadly Sweets!")
    time.sleep(1)
    player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp = battle(player_max_hp, player_hp, player_rst, player_dmg, player_max_mp, player_mp, "Deadly Sweets", 200, 35, 30, 40)

    print("You successfully defended Dental Hygiene from all the evil foods!")
    print("Congratulations!")

main()
