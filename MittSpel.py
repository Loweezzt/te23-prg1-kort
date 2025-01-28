import random
def kasta_tarning():
    return random.randint(1, 6)

def spela_runda():
    print("Player one, Choose if the dice results is over or under:")
    val_1 = input("Write your choice, over or under?: ").lower()
    
    
    tarning_1 = kasta_tarning()
    print(f"Player one threw the dice {tarning_1}.")
    
    if (val_1 == 'over' and tarning_1 >= 4) or (val_1 == 'under' and tarning_1 < 3):
        print("Player one guessed correctly!\n")
        return 1
    else:
        print("Player one guessed wrong.\n")
        return 2
     
    print("Player two, Choose if the dice results is over or under:")
    val_2 = input("Write your choice, over or under?: ").lower()
   
    tarning_2 = kasta_tarning()
    print(f"Player two threw the dice {tarning_2}.")
    
    if (val_2 == 'over' and tarning_2 >= 4) or (val_2 == 'under' and tarning_2 < 3):
        print("Player two guessed right!\n")
        return 2
    else:
        print("Player two guessed wrong!.\n")
        return 1

run = True

player_1 = 0
player_2 = 0 

while run:
    print("p1", player_1, "player_", player_2)
    if player_1 == 3:
        print("Player one wins")
        run= False
    elif player_2 == 3:
        print("player two wins")
        run = False

    winner = spela_runda()

    if winner == 1:
        player_1 += 1

    elif winner ==2:
        player_2 += 1

