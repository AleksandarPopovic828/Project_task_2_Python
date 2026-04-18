#Proekt 2
#ime na klient: OneLizing.mk
#Programa sto sporeduva 2 ili povekje lizing ponudi i gi prikazuva mesecnuite plakjanja i vkupniot trosok

import math

class LizingPonuda:
    def __init__(self, ime, cena, ucestvo, kamata, meseci):
        self.ime = ime
        self.cena = cena
        self.ucestvo = ucestvo
        self.kamata = kamata
        self.meseci = meseci
    
    def mesecna_rata(self):
        dolg = self.cena - self.ucestvo
        mesecna_kamata = (self.kamata/100)/12

        if mesecna_kamata == 0:
            return dolg / self.meseci
        
        rata = dolg * (mesecna_kamata * (1 + mesecna_kamata)**self.meseci) / ((1 + mesecna_kamata) ** self.meseci - 1)
        return rata
    
    def vkupen_trosok(self):
        mesecen = self.mesecna_rata()
        return mesecen * self.meseci + self.ucestvo
    
def sporedi_lizing(ponudi):
    print("\nLizing Sporedba Za OneLizing.mk:\n")
    print(f"{'offer':15}{'Mesecna Rata':<20}{'Vkupen Trosok'}")
    print("-" * 55)

    for ponuda in ponudi:
        mesecno = ponuda.mesecna_rata()
        vkupno = ponuda.vkupen_trosok()
        print(f"{ponuda.ime:<15}{mesecno:<20.2f}{vkupno:<20.2f}")

# Primer ponudi
ponudi = [
    LizingPonuda("Diler A", cena=30000, ucestvo=3000, kamata=4.5, meseci=36),
    LizingPonuda("Diler B", cena=29500, ucestvo=2500, kamata=5.0, meseci=36),
    LizingPonuda("Diler C", cena=31000, ucestvo=2000, kamata=3.9, meseci=48),
]

sporedi_lizing(ponudi)    




