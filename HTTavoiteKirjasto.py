######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Simo Mustakallio
# Opiskelijanumero: 003411683
# Päivämäärä: 6.12.2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTTavoite.py
# eof

import sys
import time
import numpy

VUODENAJAT = ["Kevät", "Kesä", "Syksy", "Talvi"]
ALUE1PANEELIT = 330
ALUE2PANEELIT = 210
ALUE3PANEELIT = 66
ALUE4PANEELIT = 210
RIVEJA = 54
SARAKKEITA = 4

class TIETO:
    Aikaleima = None
    Alue1 = None
    Alue2 = None
    Alue3 = None
    Alue4 = None

class KUUKAUSI:
    Alue1 = None
    Alue2 = None
    Alue3 = None
    Alue4 = None
    Olemassaolo = None

def kysyNimi(Kehote):
    Nimi = input(Kehote)
    while Nimi.endswith(".txt") == False:
        print("Tiedostopääte väärin. Anna uusi nimi.")
        Nimi = input(Kehote)
    return Nimi

def lueTiedosto(Nimi, Lista):
    try:
        Lista.clear()
        tiedosto = open(Nimi, "r", encoding="UTF-8")
        Rivi = tiedosto.readline()
        Rivi = tiedosto.readline()
        while (len(Rivi) > 0):
            Data = TIETO()
            osat = Rivi.strip().split(";")
            Data.Aikaleima = osat[0]
            Data.Alue1 = int(osat[1])
            Data.Alue2 = int(osat[2])
            Data.Alue3 = int(osat[3])
            Data.Alue4 = int(osat[4])
            Lista.append(Data)
            Rivi = tiedosto.readline()
        tiedosto.close()
        tuloste = "Tiedostosta '" + Nimi + "' lisättiin listaan " + str(len(Lista)) + " datariviä."
        print(tuloste)
    except OSError:
        tuloste = "Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan."
        print(tuloste)
        sys.exit(0)
    return Lista

def analysoiKuukaudet(Lista, Tulokset):
    Tulokset.clear()
    Kuukaudet = []
    for i in range(12):
        KuukausiData = KUUKAUSI()
        KuukausiData.Alue1 = 0
        KuukausiData.Alue2 = 0
        KuukausiData.Alue3 = 0
        KuukausiData.Alue4 = 0
        KuukausiData.Olemassaolo = False
        Kuukaudet.append(KuukausiData)
    for i in Lista:
        Aika = time.strptime(i.Aikaleima, "%d/%m/%Y")
        Luku = Aika.tm_mon - 1
        Kuukaudet[Luku].Olemassaolo = True
        Kuukaudet[Luku].Alue1 += i.Alue1
        Kuukaudet[Luku].Alue2 += i.Alue2
        Kuukaudet[Luku].Alue3 += i.Alue3
        Kuukaudet[Luku].Alue4 += i.Alue4
    for i in range(12):
        A1 = Kuukaudet[i].Alue1
        A2 = Kuukaudet[i].Alue2
        A3 = Kuukaudet[i].Alue3
        A4 = Kuukaudet[i].Alue4
    Tulokset.append("Kuukausittaiset tuotot (kWh):\n")
    Tulokset.append("Kuukausi;Alue1;Alue2;Alue3;Alue4\n")
    Luku = 0
    for i in range(12):
        if Kuukaudet[i].Olemassaolo:
            A1 = Kuukaudet[i].Alue1
            A2 = Kuukaudet[i].Alue2
            A3 = Kuukaudet[i].Alue3
            A4 = Kuukaudet[i].Alue4
            Paiva = "01/{0}/2000".format(i+1)
            Kuu = time.strptime(Paiva, "%d/%m/%Y")
            Nimi = time.strftime("%B", Kuu)
            Tuloste = "{0};{1:.1f};{2:.1f};{3:.1f};{4:.1f}\n".format(Nimi, A1/1000, A2/1000, A3/1000, A4/1000)
            Tulokset.append(Tuloste)
            Luku += 1
    print("Kuukausittaiset summat laskettu", str(Luku), "kuukaudelle.")
    Kuukaudet.clear()
    return Tulokset

