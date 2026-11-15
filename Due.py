import random

CODICE_MINIMO = 1
CODICE_MASSIMO = 20
TENTATIVI_MASSIMI = 5
PUNTI_PRIMO_TENTATIVO = 100
PUNTI_PERSI_PER_TENTATIVO = 20  


def punteggio():
    print()
    print(".    Punteggio che puoi ottenere:                                                               ")
    print()
    print(".    100 al primo tentativo                                                                      ")
    print(".     80 al secondo tentativo                                                                    ")
    print(".     60 al terzo tentativo                                                                      ")
    print(".     40 al quarto tentativo                                                                     ")
    print(".     20 al quinto tentativo                                                                     ")
    print(".      0 alla sconfitta                                                                          ")
    print()


def stampaMenuAdv():
    print()
    print("================================================================================================")
    print("--------------------------------------LA CASSAFORTE DI FELIX------------------------------------")
    print("================================================================================================")
    punteggio()
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

stampaMenuAdv()

codice_segreto = random.randint(CODICE_MINIMO, CODICE_MASSIMO)
tentativo_corrente = 1
codice_indovinato = False
punteggio = 0  

while (tentativo_corrente <= TENTATIVI_MASSIMI) and (not codice_indovinato):
    numero_inserito = int(input(f". Tentativo {tentativo_corrente}: ").strip())

    if numero_inserito > codice_segreto:
        print(" -   Troppo alto!")
    elif numero_inserito < codice_segreto:
        print(" -   Troppo basso!")
    else:
        codice_indovinato = True
        punteggio = PUNTI_PRIMO_TENTATIVO - ((tentativo_corrente - 1) * PUNTI_PERSI_PER_TENTATIVO)

    tentativo_corrente += 1

print()
if codice_indovinato:
    haiVinto()
else:
    haiPerso()

print(f"    -   Punteggio finale: {punteggio}")
print()
