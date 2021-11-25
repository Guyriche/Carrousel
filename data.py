import requests
import pandas as pd

url = 'https://data.rennesmetropole.fr/explore/dataset/export-api-parking-citedia/download/?format=json&timezone=Europe/Berlin&lang=fr'
fname = 'dataset.json'

reponse = requests.get(url)
with open(fname, 'wb') as f:
    f.write(reponse.content)

df = pd.read_json(fname)
df.to_json(fname)
print(df)