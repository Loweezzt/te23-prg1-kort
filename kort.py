from random import randint

spelare_1_namn = ("Choose a name for player 1")
spelare_2_namn = ("Choose a name for player 2")

player_1_score = 10
player_2_score = 10

while true:
    game_round = 0 

player_1_throw = randint(1, 6)
player_2_throw = randint(1, 6)

if player_1_throw > player_2_throw:
    damage = player_2_throw - player_1_throw

player_2_score =- damage

    print(f"{spelare_1_namn} rolls {player_1_throw} !")
    print(f"{spelare_2_namn} rolls {player_2_throw} !")

    print(f"{spelare_1_namn} Does {damage} Damage!")
    print(f"{spelare_2_namn} Only has {player_2_score} Lifes left!")
    throw_again = input("Click enter to throw again!")

    elif player_2_throw > player_1_throw :
        Damage = player_2_throw - player_1_throw


    player_1_score -= Damage
    print("#|||||||||||||||||||||||||||#")
    print(f"{spelare_1_namn} rolls {player_1_throw}")
    print(f"{spelare_2_namn} rolls {player_2_throw}")
    print("#|||||||||||||||||||||||||||#")

    print(f"{}")




