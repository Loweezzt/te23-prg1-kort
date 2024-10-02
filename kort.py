from random import randint

spelare_1_namn = ("Choose a name for player 1")
spelare_2_namn = ("Choose a name for player 2")

play_game =""

player_1_score = 10
player_2_score = 10

while play_game.upper() == "":

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
    
    


