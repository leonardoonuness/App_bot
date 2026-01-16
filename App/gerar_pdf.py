from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def gerar_pdf(dados, arquivo):
    c = canvas.Canvas(arquivo, pagesize=A4)
    c.drawString(50, 800, "ORÇAMENTO DE FRETE")
    y = 760
    for k, v in dados.items():
        c.drawString(50, y, f"{k}: {v}")
        y -= 20
    c.save()
