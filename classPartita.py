import random
from classMazzo import Carta

# from classGiocatore import Giocatore
from Giocatore import Giocatore


class Partita:
    def __init__(self, dati_json) -> None:
        self.ruoli = ["sceriffo", "fuorilegge", "rinnegato", "vice"]
        self.mazzo = self.CreaMazzo()
        self._giocatori: list[Giocatore] = []
        self.personaggi = dati_json["personaggi"]
        self.armi = dati_json["armi"]
        self.carte = dati_json["carte"]
        self.turno_corrente = 0

    def IniziaGioco(self):
        for giocatore in self._giocatori:
            giocatore.PescaCarte(self.mazzo, giocatore.pf)

    def CreaMazzo(self):
        mazzo = []
        for carta in self.carte:
            for copia in carta["copie"]:
                mazzo.append(
                    Carta(
                        carta["nome"],
                        carta["descrizione"],
                        carta["equipaggiabile"],
                        copia["valore"],
                        copia["seme"],
                    )
                )
        random.shuffle(mazzo)
        return mazzo

    def GestisciTurno(self):
        giocatore_corrente: Giocatore = self._giocatori[self.turno_corrente]
        print(f"Turno di {giocatore_corrente._nome}")
        giocatore_corrente.PescaCarte(self.mazzo, 2)
        giocatore_corrente.menu_gioca_carta()
        self.turno_corrente = (self.turno_corrente + 1) % len(self._giocatori)
