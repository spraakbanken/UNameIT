
Download OSM data from http://download.geofabrik.de/europe/sweden-latest.osm.pbf

On http://download.geofabrik.de/ data for the whole world is also available in pbf format, update
`osm_to_json.py` to use another file.

## How to run

1. Create a virtualenv and activate it (optional)
2. `pip install -r requirements.txt`
3. `python osm_to_json.py`

The python script creates:

- `ways.json`, all named ways. Not really much interesting metadata for ways,
   so only names are saved.
- `places.json`, all named places with longitude and latitude along with what type of place this is


