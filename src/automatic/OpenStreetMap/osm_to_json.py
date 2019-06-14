import osmium
import json


class Handler(osmium.SimpleHandler):
    def __init__(self):
        osmium.SimpleHandler.__init__(self)
        self.data = {'ways': [], 'nodes': []}

    def node(self, n):
        name = n.tags.get('name')
        place = n.tags.get('place')
        if name and place:
            self.data['nodes'].append({
                'name': name,
                'place': place,
                'lon': n.location.lon,
                'lat': n.location.lat
            })

    def way(self, w):
        name = w.tags.get('name')
        # possibly also check w.is_closed() to avoid things 
        # that aren't roads (but what about roads that are loops?)
        if name:
            self.data['ways'].append(name)


if __name__ == '__main__':
    h = Handler()
    h.apply_file("sweden-latest.osm.pbf")
    with open('ways.json', 'w') as fp:
        json.dump(h.data['ways'], fp, indent=2)
    with open('places.json', 'w') as fp:
        json.dump(h.data['nodes'], fp, indent=2)

