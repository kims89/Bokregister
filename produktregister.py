#denne importerer inn bok, spill og musikk.. Når vi bruker hoved.py så brukes denne
#for å legge inn produktene og skrive produktene ut.

from musikk import Musikk
from bok import bok
from spill import Spill

class Produktregister:
      def __init__(self):
            self.__produktListe = []

      def LeggInnProdukt(self,SettProduktet):
            self.__produktListe.append(SettProduktet)

      def SkrivUtProdukter(self):
            for produktereg in self.__produktListe:
                  print(produktereg)