def kirjoitaTiedosto(Nimi, Tulokset):
    try:
        tiedosto = open(Nimi, "w", encoding="UTF-8")
        for i in range(len(Tulokset)):
                tiedosto.write(Tulokset[i])
        tiedosto.close()
        tuloste = "Tiedosto '" + Nimi + "' kirjoitettu."
        print(tuloste)
    except OSError:
        tuloste = "Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan."
        print(tuloste)
        sys.exit(0)
    return None

def kirjoitaTiedostoVuodenaika(Nimi, VuodenaikaTulokset):
    try:
        tiedosto = open(Nimi, "w", encoding="UTF-8")
        for i in range(len(VuodenaikaTulokset)):
            tiedosto.write(VuodenaikaTulokset[i])
        tiedosto.close()
        tuloste = "Tiedosto '" + Nimi + "' kirjoitettu."
        print(tuloste)
    except OSError:
        tuloste = "Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan."
        print(tuloste)
        sys.exit(0)
    return None

def kirjoitaTiedostoYhdistetty(Nimi, Lista, Sanakirja):
    try:
        tiedosto = open(Nimi, "w", encoding="UTF-8")
        tiedosto.write("Päivittäiset tuotot (Wh) ja paisteaika (s):\n")
        tiedosto.write("Aikaleima;Alue 1 (Wh);Alue 2 (Wh);Alue 3 (Wh);Alue 4 (Wh);Päiväsumma (Wh);Paisteaika (s)\n")
        for i in range(len(Lista)):
            Aika = time.strptime(Lista[i].Aikaleima, "%d/%m/%Y")
            Paivamaara = time.strftime("%Y%m%d", Aika)
            Paivasumma = Lista[i].Alue1 + Lista[i].Alue2 + Lista[i].Alue3 + Lista[i].Alue4
            tiedosto.write("{0};{1};{2};{3};{4};{5};{6}\n".format(time.strftime("%d.%m.%Y", Aika), str(Lista[i].Alue1), str(Lista[i].Alue2), str(Lista[i].Alue3), str(Lista[i].Alue4), str(Paivasumma), Sanakirja[Paivamaara]))
        tiedosto.close()
        tuloste = "Tiedosto '" + Nimi + "' kirjoitettu."
        print(tuloste)
    except OSError:
        tuloste = "Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan."
        print(tuloste)
        sys.exit(0)
    return None
        

def analysoiVuodenajat(Lista, VuodenaikaTulokset):
    Kevat = 0
    Kesa = 0
    Syksy = 0
    Talvi = 0
    for Data in Lista:
        Aika = time.strptime(Data.Aikaleima, "%d/%m/%Y")
        Kuukausi = Aika.tm_mon
        Summa = Data.Alue1 + Data.Alue2 + Data.Alue3 + Data.Alue4
        if Kuukausi in [3, 4, 5]:
            Kevat += Summa
        elif Kuukausi in [6, 7, 8]:
            Kesa += Summa
        elif Kuukausi in [9, 10, 11]:
            Syksy += Summa
        elif Kuukausi in [12, 1, 2]:
            Talvi += Summa
            
    Kevat /= 1000
    Kesa /= 1000
    Syksy /= 1000
    Talvi /= 1000
    
    VuodenaikaTulokset.clear()
    VuodenaikaTulokset.append("Vuodenaika;Tuotto (kWh)\n")
    tuloste = "{0};{1:.1f}\n".format(VUODENAJAT[0], Kevat)
    VuodenaikaTulokset.append(tuloste)
    tuloste = "{0};{1:.1f}\n".format(VUODENAJAT[1], Kesa)
    VuodenaikaTulokset.append(tuloste)
    tuloste = "{0};{1:.1f}\n".format(VUODENAJAT[2], Syksy)
    VuodenaikaTulokset.append(tuloste)
    tuloste = "{0};{1:.1f}\n".format(VUODENAJAT[3], Talvi)
    VuodenaikaTulokset.append(tuloste)
    return VuodenaikaTulokset

