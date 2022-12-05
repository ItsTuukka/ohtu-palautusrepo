class Summa:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote
        self._edellinen_lisatty = 0

    def suorita(self):
        self._edellinen_lisatty = self._lue_syote()
        self._sovellus.plus(self._edellinen_lisatty)
    
    def kumoa(self):
        self._sovellus.miinus(self._edellinen_lisatty)

class Erotus:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote
        self._edellinen_vahennetty = 0

    def suorita(self):
        self._edellinen_vahennetty = self._lue_syote()
        self._sovellus.miinus(self._edellinen_vahennetty)

    def kumoa(self):
        self._sovellus.plus(self._edellinen_vahennetty)

class Nollaus:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovellus.tulos
        self._sovellus.nollaa()

    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen_arvo)

class Kumoa:
    def __init__(self, sovellus, edellinen_komento):
        self._sovellus = sovellus
        self._edellinen_komento = edellinen_komento

    def suorita(self):
        edellinen_komento = self._edellinen_komento()
        if edellinen_komento:
            print("kumoaa")
            edellinen_komento.kumoa()