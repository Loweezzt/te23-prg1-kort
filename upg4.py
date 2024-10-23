print("WElCOME to the slums simulator")
run = True
dishes = ["Lunchly", "Mango", "Galaxy gas", "Straight shit"]
drinks = ["Prime", "Still Water", "Mangojuice", "Still those who know"]
while run:
    choice = input("Whats happenin next?\n[1] List of food\n[2] List of drinks\n[3] You just found\n[4] Fanum Tax\n[5] Sort\n[6] End\n")
    if choice == "1":
        print("Dishes avalible: ")
        print("#-----------------------")
        for dish in dishes:
            print(dish)
    elif choice == "2":
        print("Drinks avalible: ")
        print("#-----------------------")
        for drink in drinks:
            print(drink)
        print("#-----------------------")
    elif choice == "2":
        dish = input("You found a old dish on the floor: ")
        dishes.append(dish)
    elif choice == "3":
        drinks = input("You found an new drink on the floor: ")
        drinks.append(drink)
    elif choice == "4":
        n = dishes.pop(0)
        print("You just fanum taxed")
        
    elif choice == "5":
        dishes.sort()
    elif choice == "6":
        run = False
    else:
        print("Jag fattar inte ditt kommando")
