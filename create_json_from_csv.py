"""
Python3-skript för att skapa JSON-databaser från CSV-filer.

Skriptet skapar följande databaser:
- `json/bolagsverket.json`, från `src/automatic/Bolagsverket/bolagsinformation.csv`
- `json/personnamn-scb.json`, från `src/automatic/SCB/personnamn-2017-12-31/*.csv`
- `json/platser-lantmateriet.json`, från `src/automatic/Lantmateriet/*.csv`

Användning:
python3 create_json_from_csv.py
"""

import csv
import json
import sys
from glob import glob


SOURCEDIR = 'src/'
TARGETDIR = 'json/'

STR = lambda col: (lambda row: row[col].strip())
INT = lambda col: (lambda row: int(row[col].replace(' ', '') or 0))

CSVINFO = {}
CSVINFO['bolagsverket'] = [
    ('bolag', 'automatic/Bolagsverket/bolagsinformation.csv', {
        'namn':       STR(4),
        'bolagsform': STR(0),
        'regår':      INT(5),
        'länskod':    INT(10),
    }),
]
CSVINFO['personnamn-scb'] = [
    ('efternamn', 'automatic/SCB/personnamn-2017-12-31/scb-efternamn.csv', {
        'namn': STR(0),
        'antal': INT(1),
    }),
    ('förnamn-kvinnor', 'automatic/SCB/personnamn-2017-12-31/scb-fornamn-kvinnor.csv', {
        'namn': STR(0),
        'antal': INT(1),
    }),
    ('förnamn-män', 'automatic/SCB/personnamn-2017-12-31/scb-fornamn-man.csv', {
        'namn': STR(0),
        'antal': INT(1),
    }),
    ('tilltalsnamn-kvinnor', 'automatic/SCB/personnamn-2017-12-31/scb-tilltalsnamn-kvinnor.csv', {
        'namn': STR(0),
        'antal': INT(1),
    }),
    ('tilltalsnamn-män', 'automatic/SCB/personnamn-2017-12-31/scb-tilltalsnamn-man.csv', {
        'namn': STR(0),
        'antal': INT(1),
    }),
]
CSVINFO['platser-lantmateriet'] = [
    ('fjäll', 'automatic/Lantmateriet/Fjallinformation-*.csv', {
        'namn': STR(0),
        'kategori': STR(2),
        'kategorikod': INT(1),
    }),
    ('översikt', 'automatic/Lantmateriet/Oversikt-*.csv', {
        'namn': STR(0),
        'kategori': STR(2),
        'kategorikod': INT(1),
    }),
    ('sverige', 'automatic/Lantmateriet/Sverigekartor-*.csv', {
        'namn': STR(2),
        'kategori': STR(1),
        'kategorikod': INT(0),
    }),
    ('terräng', 'automatic/Lantmateriet/Terrangkartan-*.csv', {
        'namn': STR(2),
        'kategori': STR(1),
        'kategorikod': INT(0),
    }),
    ('vägar', 'automatic/Lantmateriet/Vagkartan-*.csv', {
        'namn': STR(0),
        'kategori': STR(3),
        'kategorikod': INT(2),
    }),
]

SKIPNAMES = {
    'bolagsverket':         ['FIRMA'],
    'platser-lantmateriet': ['DISTRNAMN', 'TEXT'],
    'personnamn-scb':       ['Förnamn', 'Efternamn', 'Tilltalsnamn'],
}


def create_database(csvinfo, skipnames):
    dbase = {}
    for (db_lbl, infiles, template) in csvinfo:
        for inf in glob(SOURCEDIR + infiles):
            print("  %s --> %s" % (inf, db_lbl), file=sys.stderr)
            with open(inf) as IN:
                for row in csv.reader(IN, delimiter=';'):
                    name = template['namn'](row)
                    if name and all(skip not in name for skip in skipnames):
                        dbase.setdefault(db_lbl, []).append({
                            lbl: column(row) for (lbl, column) in template.items()
                        })
    return dbase


def main():
    for dbname in CSVINFO:
        filename = TARGETDIR + dbname + '.json'
        print("Building json database %s" % (filename,), file=sys.stderr)
        dbase = create_database(CSVINFO[dbname], SKIPNAMES[dbname])
        with open(filename, "w") as OUT:
            json.dump(dbase, OUT, indent=4)


if __name__ == '__main__':
    main()
