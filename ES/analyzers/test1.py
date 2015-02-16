import requests
import json

r = requests.get('http://localhost:9200/_analyze',
             params={'analyzer':'standard'},
             data='a Text to analyze')

print json.dumps(r.json(),indent=4)

