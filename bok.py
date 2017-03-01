# Her er underklasse for produkt.
# Takket være supernøklene fra produkt trengte jeg bare å legge ved forfatter. Det er ikke
# merverdi på bøker.
from produkt import Produkt

#For å teste bok kan man kjøre denne for å legge inn (husk klammer på data som ikke er int)

#eksempel = bok(produktidentitet,produktnavnet,forfatteren,produktnettoprisen)

#og for å skrive ut
#print(eksempel)

class bok(Produkt):
      def __init__(self,produktidentitet,produktnavnet,forfatteren,produktnettoprisen):
            super().__init__(produktidentitet,produktnavnet,produktnettoprisen)
            self.__forfatter = forfatteren

      def setForfatter(self,forfatteren):
            self.__forfatter =forfatteren
      def getForfatter(self):
            return self.__forfatter

      def __str__(self):
            bokinformasjon = "Musikk \n"\
                             +"Navnet er: "+(self.getProduktnavn())+" \n"\
                             +"Forfatteren er: "+self.__forfatter+" \n"\
                             +"Nettoprisen er: "+str(self.getProduktnetto())+" \n"
            return bokinformasjon
