## Dental Hygiene Battle sim
# By: Matthew Holdaway
# On: 29/08/19
# V0.1: 29/08/19

import random
import time

def battle(player_hp, player_rst, player_dmg, player_mana, enemy_name, enemy_hp, enemy_rst, enemy_dmg, enemy_mana):
    """The function that is called when the player is in a battle"""
    #def enemy_turn():
        #"""Simulates the enemy's turn in the battle"""
        #if yes
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
        if player_move == "1" or player_move == "attack":
            attack_dmg = random.randint(-5, 5)+ player_dmg
            attack_dmg -= (enemy_rst/100)* attack_dmg
            print("You attacked {} and dealt {} Damage!".format(enemy_name, attack_dmg))
            enemy_hp -= attack_dmg
            #enemy_turn()
        elif player_move == "2" or player_move == "heal":
            heal_move = input("""------------------------------
CHOOSE A HEAL:
    1) Heal 1
    2) Heal 2
    3) Heal 3
------------------------------
""").strip().lower()
            if heal_move == "1" or heal_move == "heal1":
                player_mana -= 5
                player_hp += 20
                print("You used Heal 1 and regenerated 20 Health!")
                #enemy_turn()
            elif heal_move == "2" or heal_move == " heal2":
                player_mana -= 10
                player_hp += 40
                print("You used Heal 2 and regenerated 40 Health!")
                #enemy_turn()
            elif heal_move == "3" or heal_move == "heal3":
                player_mana -= 15
                player_hp += 60
                print("You used Heal 3 and regenerated 60 Health!")
                #enemy_turn()
            else:
                print("Please enter 1, 2 or 3")
        elif player_move == "3" or player_move == "specialability":
            print("yes")
        elif player_move == "4" or player_move == "info":
            print("""------------------------------
Health -> How much health the unit has, when this is 0, the unit dies.

Resistance -> The percentage that damage received is reduced by, special abilities are not affected by this.

Damage -> How much damage regular attacks deal, this can vary by up to 5 damage higher or lower than the shown value.

Mana -> Special abilities use mana, if the unit does not have enough mana to use a special ability then it cannot be used. Mana does not regenerate between battles passively.
------------------------------
""")
        else:
            print("Please enter either 1, 2, 3 or 4")
            
        if enemy_hp <= 0:
            again = False
            print("You won the battle!")
            return player_hp, player_rst, player_dmg, player_mana
        



print("Welcome to the Dental Hygiene Battle Simulator")
time.sleep(1.5)
print("You are being attacked by an Evil Milkshake")
time.sleep(2)
player_hp, player_rst, player_dmg, player_mana = battle(100, 10, 25, 50, "Evil Milkshake", 50, 10, 15, 25)
print("""PLAYER STATS:
    Health: {}
    Resistance: {}
    Damage: {}
    Mana: {}
""".format(player_hp, player_rst, player_dmg, player_mana))
