# Data från Bolagsverket
Information om företag och organisationer i Sverige. Data kommer från Bolagsverket, genom ett upprättat avtal mellan dem och Språkbanken, i april 2019.

Originaldatabasen innehåller känslig personlig information, så den ligger inte med i detta repo. Den härledda databasen är `bolagsinformation.csv`, och den har skapats på följande sätt:

    python3 create_csv.py original-2019-04-30/*.txt > bolagsinformation.csv

(om vi antar att originalfilerna finns i katalogen `original`)


## Posttyper
Denna information är hämtad från `postbeskrivning.pdf`.

### Teckenkodning
Teckenkodning som används i originalfilerna: ISO 8859-15

### Posttyp 100 "startpost"

```
HU-SEKVNR        Heltal    1-8   Sekvensnummer för varje skapad fil i aviseringsregistret. Posttyp 100 skrivs en gång i filen (början)
HU-UTSKRDAT      Heltal    9-16  Datum då filen skrivs i aviseringssystemet
HU-KUNDNR        Heltal   17-26  Kundnummer
HU-UTSKRTID      Heltal   27-34  Tid då filen skrivs i aviseringssystemet
FILLER           Text     35-66  Utfyllnad
HU-POSTTYP100    Heltal   67-69  Posttyps identitet. Se resp postbeskrivning FFREG, FIR, KKREG, NFREG, PTREG, UNIREG, VPREG
```

### Alla posttyper

```
HU-POSTBETECK    Text      1-6   Postbeteckning = UNIREG. Avisering från AB-registret, Handels- och föreningsregistren, Bank- o försäkringsregistret HU-POSTID (HU-AVISERPOS T) skrivs i början på varje rad i filen (före respektive posttyp).
HU-UTSKRIFTDAT   Heltal    7-14  Datum då posten skrivs i aviseringsregistret 
HU-ERENDEREGDAT  Heltal   15-30  Ärendets registreringsdatum och tidpunkt hos Bolagsverket 
HU-OBJTYP        Text     31-35  Objekttyp/företagsform/registerspecifikt 
HU-SEK           Text     36-36  Sekel, värde: 9/8/blank. 9=1900, 8=1800 
HU-ORGNR         Heltal   37-46  Objektets organisationsnummer eller personnummer 
HU-LOPNR         Heltal   47-51  Löpnummer (identitet). Används för företag som har flera näringsdrivande företag registrerade på samma organisationsnummer eller per sonnummer. Avser: E, I, S, TSF
HU-DINR          Heltal   52-58  Ärendets ärendenummer
HU-DINRAR        Heltal   59-62  Ärendenumrets årtal
HU-ERENDETYP     Text     63-65  Markering av ärendetyp. Värde: NYB/AND/KOR/BAS
HU-HISTMARK      Text     66-66  Markering om ärendet är ett historiskt ärende. Värde: H/blank. ’H’ i HU-HISTMARK för HU-ERENDETYP = ’BAS’ förekommer vid korrigering på historiskt ärende. BAS aviseringen skrivs trots den historiska markeringen från gällande uppgifter.
HU-POSTTYP       Text     67-69  Avser typ av post, uppgifterna är samlade under olika typer för att motsvara Bolagsverkets handlägning/datalagring
HU-AVISERDATA    Text     70-400 Innehåller aviseringsuppgifter enligt respektive posttypsbeskrivning nedan. HU-AVISERDATA är detaljer enligt resp posttyp, ex 800, 804 osv
```

### Posttyp 800 "firma"

```
HU-FIRMA         Text     70-269  Företagsnamn (firma)
HU-FIRMREGDAT    Heltal  270-277  Företagsnamnets registreringsdatum
HU-LAGERBOLAG    Text    278-278  Markering om företaget är ett sk lagerbolag. Värde J/blank
HU-FIRMAMARK     Text    279-279  Markering om att firma ändrats. Värde: 1/blank
HU-KONVMARK      Text    280-284  Markering om att företaget är manuellt konverterat i företagsregistret. Värde: KONVM/blank
HU-REGLAN        Heltal  285-286  Företagets registreringslän
HU-SKYDDSLAN     Heltal  287-288  Företagsnamnets skyddslän. 2 pos * 21 ggr (= 42 pos)
HU-SKYDDSLANMARK Text    289-289  Markering för typ av skyddsregistrering. Värde: S/U/J/blank. (S=befintligt skyddslän, U=upphört skyddslän, J=nytt skyddslän). 1 pos * 21 ggr (= 21 pos)
FILLER           Text    290-400
```

## Förkortningar som används i posterna

### Företagstyper (HU-OBJTYP)

```
EGTS Europeiska Grupperingar för Territoriellt Samarbete (EGTS) 
EK   Ekonomisk förening
E    Enskild näringsidkare
EB   Enkla bolag
SE   Europabolag
SCE  Europakooperativ
EEIG Europeisk ekonomisk intressegruppering 
FAB  Försäkringsaktiebolag
FOF  Försäkringsförening
FL   Filial
HB   Handelsbolag
I    Ideell förening som bedriver näring 
KB   Kommanditbolag
KHF  Kooperativ hyresrättsförening
MB   Medlemsbank
SB   Sparbank
S    Stiftelse som bedriver näring
SF   Sambruksförening
TSF  Trossamfund
OFB  Ömsesidigt försäkringsbolag
```

### Länskoder

```
01  AB  Stockholms län
03  C   Uppsala län
04  D   Södermanlands län
05  E   Östergötlands län
06  F   Jönköpings län
07  G   Kronobergs län
08  H   Kalmar län
09  I   Gotlands län
10  K   Blekinge län
12  M   Skåne län
13  N   Hallands län
14  O   Västra Götalands län
17  S   Värmlands län
18  T   Örebro län
19  U   Västmanlands län
20  W   Dalarnas län
21  X   Gävleborgs län
22  Y   Västernorrlands län
23  Z   Jämtlands län
24  AC  Västerbottens län
25  BD  Norrbottens län
```
