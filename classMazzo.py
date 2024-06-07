import random


class Carta:
    def __init__(self, nome, equipaggiabile, descrizione, valore=None, seme=None):
        self._nome = nome
        self._descrizione = descrizione
        self._equipaggiabile = equipaggiabile
        self._valore = valore
        self._seme = seme


class Arma(Carta):
    def __init__(self, nome, distanza, valore, seme):
        self._distanza = distanza
        super().__init__(nome, valore, seme)
