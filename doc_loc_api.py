import requests
import json
base_url = "https://www.loc.gov/film-and-videos/?q=feminist&fo=json"
payload = {
 'q' : 'feminist', 'feminism'
 'rows' : 1000
}
r = requests.get(base_url, params=payload)
data = json.loads(r.text)
print(r.text)
