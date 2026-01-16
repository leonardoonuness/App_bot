from openai import OpenAI
import json

# ⚠️ APENAS PARA TESTE – depois passamos para variável de ambiente
client = OpenAI(
    api_key="<OPENAI_API_KEY>"
)

def extrair_dados(texto_usuario):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Extraia e retorne SOMENTE um JSON válido com as chaves: "
                    "cidade_origem, cidade_destino, tipo_veiculo. "
                    "Não escreva nada fora do JSON."
                )
            },
            {"role": "user", "content": texto_usuario}
        ],
        temperature=0
    )

    conteudo = response.choices[0].message.content.strip()
    return json.loads(conteudo)
