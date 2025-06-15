import os
from moviepy.editor import concatenate_videoclips, VideoFileClip, AudioFileClip

def gerar_video(video_path, audio_path, output_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)
    video.write_videofile(output_path, codec="libx264", audio_codec="aac")

def unir_clipes_em_video_final(pasta_entrada, caminho_saida):
    clipes = []
    for arquivo in sorted(os.listdir(pasta_entrada)):
        if arquivo.endswith(".mp4") and arquivo.startswith("cena_"):
            clipes.append(VideoFileClip(os.path.join(pasta_entrada, arquivo)))
    if clipes:
        video_final = concatenate_videoclips(clipes)
        video_final.write_videofile(caminho_saida, codec="libx264", audio_codec="aac")
