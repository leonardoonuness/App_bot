import os, requests

TOKEN = os.getenv("MAPBOX_TOKEN")

def geocode(cidade):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{cidade}.json"
    r = requests.get(url, params={"access_token": TOKEN, "limit": 1})
    data = r.json()
    lon, lat = data["features"][0]["center"]
    return f"{lon},{lat}"

def calcular_distancia_por_cidade(o, d):
    oc = geocode(o)
    dc = geocode(d)
    url = f"https://api.mapbox.com/directions/v5/mapbox/driving/{oc};{dc}"
    r = requests.get(url, params={"access_token": TOKEN})
    rota = r.json()["routes"][0]
    return round(rota["distance"]/1000, 2), round(rota["duration"]/60, 1)
