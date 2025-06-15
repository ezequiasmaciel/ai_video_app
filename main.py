import streamlit as st
from dotenv import load_dotenv
import os
from scrapers.fetch_stock_videos import buscar_video_pexels
from generators.download_and_edit_stock import baixar_video, cortar_video
from generators.generate_tts import gerar_audio_coqui
from generators.generate_video import gerar_video, unir_clipes_em_video_final

load_dotenv()

st.set_page_config(page_title="Criador de Vídeos com IA", layout="wide")
st.title("🎬 Criador de Vídeos YouTube com Inteligência Artificial")

roteiro = st.text_area("✍️ Cole seu roteiro aqui:")
modo = st.radio("Selecione o tipo de vídeo:", ["Imagens IA", "Vídeos de Acervo Gratuito"])

if st.button("Gerar Vídeo") and roteiro:
    cenas = [linha for linha in roteiro.strip().split("\n") if linha]

    for i, cena in enumerate(cenas):
        st.write(f"🎬 Cena {i+1}: {cena}")
        caminho_video_final = f"saida/cena_{i}.mp4"
        caminho_audio = f"saida/cena_{i}.mp3"

        if modo == "Vídeos de Acervo Gratuito":
            video_url = buscar_video_pexels(cena)
            if video_url:
                caminho_video_raw = f"saida/raw_cena_{i}.mp4"
                baixar_video(video_url, caminho_video_raw)
                cortar_video(caminho_video_raw, caminho_video_final, duracao=8)
            else:
                st.warning(f"Nenhum vídeo encontrado para a cena {i+1}.")
                continue
        else:
            continue

        gerar_audio_coqui(cena, caminho_audio)
        gerar_video(caminho_video_final, caminho_audio, caminho_video_final)

    unir_clipes_em_video_final("saida", "saida/video_final_completo.mp4")
    st.video("saida/video_final_completo.mp4")
