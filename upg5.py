ålder = 18
din_ålder = input("Hur gammal är du?")
if int(din_ålder) < ålder:
    print("du är för ung för att ta körkortet.")
else: 
    print("Du får ta körkortet eftersom du är", + din_ålder)
    print("Du skrev inte en ålder")
 