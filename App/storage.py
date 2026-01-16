import json, datetime

ARQ = "historico.json"

def salvar(dados):
    dados["data"] = str(datetime.datetime.now())
    try:
        hist = json.load(open(ARQ))
    except:
        hist = []
    hist.append(dados)
    json.dump(hist, open(ARQ, "w"), indent=2)
