from telegram import Update
from telegram.ext import *
from openai_service import extrair_dados
from mapbox_service import calcular_distancia_por_cidade
from freight import calcular_frete
from pix_service import gerar_pix
from gerar_pdf import gerar_pdf
from storage import salvar

TOKEN = "TELEGRAM_TOKEN"

async def calcular(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dados = extrair_dados(update.message.text)
    dist, tempo = calcular_distancia_por_cidade(
        dados["cidade_origem"],
        dados["cidade_destino"]
    )
    valor = calcular_frete(dist, dados["tipo_veiculo"])

    registro = {**dados, "distancia": dist, "tempo": tempo, "valor": valor}
    salvar(registro)

    pdf = "orcamento.pdf"
    gerar_pdf(registro, pdf)

    await update.message.reply_text(
        f"🚚 FRETE\n💰 R$ {valor}\n\n{gerar_pix(valor)}"
    )
    await update.message.reply_document(open(pdf, "rb"))

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, calcular))
    app.run_polling()

if __name__ == "__main__":
    main()
