class Giocatore:
    def __init__(self, nome: str, ruolo: str, punti_ferita, descrizione: str):
        self._nome = nome
        self._ruolo = ruolo
        self._descrizione = descrizione
        self._punti_ferita = punti_ferita
