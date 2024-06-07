class Giocatore:
    def __init__(self, nome: str, ruolo: str, pf: int, descrizione: str, mano: list):
        self._nome = nome
        self._ruolo = ruolo
        self._descrizione = descrizione
        self._pf = pf
        self._mano = []
        self._equipaggiamenti = []

    def PescaCarte(self, mazzo, numero_carte):
        carte_pescate = []
        for i in range(numero_carte):
            if mazzo:
                carte_pescate.append(mazzo.pop(0))
            else:
                self.RigeneraMazzo()
                carte_pescate.append(mazzo.pop(0))
        return carte_pescate

    def gioca_carta(self, carta, bersaglio):
        
    
    