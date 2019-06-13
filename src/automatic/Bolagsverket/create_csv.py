"""
Python3-skript för att skapa en CSV-databas från Bolagsverkets databas.

CSV-databasen lagras i SBX Github-repo, men originaldatabasen lagras inte
på Github eftersom den kan innehålla känslig information.
Framförallt org-/personnummer tar vi inte med, inte heller
några enskilda firmor (OBJTYP = "E").

Användning:
python3 create_csv.py original-2019-04-30/*.txt > bolagsinformation.csv
"""

import sys
import fileinput
import csv

RECORDS = [
    ### onödiga fält är bortkommenterade:
    # ('POSTBETECK',     0,   6),  # Postbeteckning = UNIREG. Avisering från AB-registret, Handels- och föreningsregistren, Bank- o försäkringsregistret HU-POSTID (HU-AVISERPOS T) skrivs i början på varje rad i filen (före respektive posttyp).
    # ('UTSKRIFTDAT',    6,  14),  # Datum då posten skrivs i aviseringsregistret
    # ('ERENDEREGDAT',  14,  30),  # Ärendets registreringsdatum och tidpunkt hos Bolagsverket
    ('OBJTYP',        30,  35),  # Objekttyp/företagsform/registerspecifikt
    # ('SEK',           35,  36),  # Sekel, värde: 9/8/blank. 9=1900, 8=1800
    ### vi vill inte ha med personnummer i github-databasen:
    # ('ORGNR',         36,  46),  # Objektets organisationsnummer eller personnummer
    # ('LOPNR',         46,  51),  # Löpnummer (identitet). Används för företag som har flera näringsdrivande företag registrerade på samma organisationsnummer eller per sonnummer. Avser: E, I, S, TSF
    # ('DINR',          51,  58),  # Ärendets ärendenummer
    # ('DINRAR',        58,  62),  # Ärendenumrets årtal
    ('ERENDETYP',     62,  65),  # Markering av ärendetyp. Värde: NYB/AND/KOR/BAS
    ('HISTMARK',      65,  66),  # Markering om ärendet är ett historiskt ärende. Värde: H/blank. ’H’ i HU-HISTMARK för HU-ERENDETYP = ’BAS’ förekommer vid korrigering på historiskt ärende. BAS aviseringen skrivs trots den historiska markeringen från gällande uppgifter.
    ('POSTTYP',       66,  69),  # Avser typ av post, uppgifterna är samlade under olika typer för att motsvara Bolagsverkets handlägning/datalagring
    ('FIRMA',         69, 269),  # Företagsnamn (firma)
    ('FIRMREGÅR',    269, 273),  # Företagsnamnets registreringsår
    ('FIRMREGDAT',   269, 277),  # Företagsnamnets registreringsdatum
    ('LAGERBOLAG',   277, 278),  # Markering om företaget är ett sk lagerbolag. Värde J/blank
    ('FIRMAMARK',    278, 279),  # Markering om att firma ändrats. Värde: 1/blank
    ('KONVMARK',     279, 284),  # Markering om att företaget är manuellt konverterat i företagsregistret. Värde: KONVM/blank
    ('REGLAN',       284, 286),  # Företagets registreringslän
    ('SKYDDSLAN',    286, 349),  # Företagsnamnets skyddslän + Markering för typ av skyddsregistrering. 3 pos * 21 ggr (= 63 pos)
    # ('SKYDDSLAN',     286, 288),  # Företagsnamnets skyddslän. 2 pos * 21 ggr (= 42 pos)
    # ('SKYDDSLANMARK', 288, 289),  # Markering för typ av skyddsregistrering. Värde: S/U/J/blank. (S=befintligt skyddslän, U=upphört skyddslän, J=nytt skyddslän). 1 pos * 21 ggr (= 21 pos)
]


def main():
    output = csv.writer(sys.stdout, delimiter=';')
    titles = [title for title, _, _ in RECORDS]
    output.writerow(titles)
    rectype_ix = titles.index('POSTTYP')
    company_ix = titles.index('OBJTYP')
    for line in fileinput.input(mode='rb'):
        line = line.decode('iso-8859-15')
        try:
            row = [line[i:j].strip(' \x00') for _, i, j in RECORDS]
            if row[rectype_ix] == '800' and row[company_ix] != 'E':
                # Endast posttyp 800 är av intresse, och
                # vi vill inte ha några enskilda firmor
                output.writerow(row)
        except ValueError:
            # Några rader / poster följer inte strukturen i RECORDS
            pass


if __name__ == '__main__':
    main()
