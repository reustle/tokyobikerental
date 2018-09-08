#!/usr/bin/env python3

from pathlib import Path
import json
import codecs
from pprint import pprint

port_list = []

pathlist = Path('docomo/').glob('*.json')
for path in pathlist:
    # For every json file
    
    # Read the contents
    handle = codecs.open(str(path), 'r', 'utf-8-sig')
    c = handle.read()
    handle.close()
    
    # Parse the json
    json_data = json.loads(c)
    
    for port in json_data:
        #print(port['name'])
        port_list.append({
            "type": "Feature",
            "properties": {
              "name": "Docomo: " + port['name'],
              "type": "share",
              "slug": "docomo"
            },
            "geometry": {
              "type": "Point",
              "coordinates": [
                port['lng'],
                port['lat']
              ]
            }
        })

handle = open('docomo-ports.json','w')
handle.write(json.dumps(port_list))
handle.close()

