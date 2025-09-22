import states


def begin() :
    print("Je staat in een TUIN voor een huis met een DEUR")
    print("Kies je voor de TUIN of de DEUR binnen te gaan")
    antwoord = input("> ")
    if antwoord == "TUIN":
        states.locatie = "TUIN"
    elif antwoord == "DEUR" :
        states.locatie = "GANG"