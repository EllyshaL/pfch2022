import requests
import json
import csv

base_url = "https://www.loc.gov/film-and-videos/?q=feminist&fo=json"
payload = {
 'q' : 'feminist', 'feminism'
 'rows' : 1000
}

r = requests.get(base_url, params=payload)
data = json.loads(r.text)
with open('feminism_results.csv', 'w') as file:
 
 writer = csv.writer(file)
 
 result_header = ["date", "shelf_id", "title", "original_format", "item_summary", "access_res"]
 writer.writerow(result_header)
 
 for item in data["content"]["results"]:

     # meow = item["item"]
     purr = []
     purr.append(item["date"])
     purr.append(item["shelf_id"])
     purr.append(item["title"])
     purr.append(item["original_format"])
     purr.append(item["item"]["summary"])
     purr.append(item["access_restricted"])

     for resource in item["resources"]:
         purr.append(resource)

     print(purr)
     writer.writerow(purr)
