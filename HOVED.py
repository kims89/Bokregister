#HOVED

#Kjør denne for å få menyene

#Fikk ikke til å lage programmet på den måten at man kan endre på produkter som allerede er lagt inn
#Prøvde flere forskjellige varianter, men ingen  i nærheten av suksess dessverre.

#i forhold til at pickle måtte brukes i oppgaven måtte dette importeres inn i python-filen som skal
#skrive ut pickle.
import pickle
#klassene musikk, bok, spill, produktregister blir importert, produkt trengs ikke importeres på grunn
#av at den hentes fra de andre underklassene.
from musikk import Musikk
from bok import bok
from spill import Spill
from produktregister import Produktregister
produktereg = Produktregister()
while True:
      meny = input("Tast 1 for å legge inn bok\n"
                 +"Tast 2 for å legge inn musikk\n"
                 +"Tast 3 for å legge inn spill\n"
                 +"Tast 4 for å skrive ut alle produkter\n"
                 +"Tast 5 for å lagre data til fil og avslutte\n"
                 +"Tast 6 for å laste inn produkter fra fil\n"
                 +" " "\n")

      if meny == "1":
#her opprettes det nye bøker
        print("")
        produktID = int(input("Skriv inn produktid til bok (Maksimalt 3 tall): "))
        produktnavn = input("Skriv inn tittel på bok: ")
        forfatter = input("Skriv inn forfatter: ")
        netto = int(input("Skriv inn nettopris: "))
        nyBok = bok(produktID,produktnavn,forfatter,netto)
        produktereg.LeggInnProdukt(nyBok)
        print("")
        print("Boken ble lagt til!")
        print("")

      elif meny == "2":
#her opprettes det nye musikk.
#Kanskje ikke helt rolls royce løsning, men valgte å regne ut merverdi gjennom netto som blir
#fyllt ut. Mest ideelt hadde vært å regne dette ut gjennom klassen musikk.
        print("")
        produktID = int(input("Skriv inn produktid til bok (Maksimalt 3 tall): "))
        produktnavn = input("Skriv inn albumnavn: ")
        Artist = input("Skriv inn Artist: ")
        netto = int(input("Skriv inn nettopris: "))
        merverdi = netto*1.14
        nyMusikk = Musikk(produktID,produktnavn,Artist,netto,merverdi)
        produktereg.LeggInnProdukt(nyMusikk)
        print("")
        print("CDen er lagt til!")
        print("")

      elif meny == "3":
#her opprettes det nye spill.
#Kanskje ikke helt rolls royce løsning, men valgte å regne ut merverdi og administrasjonavgift gjennom netto som blir
#fyllt ut. Mest ideelt hadde vært å regne dette ut gjennom klassen spill.

#på grunn av skrivefeilen jeg ikke finner så fungerer ikke det skrive ut informasjon fra spill
        print("")
        produktID = int(input("Skriv inn produktid til bok (Maksimalt 3 tall): "))
        produktnavn = input("Skriv inn tittel: ")
        sjanger = input("Skriv inn sjanger: ")
        alder = int(input("Skriv inn aldersgrense: "))
        netto = int(input("Skriv inn nettopris: "))
        merverdi = netto*1.14
        Admavgift = merverdi*1.05
        nySpill = Spill(produktID,produktnavn,sjanger,alder,netto,merverdi,admavgift)
        produktereg.LeggInnProdukt(nySpill)
        print("")
        print("spillet ble lagt til!")
        print("")

      elif meny == "4":
#denne skriver ut alle dokumenter
#på grunn av skrivefeilen så fungerer ikke det å skrive ut spill.
            produktereg.SkrivUtProdukter()

      elif meny =="5":
#denne bruker produktereg (som ble brukt til utskrift) til å skrive ut til pickle-filen, og deretter lukke filen
            try:
                  print("Filen lagres")
                  utskriftTilFil = open("filen.pck","wb")
                  pickle.dump(produktereg,utskriftTilFil)
                  print("_"*20+"Ferdig"+"_"*20)
            finally:
                  utskriftTilFil.close()

      elif meny == "6":
#denne laster inn informasjon fra pickle-filen. og avslutter programmet.
            try:
                  print("Filen lastes over")
                  utskriftFraFil = open("filen.pck","rb")
                  produktereg = pickle.load(utskriftFraFil)
                  print("_"*20+"Ferdig"+"_"*20)
            finally:
                  utskriftFraFil.close()
            
