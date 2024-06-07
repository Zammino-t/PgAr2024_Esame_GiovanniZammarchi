from classMazzo import Carta, Arma
from classPartita import Partita
from kibo_pgar_lib import Menu
from math import abs


class Giocatore:
    def __init__(self, nome: str, ruolo: str, pf: int, descrizione: str):
        self._nome = nome
        self._ruolo = ruolo
        self._descrizione = descrizione
        self._pf = pf
        self._mano: list[Carta] = []
        self._equipaggiamenti = []

    def PescaCarte(self, mazzo, numero_carte):
        for _ in range(numero_carte):
            if mazzo:
                self._mano.append(mazzo.pop(0))
            else:
                # Gestire rigenerazione mazzo
                pass

    def ControllaCartaEquipaggiamento(self):
        return [carta for carta in self._mano if isinstance(carta, Arma)]

    def ScegliCartaEquipaggiamento(self, carte_arma):
        scegli_arma = Menu(
            "Quale arma vuoi equipaggiare: ",
            [arma.nome for arma in carte_arma],
            False,
            True,
        )
        scelta = scegli_arma.choose()
        return carte_arma[scelta - 1]

    def ControllaCartaBang(self):
        quante_carte_bang = 0
        for carta in self._mano:
            if carta._nome == "BANG!":
                quante_carte_equi += 1
        return quante_carte_bang

    def PossoSparare(self, bersaglio, partita: Partita):
        mia_posizione = partita._giocatori.index(self)
        distanza_bersaglio = abs(mia_posizione - partita._giocatori.index(bersaglio))
        return self._equipaggiamenti[0]._distanza >= distanza_bersaglio

    def menu_gioca_carta(self, partita: Partita):
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
        if choice == 1:
            if self.ControllaCartaBang() == 0:
                print("ERROR: Non hai carte bang in mano")
            else:
                scegli_bersaglio = int(input("Inserisci il la persona a cui sparare"))
                bersaglio = partita._giocatori[scegli_bersaglio]
                if self.PossoSparare(bersaglio, partita):
                    # Logica per sparare
                    pass
                else:
                    print("Il bersaglio è troppo lontano.")
        elif choice == 2:
            carte_arma = self.ControllaCartaEquipaggiamento()
            if not carte_arma:
                print("Errore, non c'è nessuna carta equipaggiamento")
            elif len(carte_arma) == 1:
                self._equipaggiamenti.clear()
                self._equipaggiamenti.append(carte_arma[0])
            else:
                quale_arma = self.ScegliCartaEquipaggiamento(carte_arma)
                self._equipaggiamenti.clear()
                self._equipaggiamenti.append(quale_arma)

    def gioca_carta(self, carta, bersaglio):
        pass
