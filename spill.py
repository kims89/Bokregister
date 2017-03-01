# underklasse for produkt.
# Jeg har gjort en eller annen skrivefeil som jeg ikke klarer å finne ut av.
# dette betyr at når man skal skrive ut fra denne klassen så får man feil.
# Bok og musikk fungerer.

# Jeg har lagt opp opgaven på den måten at utregningen av merverdi og administrasjonsavgift blir
# regnet ut i HOVED.py
#For å teste spill kan man kjøre denne for å legge inn (husk klammer på data som ikke er int)

#eksempel = Spill(produktidentitet,produktnavnet,sjangeren,aldersgrensen,produktnettoprisen,merverdien,admavgiften)
#og for å skrive ut"
#print(eksempel)

from produkt import Produkt
class Spill(Produkt):       
       def __init__(self,produktidentitet,produktnavnet,sjangeren,aldersgrensen,produktnettoprisen,merverdien,admavgiften):
              super().__init__(produktidentitet,produktnavnet,produktnettoprisen)
              self.__sjanger = sjangeren
              self.__aldersgrense = aldersgrensen
              self.__merverdi = merverdien
              self.__admavgift = admavgiften              

       def setSjanger(self,sjangeren):
           self.__sjanger = sjangeren
       def getSjanger(self):
           return self.__sjanger

       def setAldersgrense(self,aldersgrensen):
           self.__aldersgrense = aldersgrensen
       def getAldersgrense(self):
           return self.__aldersgrense

       def setMere(self,merverdien):
           self.__merverdi = merverdien
       def getMere(self):
           return self.__merverdi

       def setAdmavgift(self,admavgiften):
           self.__admavgift = admavgiften
       def getAdmavgift(self):
           return self.__admavgift
       
       def __init___(self):
           spillinformasjon = " \n"\
                              +"Tittelen er: "+(self.getProduktnavn())+" \n"\
                              +"Sjangeren er: "+self.__sjanger+" \n"\
                              +"Aldergrensen er: "+str(self.__aldersgrense)+" \n"\
                              +"Administrasjonsavgift er: "+str(self.__admavgift)+" \n"\
                              +"Bruttoprisen er: "+str(self.__merverdi)+" \n"\
                              +"Nettoprisen er: "+str(self.getProduktnetto())+" \n"
                                                      
           return spillinformasjon
            

       
             
