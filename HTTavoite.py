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

import numpy
import HTTavoiteKirjasto

RIVEJA = 54
SARAKKEITA = 4

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi vuodenaikatulokset")
    print("5) Lue ja yhdistä paisteaikatiedosto")
    print("6) Kirjoita yhdistetty data tiedostoon")
    print("7) Analysoi viikoittaiset tulokset")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def paaohjelma():
    Lista = []
    Tulokset = []
    VuodenaikaTulokset = []
    Sanakirja = {}
    Matriisi = numpy.zeros((RIVEJA, SARAKKEITA), int)
    valinta = valikko()
    while valinta != 0:
        if valinta == 1:
            kehote = "Anna luettavan tiedoston nimi: "
            Nimi = HTTavoiteKirjasto.kysyNimi(kehote)
            Lista = HTTavoiteKirjasto.lueTiedosto(Nimi, Lista)
        elif valinta == 2:
            if len(Lista) > 0:
                Tulokset = HTTavoiteKirjasto.analysoiKuukaudet(Lista, Tulokset)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
        elif valinta == 3:
            if len(Lista) > 0:
                kehote = "Anna kirjoitettavan tiedoston nimi: "
                Nimi = HTTavoiteKirjasto.kysyNimi(kehote)
                HTTavoiteKirjasto.kirjoitaTiedosto(Nimi, Tulokset)
            else:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
        elif valinta == 4:
            if len(Lista) > 0:
                VuodenaikaTulokset = HTTavoiteKirjasto.analysoiVuodenajat(Lista, VuodenaikaTulokset)
                kehote = "Anna kirjoitettavan tiedoston nimi: "
                Nimi = HTTavoiteKirjasto.kysyNimi(kehote)
                HTTavoiteKirjasto.kirjoitaTiedostoVuodenaika(Nimi, VuodenaikaTulokset)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
        elif valinta == 5:
            if len(Lista) > 0:
                kehote = "Anna luettavan tiedoston nimi: "
                Nimi = HTTavoiteKirjasto.kysyNimi(kehote)
                Sanakirja = HTTavoiteKirjasto.lueJaYhdista(Nimi, Sanakirja)
            else:
                print("Lue sähköntuottotiedot ennen paisteaikatietoja.")
        elif valinta == 6:
            if (len(Lista) > 0) and (len(Sanakirja) > 0):
                kehote = "Anna kirjoitettavan tiedoston nimi: "
                Nimi = HTTavoiteKirjasto.kysyNimi(kehote)
                HTTavoiteKirjasto.kirjoitaTiedostoYhdistetty(Nimi, Lista, Sanakirja)
            elif (len(Lista) == 0):
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            elif (len(Sanakirja) == 0):
                print("Ei tietoja tallennettavaksi, lue ja yhdistä tiedot ennen tallennusta.")
        elif valinta == 7:
            if len(Lista) > 0:
                Matriisi = HTTavoiteKirjasto.matriisi(Matriisi, Lista)
                kehote = "Anna kirjoitettavan tiedoston nimi: "
                Nimi = HTTavoiteKirjasto.kysyNimi(kehote)
                HTTavoiteKirjasto.tallennaMatriisi(Matriisi, Nimi)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        valinta = valikko()
    print("Lopetetaan.")
    Lista.clear()
    Tulokset.clear()
    VuodenaikaTulokset.clear()
    Sanakirja.clear()
    Matriisi = numpy.delete(Matriisi, numpy.s_[:], None)
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
