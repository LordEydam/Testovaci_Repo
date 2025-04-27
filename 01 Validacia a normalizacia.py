class Osoba:
    def __init__(self):
        #inicializovat privatnu premennu
        #private / sukromny __vlastnost len tato trieda
        #protected _vlastnost tato trieda aj odvodene, detske triedy
        self.__vek = 0


    #getter, get metoda
    @property
    def vek(self):
        return self.__vek


    #setter, set metoda
    #zmenit, nastavit hodnoty, zapis
    @vek.setter
    def vek(self, hodnota):
        if hodnota < 0:
            raise ValueError("🤦🤦🤦🤦🤦nemozes mat minusovy vek ty kokot! 🤦🤦🤦🤦🤦🤦🤦🤦")
        self.__vek = hodnota


#vytvarame instancie:

karol = Osoba()
karol.vek = 40
print(f"Osoba am {karol.vek} rokov")

maria = Osoba()
maria.vek = 21
print(f"Osoba am {maria.vek} rokov")

oto = Osoba()
oto.vek = 30
print(f"Osoba am {oto.vek} rokov")

import math
class Kruh:
    def __init__(self, polomer):
        self._polomer = polomer

    #get metoda
    @property
    def polomer(self):
        return self._polomer

    @polomer.setter
    def polomer(self, hodnota):
         if hodnota < 0:
             raise ValueError("Polomer musi byt kladne cislo a ty tela!!")
         self._polomer = hodnota

    @property
    def obvod(self):
        return round(2 * math.pi * self._polomer, 3)

    @property
    def obsah(self):
        return round(math.pi * math.pow(self._polomer, 2), 3)


kruh1 = Kruh(10)
kruh1.polomer = 20

print(f"kruh1 ma obvod {kruh1.obvod} m a obsah {kruh1.obsah} m^2")
