import json
from collections import deque
import sys
from kibo_pgar_lib import Menu
from classPartita import Partita
import random


def ControllaRuoliEsistenti(ruolo, partita: Partita):
    if ruolo == "Rinnegato":
        for giocatore in partita._giocatori:
            if giocatore._ruolo == "Rinnegato":
                return True
    return False


def SelezionaPersonaggio(
    dati_json, partita: Partita, nome_giocatore: str, posizione: int
):
    while True:
        personaggio = random.choice(dati_json["personaggi"])
        for character in partita._giocatori:
            if character._nome == personaggio:
                break
            else:
                ruoli_senza_sceriffo = [
                    ruolo
                    for ruolo in dati_json["ruoli"]
                    if (ruolo != "Sceriffo" and "Vice")
                ]
                while True:
                    ruolo_casuale = random.choice(ruoli_senza_sceriffo)
                    rinnegato_presente = ControllaRuoliEsistenti(ruolo_casuale, partita)
                    if rinnegato_presente:
                        ruolo_casuale = "Fuorilegge"
                    nome_giocatore = Giocatore(
                        personaggio["nome"],
                        ruolo_casuale,
                        personaggio["pf"],
                        personaggio["descrizione"],
                    )
                    break
                rinnegato = ControllaRuoliEsistenti()
                if posizione == 2 and not rinnegato:
                    nome_giocatore._ruolo = "Rinnegato"

                return nome_giocatore


def LeggiFileJson(path: str):
    with open(path, "r") as file:
        dati_json = json.load(file)
        return dati_json


def Inizializzazione(dati_json, partita: Partita):
    menu_ruoli = Menu(
        "Vuoi inserire ancora un giocatore? (Ricorda che il massimo è 7)",
        ["SI", "NO"],
        False,
        True,
    )
    choice = menu_ruoli.choose()

    match choice:
        case 1:
            if len[partita._giocatori] == 7:
                print("ERROR: il numero massimo di giocatori è 7")
            else:
                nome = input("Inserisci il nome del giocatore: ")
                partita._giocatori.append(nome)
        case 2:
            return False


def main():
    partita = Partita()
    dati_json = LeggiFileJson()
    for i in range(4):
        nome = input("Inserisci il nome del giocatore: ")
        partita._giocatori.insert(0, nome)

    # inizializza sceriffo
    personaggio = random.choice(
        dati_json["personaggi"]
    )  # prende randomicamente un personaggio dalla lista personaggi
    partita._giocatori[-1] = Giocatore(
        personaggio["nome"],
        "Sceriffo",
        personaggio["pf"] + 1,
        personaggio["descrizione"],
    )
    for i in range(3):
        nome = partita._giocatori[i - 1]
        partita._giocatori[i - 1] = SelezionaPersonaggio(partita, nome, i - 1)

    while True:
        partita.GestisciTurno()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Killed by user exciting...")
        sys.exit(0)
