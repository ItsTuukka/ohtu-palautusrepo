KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin on oltava positiivinen numero.")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon on oltava positiivinen numero.")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        for n in self.ljono:
            if n == numero:
                return True
        return False

    def lisaa(self, numero):
        if self.kuuluu(numero):
            return False

        self.ljono[self.alkioiden_lkm] = numero
        self.alkioiden_lkm += 1

        if self.alkioiden_lkm % len(self.ljono) == 0:
            vanha_lista = self.ljono
            self.kopioi_taulukko(self.ljono, vanha_lista)
            self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(vanha_lista, self.ljono)

        return True

    def poista(self, numero):
        loyty = False

        for i in range(0, len(self.ljono)-1):
            if not loyty:
                if self.ljono[i] == numero:
                    self.ljono[i] = self.ljono[i+1]
                    self.alkioiden_lkm -= 1
                    loyty = True
            else:
                self.ljono[i] = self.ljono[i+1]

        return loyty

    def kopioi_taulukko(self, kopioitava_lista, kopio):
        for i in range(0, len(kopioitava_lista)):
            kopio[i] = kopioitava_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        lista = [0] * self.alkioiden_lkm
        for i in range(0, len(lista)):
            lista[i] = self.ljono[i]
        return lista

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        for numero in a.to_int_list():
            joukko.lisaa(numero)

        for numero in b.to_int_list():
            joukko.lisaa(numero)

        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()

        for numero in a.to_int_list():
            for numero2 in b.to_int_list():
                if numero == numero2:
                    joukko.lisaa(numero)

        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        for numero in a.to_int_list():
            joukko.lisaa(numero)

        for numero in b.to_int_list():
            joukko.poista(numero)

        return joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        string = "{"
        for number in self.ljono:
            if number != 0:
                string += str(number) + ", "
        string = string[:-2] + "}"
        return string
