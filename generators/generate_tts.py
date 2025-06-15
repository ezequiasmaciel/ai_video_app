def gerar_audio_coqui(texto, caminho_audio):
    # Aqui entra a lógica com Coqui TTS (exemplo placeholder)
    with open(caminho_audio, "wb") as f:
        f.write(b"AUDIO FICTICIO PARA: " + texto.encode())
