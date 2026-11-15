"""
    File generico per le mie funzioni
    Potrei anche mettere quelle che ho fatto dentro ai .py ma va bene cosi per me.
    
"""

def leggi_intero(messaggio, valore_minimo, valore_massimo):
    while True:
        testo = input(messaggio).strip()
        try:
            numero = int(testo)
        except:
            print("Input non valido: inserisci un numero intero.")
            continue

        if numero >= valore_minimo and numero <= valore_massimo:
            return numero
        print(f"Il numero deve essere compreso tra {valore_minimo} e {valore_massimo}.")


def leggi_si_no(messaggio):
    while True:
        risposta = input(messaggio).strip().lower()
        if risposta == "s":
            return True
        if risposta == "n":
            return False
        print("Rispondi con 's' per sì oppure 'n' per no.")