def input_int(text):
    while True:
        try:
            return int(input(text))
        except:
            print("Skriv hur många frukter du sålt?")

äpple = 7

päron = 13

antal_A = input_int("Hur många äpplen har du hunnit sälja?")
antal_P = input_int("Hur många päron har du hunnit sälja?")

äpplen_mer = äpple*antal_A 
päron_mer = päron*antal_P

if äpplen_mer > päron_mer:
    skillnad_A = päron_mer - äpplen_mer
    print(f"Antal du har tjänat från äppel försälningen är {äpplen_mer} kr")
    print(f"Antal du har tjänat från päron: {päron_mer} kr")
    print("__________________________________________________")
    print(f"Du har fått ihop {skillnad_A} kr mer än päron försjälningen")
else:
    äpplen_mer < päron_mer
    skillnad_P = päron_mer - äpplen_mer
    print(f"Antal du har tjänat från äppel försälningen är {äpplen_mer} kr")
    print(f"Antal du har tjänat från päron: {päron_mer} kr")
    print("__________________________________________________")
    print(f"Du har fått ihop {skillnad_P} kr mer än äpple försjälningen")
    