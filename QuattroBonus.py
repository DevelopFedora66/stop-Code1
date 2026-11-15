import random

from funzioni import leggi_intero, leggi_si_no

TENTATIVI_MASSIMI = 5
PUNTI_PRIMO_TENTATIVO = 100
PUNTI_PERSI_PER_TENTATIVO = 20

def stampaTabellaPunteggi():
    print()
    print(". ********************   Punteggio che puoi ottenere:    ********************                    ")
    print()
    print(".    100 al primo tentativo                                                                      ")
    print(".     80 al secondo tentativo                                                                    ")
    print(".     60 al terzo tentativo                                                                      ")
    print(".     40 al quarto tentativo                                                                     ")
    print(".     20 al quinto tentativo                                                                     ")
    print(".      0 alla sconfitta                                                                          ")
    print()
    print(". ***************************************************************************                    ")
    print()

def livello():
    print(" -   Scegli la difficoltà:    ")
    print()
    print(" 1) Facile    (codice da 1 a 10)     ")
    print(" 2) Normale   (codice da 1 a 20)     ")
    print(" 3) Difficile (codice da 1 a 50)     ")
    print()

def stampaMenuAdvLivello():
    print()
    print("================================================================================================")
    print("--------------------------------------LA CASSAFORTE DI FELIX------------------------------------")
    print("================================================================================================")
    stampaTabellaPunteggi()
    


def stampaMenuAdv():
    print()
    print("================================================================================================")
    print("--------------------------------------LA CASSAFORTE DI FELIX------------------------------------")
    print("================================================================================================")
    stampaTabellaPunteggi()
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
    print(" -   Il codice segreto di Felix era " + str(codice_segreto) + ".")
    print(" -   Il gatto Felix si tiene i suoi croccantini!")
    print()
    

stampaMenuAdvLivello()
    
vuole_giocare = True
lvlScelto = "NORMALE"

while vuole_giocare:
    livello()

    scelta_difficolta = leggi_intero(". La tua scelta: ", 1, 3)
    if scelta_difficolta == 1:
        codice_massimo = 10
        lvlScelto = "FACILE"
    elif scelta_difficolta == 3:
        codice_massimo = 50
        lvlScelto = "DIFFICILE"
    else:
        codice_massimo = 20
    
    print()
    print(f"Livello : {lvlScelto} ")
    print(f"\nIndovina il codice da 1 a {codice_massimo}.   ")
    print(f"Hai a disposizione {TENTATIVI_MASSIMI} tentativi.\n")

    codice_segreto = random.randint(1, codice_massimo)  # nuovo codice a ogni partita
    tentativo_corrente = 1
    codice_indovinato = False
    punteggio = 0

    while (tentativo_corrente <= TENTATIVI_MASSIMI) and (not codice_indovinato):

        numero_inserito = leggi_intero(f"Tentativo {tentativo_corrente}: ", 1, codice_massimo)

        if numero_inserito > codice_segreto:
            print(" -   Troppo alto!")
        elif numero_inserito < codice_segreto:
            print(" -   Troppo basso!")
        else:
            codice_indovinato = True
            punteggio = PUNTI_PRIMO_TENTATIVO - (tentativo_corrente - 1) * PUNTI_PERSI_PER_TENTATIVO

        tentativo_corrente += 1

    print()
    if codice_indovinato:
        haiVinto()
    else:
        haiPerso()
    
    print(f"    -   Punteggio finale: {punteggio}")
    
    vuole_giocare = leggi_si_no("\nVuoi riprovare a giocare? (s/n): ")

print("\nIl gioco è terminato.")