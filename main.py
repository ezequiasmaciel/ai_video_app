# main.py

import streamlit as st
import os
from dotenv import load_dotenv
from generators.tts_generator import gerar_audio
from generators.download_and_edit_stock import baixar_video, cortar_video

# Carrega variáveis de ambiente
load_dotenv()

# Configurações da página
st.set_page_config(page_title="Criador de Vídeos com IA", layout="centered")
st.title("🎬 Criador de Vídeos para YouTube com Inteligência Artificial")
st.markdown("Crie vídeos automatizados com base em um roteiro, usando imagens, vídeos de acervo e narração por IA.")

# Entrada do roteiro
roteiro = st.text_area("📜 Cole seu roteiro abaixo:", height=300)

# Escolha do tipo de vídeo
modo = st.selectbox("🎞️ Tipo de vídeo desejado:", ["Com imagens IA", "Com vídeos de acervo"])

# Escolha do idioma para narração
idioma = st.selectbox("🌍 Idioma da narração:", ["pt", "en", "es"], index=0)

# Botão para gerar narração
if st.button("🎤 Gerar Narração com gTTS"):
    if not roteiro.strip():
        st.warning("⚠️ Por favor, insira um roteiro antes de gerar o áudio.")
    else:
        try:
            st.info("🧠 Gerando narração humanizada com gTTS...")
            nome_audio = "voz.mp3"
            caminho_audio = gerar_audio(roteiro, idioma=idioma, nome_arquivo=nome_audio)
            st.success("✅ Narração gerada com sucesso!")
            st.audio(caminho_audio, format="audio/mp3")
        except Exception as e:
            st.error(f"❌ Erro ao gerar a narração: {str(e)}")

# Exemplo extra: manipulação de vídeos de acervo

