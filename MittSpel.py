import random
def kasta_tarning():
    return random.randint(1, 6)

def spela_runda():
    print("Spelare 1, välj om resultatet blir över eller under:")
    val_1 = input("Skriv 'över' eller 'under': ").lower()
    
    tarning_1 = kasta_tarning()
    print(f"Spelare 1 kastade {tarning_1}.")
    
    if (val_1 == 'över' and tarning_1 >= 4) or (val_1 == 'under' and tarning_1 < 3):
        print("Spelare 1 gissade rätt!\n")
    else:
        print("Spelare 1 gissade fel.\n")
     
    print("Spelare 2, välj om resultatet blir över eller under:")
    val_2 = input("Skriv 'över' eller 'under': ").lower()
   
    tarning_2 = kasta_tarning()
    print(f"Spelare 2 kastade {tarning_2}.")
    
    if (val_2 == 'över' and tarning_2 >= 4) or (val_2 == 'under' and tarning_2 < 3):
        print("Spelare 2 gissade rätt!\n")
    else:
        print("Spelare 2 gissade fel.\n")
spela_runda()