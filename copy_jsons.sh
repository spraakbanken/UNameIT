
# OpenStreetMap: {places,ways}.json --> osm-{places,ways}.json
for f in places ways; do
    cp src/automatic/OpenStreetMap/$f.json json/osm-$f.json
done
