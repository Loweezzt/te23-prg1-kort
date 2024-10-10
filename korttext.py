import random

# Spelarens startliv
player1_hp = 10
player2_hp = 10

while player1_hp > 0 and player2_hp > 0:
    # Slår tärningen för båda spelarna (1 till 6)
    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)
    
    print(f"Player 1 slår: {player1_roll}")
    print(f"Player 2 slår: {player2_roll}")
    
    if player1_roll > player2_roll:
        # Player 1 vinner rundan, Player 2 tar skada
        damage = player1_roll - player2_roll
        player2_hp -= damage
        print(f"Player 1 vinner och gör {damage} i skada. Player 2 har {player2_hp} liv kvar.")
    elif player2_roll > player1_roll:
        # Player 2 vinner rundan, Player 1 tar skada
        damage = player2_roll - player1_roll
        player1_hp -= damage
        print(f"Player 2 vinner och gör {damage} i skada. Player 1 har {player1_hp} liv kvar.")
    else:
        # Oavgjort, ingen tar skada
        print("Oavgjort! Ingen tar skada.")

    print("-" * 20)  # För att separera rundor

# Slutresultat
if player1_hp <= 0:
    print("Player 2 vinner!")
elif player2_hp <= 0:
    print("Player 1 vinner!")
