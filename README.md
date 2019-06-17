# UNameIT

"Universal Names and miscellaneous entities (for) Information Technology"

This repo contains several (open) databases containing information about names (e.g., person names, geographical names, company names, etc).

### Large file storage

This repo uses [Git LFS](https://git-lfs.github.com/) to store large files. To get the files and run the scripts correctly, install Git LFS and then do this inside your clone of the repo:

```sh
git lfs install
git lfs pull
```

### No sensitive information!

Since this repo is not hosted at GU, it is important that we do not store any sensitive information here. Sensitive information are, e.g., any information that can be connected to an individual person.

### Source files

All original database sources should reside in the `src` directory. This is divided into:

- `automatic`: here are databases that are downloaded from other places, or automatically created in some way
- `manual`: here are databases that we build and update manually

Every data source should have a separate directory in `src/automatic` or `src/manual`, and there must be a readme file detailing how the sources have been obtained and what scripts have been used.

### Derived JSON databases

Our preferred result database format is JSON, and they should be automatically created by scripts. The resulting JSON databases should be in the `json` directory.

## Contents

Here are very short descriptions of all the resources in this repository.

### Bolagsverket

- converted by: [create_json_from_csv.py](create_json_from_csv.py)
- source CSV: [bolagsinformation.csv](src/automatic/Bolagsverket/bolagsinformation.csv)
- target JSON: [bolagsverket.json](json/bolagsverket.json)
- more information: [Bolagsverket README](src/automatic/Bolagsverket/README.md)

**Note**: The source file `bolagsinformation.csv` is not the original, but it is automatically converted from the original files by [create_csv.py](src/automatic/Bolagsverket/create_csv.py). 

### Lantmäteriet

- converted by: [create_json_from_csv.py](create_json_from_csv.py)
- source CSVs: [Lantmateriet/*.csv](src/automatic/Lantmateriet)
- target JSON: [platser-lantmateriet.json](json/platser-lantmateriet.json)
- more information: [Lantmäteriet README](src/automatic/Lantmateriet/README.md)

### OpenStreetMap

- copied by: [copy_jsons.sh](copy_jsons.sh)
- source JSONs: [places.json](src/automatic/OpenStreetMap/places.json) and [ways.json](src/automatic/OpenStreetMap/ways.json)
- target JSONs: [osm-places.json](json/osm-places.json) and [osm-ways.json](json/osm-ways.json)
- more information: [OpenStreeMap README](src/automatic/OpenStreetMap/README.md)

### SCB Personnamn

- converted by: [create_json_from_csv.py](create_json_from_csv.py)
- source CSVs: [SCB/personnamn-2017-12-31/*.csv](src/automatic/SCB/personnamn-2017-12-31)
- target JSONs: [personnamn-scb.json](json/personnamn-scb.json)
- more information: [SCB personnamn README](src/automatic/SCB/personnamn-2017-12-31/README.md)

**Note**: the source CSV files are not the original, but were saved from the Excel file in the directory [personnamn-2017-12-31/original](src/automatic/SCB/personnamn-2017-12-31/original). 

### SCB Öppna data

- currently not copied to the `json` directory, because the `personnamn-2017-12-31` contains the approximately the same information
- source JSONs: [SCB/oppna-data/*.json](src/automatic/SCB/oppna-data)
- more information: [SCB öppna data README](src/automatic/SCB/oppna-data/README.md)

### Svenskaplatser.se

- converted by: [create_json_from_csv.py](create_json_from_csv.py)
- source CSV: [streets.csv](src/automatic/Svenskaplatser/streets.csv)
- target JSON: [svenskaplatser.json](json/svenskaplatser.json)
- more information: [Svenskaplatser README](src/automatic/Svenskaplatser/README.md)

**Note**: We don't know the license of svenskaplatser.se, and if/what we are allowed to do with the data. 




