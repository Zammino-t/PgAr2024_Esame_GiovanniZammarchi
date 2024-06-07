import json
from collections import deque
import sys
from kibo_pgar_lib import Menu
from classGiocatore import Giocatore
import random

def LeggiFileJson(path: str):
    with open(path, "r") as file:
        dati_json = json.load(file)
        return dati_json


def Inizializzazione(dati_json):
    menu_ruoli = Menu(
        "In quante persone volete giocare?", ["4", "5", "6", "7"], False, True
    )
    choice = menu_ruoli.choose()
    match choice:
        case 1:
                        

def main():
    dati_json = LeggiFileJson()
    sceriffo = {'sceriffo', 
        
    }
    sceriffo = Giocatore()
    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Killed by user exciting...")
        sys.exit(0)
