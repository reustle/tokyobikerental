#!/usr/bin/env python3

import json
import codecs
from pprint import pprint

full_list = []

# Docomo File
handle = codecs.open('docomo-ports.json', 'r', 'utf-8')
c = handle.read()
c = json.loads(c)
handle.close()

# Gist File
handle = open('gist-data.geojson', 'r')
c2 = handle.read()
c2 = json.loads(c2)['features']
handle.close()

# Combine

output = json.dumps({ 'features' : c+c2 })

handle = open('results.geojson','w+')
handle.write(output)
handle.close()

