#Dette er underklasse for produkt.
# Jeg har lagt opp opgaven på den måten at utregningen av merverdi blir
# regnet ut i HOVED.py
#For å teste musikk kan man kjøre denne for å legge inn (husk klammer på data som ikke er int)")
#eksempel = Musikk(produktidentitet,produktnavnet,artisten,produktnettoprisen,merverdien)")
#og for å skrive ut
#print(eksempel)
from produkt import Produkt

class Musikk(Produkt):

    def __init__(self,produktidentitet,produktnavnet,artisten,produktnettoprisen,merverdien):
        super().__init__(produktidentitet,produktnavnet,produktnettoprisen)
        self.__artist = artisten
        self.__merverdi = merverdien

    def setArtist(self,artisten):
        self.__artist = artisten
    def getArtist(self):
        return self.__artist

    def setMere(self,merverdien):
        self.__merverdi = merverdien
    def getMere(self):
        return self.__merverdi

    def __str__(self):
        musikkinformasjon = "Musikk \n"\
                   +"Navnet er: "+(self.getProduktnavn())+" \n"\
                   +"Artisten er: "+self.__artist+" \n"\
                   +"Nettoprisen er: "+str(self.getProduktnetto())+" \n"\
                   +"Bruttopris er: "+str(self.__merverdi)+" \n"
        return musikkinformasjon
