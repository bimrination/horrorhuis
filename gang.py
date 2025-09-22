import states

def begin():
    print("Je staat in de GANG met een TRAP.")
    print("Kies je voor de TRAP of g je TERUG?")
    antwoord = input("> ")
    if antwoord == "TRAP"
        states.locatie = "ZOLDER"
    elif antwoord == "TERUG" :
        states.locatie = "HUIS"