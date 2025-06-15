import requests
from moviepy.editor import VideoFileClip

def baixar_video(url, caminho_saida):
    resposta = requests.get(url)
    with open(caminho_saida, "wb") as f:
        f.write(resposta.content)

def cortar_video(caminho_entrada, caminho_saida, duracao=8):
    clipe = VideoFileClip(caminho_entrada)
    clipe_sub = clipe.subclip(0, min(duracao, clipe.duration))
    clipe_sub.write_videofile(caminho_saida, codec="libx264", audio_codec="aac")
