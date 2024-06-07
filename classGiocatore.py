from kibo_pgar_lib import Menu
from classMazzo import Carta, Arma
from classPartita import Partita
from math import abs

class Giocatore:
    def __init__(self, nome: str, ruolo: str, pf: int, descrizione: str, mano: list):
        self._nome = nome
        self._ruolo = ruolo
        self._descrizione = descrizione
        self._pf = pf
        self._mano: list[Carta] = []
        self._equipaggiamenti = []

    def PescaCarte(self, mazzo, numero_carte):
        carte_pescate = []
        for i in range(numero_carte):
            if mazzo:
                carte_pescate.append(mazzo.pop(0))
            else:
                # Devo rigenerare il mazzo
                carte_pescate.append(mazzo.pop(0))
        return carte_pescate

    def ControllaCartaEquipaggiamento(self):
        lista_carte_equipaggiamento = []
        for carta in self._mano:
            if isinstance(carta, Arma):
                lista_carte_equipaggiamento.append(carta)
        if not lista_carte_equipaggiamento:
            print("Non hai nessuna carta BANG! in mano")
            return False
        else:
            return lista_carte_equipaggiamento

    def ScegliCartaEquipaggiamento(self, carte_arma):
        scegli_arma = Menu(
            "Quale arma vuoi equipaggiare: ",
            [arma.nome for arma in carte_arma],
            False,
            True,
        )
        scelta = scegli_arma.choose()
        carte_arma[scelta - 1]

    def ControllaCartaBang(self):
        quante_carte_bang = 0
        for carta in self._mano:
            if carta._nome == "BANG!":
                quante_carte_equi += 1
        return quante_carte_bang
    
    def PossoSparare(self, bersaglio, partita: Partita):
        for giocatore in partita._giocatori:
            if giocatore._nome == self._nome:
                mia_posizione = partita._giocatori.index(giocatore)
        quanto_dista = abs(mia_posizione - bersaglio)
        if self._equipaggiamenti[0]._distanza > quanto_dista:
            print("Non puoi sparare, il bersaglio è troppo lontano")
        else:
            
            
        

    def MenuGiocaCarta(self):
        menu_dinamico = Menu(
            "Seleziona la prossima mossa: ",
            [
                "Giocare carta Bang",
                "Equipaggiare nuova arma",
                "Scartare e passare il turno",
            ],
            False,
            True,
        )
        choice = menu_dinamico.choose()
        match choice:
            case 1:
                carte_bang = self.ControllaCartaBang()
                if carte_bang == 0:
                    print("ERROR: Non hai carte bang in mano")
                else:
                    scegli_bersaglio = int(input("Inserisci il la persona a cui sparare"))
                    
                        
                    
            case 2:
                carte_arma = self.ControllaCartaEquipaggiamento()
                if not carte_arma:
                    print("Errore, non c'è nessuna carta equipaggiamento")
                elif len(carte_arma) == 1:
                    self._equipaggiamenti.clear()
                    self._equipaggiamenti.append(carte_arma)
                else:
                    quale_arma = self.ScegliCartaEquipaggiamento(carte_arma)
                    self._equipaggiamenti.clear()
                    self._equipaggiamenti.append(quale_arma)

    def gioca_carta(self, carta, bersaglio):
        carta_bang_giocata = False
