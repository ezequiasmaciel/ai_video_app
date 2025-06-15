import requests
from PIL import Image
from io import BytesIO
import os

def gerar_imagem_dalle(texto, caminho_saida):
    # Exemplo de uso de uma API local Open Source como Stable Diffusion web API
    response = requests.post(
        "http://localhost:7860/sdapi/v1/txt2img",
        json={
            "prompt": texto,
            "steps": 20,
            "width": 768,
            "height": 432,
        }
    )
    data = response.json()
    imagem_base64 = data["images"][0]
    imagem_bytes = BytesIO(base64.b64decode(imagem_base64))
    imagem = Image.open(imagem_bytes)
    imagem.save(caminho_saida)
