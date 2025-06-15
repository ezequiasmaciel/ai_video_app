# generators/tts_generator.py

from gtts import gTTS
import os

def gerar_audio(texto: str, idioma: str = "pt", nome_arquivo: str = "voz.mp3") -> str:
    """Gera um arquivo de áudio MP3 a partir de um texto usando gTTS."""
    if not texto.strip():
        raise ValueError("Texto vazio fornecido para narração.")
    
    tts = gTTS(text=texto, lang=idioma)
    tts.save(nome_arquivo)
    return nome_arquivo
