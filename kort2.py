from random import randint

player1_hp = 10
player2_hp = 10

while player1_hp > 0 and player2_hp > 0:



    player_1_hits = randint(1, 6)
    player_2_hits = randint(1, 6)

    print(f"<----------------Player one strikes {player_1_hits}!---------------->")
    print(f"<----------------Player two strikes {player_2_hits}!---------------->")

    if player_1_hits > player_2_hits:
        print(f"<------Playa one hits harder and deals {player_1_hits - player_2_hits} damage!------>")
        player_1_score = player_1_hits - player_2_hits
    elif player_2_hits > player_1_hits:
        print(f"<------Player two hits harder and deals {player_2_hits - player_1_hits} damage!----->")
        player_2_score = player_2_hits - player_1_hits
    else:
        print(
            f"<--No one deals damage, they both dodged the attack!-->"
        )
    
    play_game = input ("<------Do you want to strike again! Press Enter------->")

if player1_hp <= 0:
    print("Player 1 died!")
elif player2_hp <= 0:
    print("Player 2 died!")

