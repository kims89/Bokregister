# Som beskrevet i oppgaven la jeg opp slik at produkt var den øvrige klassen, mens bøker, musikk
# og spill var underklasser. på denne måten vil jeg spare mye skriving for at underklassene kan hente
#supernøkler fra hovedklassen som er denne.
class Produkt:
#disse hentes ut med supernøkler.
      def __init__(self,produktidentitet,produktnavnet,produktnettoprisen):
            self.__produktID = produktidentitet
            self.__produktnavn = produktnavnet
            self.__produktnetto = produktnettoprisen

      def setProduktID(self,produktidentitet):
            self.__produktID = produktidentitet
      def getProduktID(self):
            return self.__produktID
      
      def setProduktnavn(self,produktnavnet):
            self.__produktnavn = produktnavnet
      def getProduktnavn(self):
            return self.__produktnavn

      def setProduktnetto(self,produktnettoprisen):
            self.__produktnetto = produktnettoprisen
      def getProduktnetto(self):
            return self.__produktnetto

      def __str__(self):
            produktinformasjon = "Produktidentitet er: "+str(self__produktID)+"\n"\
                                 +"Produktnavn er: "+(self.__produktnavn)+" \n"\
                                 +"Nettopris er: "+ str(self.__produktnetto)
            return produktinformasjon