def lueJaYhdista(Nimi, Sanakirja):
    try:
        Sanakirja.clear()
        tiedosto = open(Nimi, "r", encoding="UTF-8")
        Rivi = tiedosto.readline()
        Rivi = tiedosto.readline()
        while (len(Rivi) > 0):
            osat = Rivi.strip().split(",")
            if int(osat[2]) < 10:
                Kuukausi = "0" + osat[2]
            else:
                Kuukausi = osat[2]
            if int(osat[3]) < 10:
                Paiva = "0" + osat[3]
            else:
                Paiva = osat[3]
            Paivamaara = osat[1] + Kuukausi + Paiva
            Sanakirja[Paivamaara] = int(osat[4])
            Rivi = tiedosto.readline()
        tiedosto.close()
        tuloste = "Tiedosto '" + Nimi + "' luettu."
        print(tuloste)
        print("Tiedot yhdistetty.")
    except OSError:
        tuloste = "Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan."
        print(tuloste)
        sys.exit(0)
    return Sanakirja

def matriisi(Matriisi, Lista):
    Matriisi[:] = 0
    for i in range(len(Lista)):
        Aika = time.strptime(Lista[i].Aikaleima, "%d/%m/%Y")
        Viikko = int(time.strftime("%W", Aika))
        Matriisi[Viikko][0] += Lista[i].Alue1
        Matriisi[Viikko][1] += Lista[i].Alue2
        Matriisi[Viikko][2] += Lista[i].Alue3
        Matriisi[Viikko][3] += Lista[i].Alue4
    print("Matriisianalyysi suoritettu.")
    return Matriisi

def tallennaMatriisi(Matriisi, Nimi):
    try:
        tiedosto = open(Nimi, "w", encoding="UTF-8")
        tiedosto.write("Viikko;Alue 1 (Wh/paneeli);Alue 2 (Wh/paneeli);Alue 3 (Wh/paneeli);Alue 4 (Wh/paneeli);Viikkosumma (Wh)\n")
        Yhteensa = 0
        AlueSumma = [0, 0, 0, 0]
        ViikkoSumma = 0
        for Rivi in range(RIVEJA):
            tiedosto.write("Vko " + str(Rivi) + ";")
            ViikkoSumma = 0
            for Sarake in range(SARAKKEITA):
                Tulos = Matriisi[Rivi][Sarake]
                if Sarake == 0:
                    tiedosto.write("{0:.1f};".format(Tulos / ALUE1PANEELIT))
                elif Sarake == 1:
                    tiedosto.write("{0:.1f};".format(Tulos / ALUE2PANEELIT))
                elif Sarake == 2:
                    tiedosto.write("{0:.1f};".format(Tulos / ALUE3PANEELIT))
                elif Sarake == 3:
                    tiedosto.write("{0:.1f};".format(Tulos / ALUE4PANEELIT))
                ViikkoSumma += Tulos
                AlueSumma[Sarake] += Tulos
            tiedosto.write("{0:.1f}\n".format(ViikkoSumma))
            Yhteensa += ViikkoSumma
        tiedosto.write("Yhteensä;{0:.1f};{1:.1f};{2:.1f};{3:.1f};{4:.1f}".format(AlueSumma[0], AlueSumma[1], AlueSumma[2], AlueSumma[3], Yhteensa))
        tiedosto.close()
        tuloste = "Tiedosto '" + Nimi + "' kirjoitettu."
        print(tuloste)
        AlueSumma.clear()
    except OSError:
        tuloste = "Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan."
        print(tuloste)
        sys.exit(0)
    return None
    
