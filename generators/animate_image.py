from moviepy.editor import ImageClip
import os

def animar_imagem(caminho_imagem, caminho_saida_video, duracao=8):
    clipe = ImageClip(caminho_imagem, duration=duracao)
    clipe = clipe.resize(height=720)
    clipe = clipe.set_position('center').fadein(1).fadeout(1)
    clipe.write_videofile(caminho_saida_video, fps=24)
