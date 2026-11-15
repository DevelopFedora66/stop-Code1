import random


def stampaMenu():
    print()
    print("================================================================================================")
    print("--------------------------------------LA CASSAFORTE DI FELIX------------------------------------")
    print("================================================================================================")
    print(" -   Felix ha nascosto i croccantini!    ")
    print(" -   Indovina il codice da 1 a 20.   ")
    print(" -   Hai a disposizione 5 tentativi. ")
    print()

def haiVinto():
    print("         COMPLIMENTI! HAI VINTO!         ")
    print(" -   Hai aperto la cassaforte!")
    print(" -   Felix ti regala i suoi croccantini!")
    print()

def haiPerso():
    print("         MI DISPIACE.... HAI PERSO PURTROPPO!         ")
    print(" -   I tentativi sono finiti.")
    print(" -   Il codice segreto di Felix era " + str(codice) + ".")
    print(" -   Il gatto Felix si tiene i suoi croccantini!")
    print()
    



stampaMenu()

codice = random.randint(1, 20)
tentativi_max = 5
tentativo = 1
vinto = False

while (tentativo <= tentativi_max) and (not vinto):
    risposta = input(". Tentativo " + str(tentativo) + ": ").strip()
    numero = int(risposta)

    if numero > codice:
        print(" -   Troppo alto!")
    elif numero < codice:
        print(" -   Troppo basso!")
    else:
        vinto = True

    tentativo = tentativo + 1

print()
if vinto:
    haiVinto()
else:
    haiPerso()

