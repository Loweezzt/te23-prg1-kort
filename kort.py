import random
player1_hp = 25
player2_hp = 25

while player1_hp > 0 and player2_hp > 0:

    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)
    
    print(f"<-----------Player one strikes with: {player1_roll} Damage!------------>")
    print(f"<-----------Player two strikes with: {player2_roll} Damage!------------>")
    
    if player1_roll > player2_roll:
        
        damage = player1_roll - player2_roll
        player2_hp -= damage
        print(f"<-Player one deals {damage} damage. Player two has {player2_hp} health left->")
    elif player2_roll > player1_roll:
        
        damage = player2_roll - player1_roll
        player1_hp -= damage
        print(f"<-Player two deals {damage} damage. Player one has {player1_hp} health left->")
    else:
       print("<--------Neither does damage, both dodge the attacks.---------->")
if player1_hp <= 0:
    print("<--------------Player two Killed player one!-------------->")
elif player2_hp <= 0:
    print("<--------------Player one Killed player two!-------------->")

    