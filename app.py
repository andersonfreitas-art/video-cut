#######################################################
####  BY ANDERSON FREITAS - FREITAS0129@GMAIL.COM  ####
#######################################################

from moviepy.editor import VideoFileClip, concatenate_videoclips


# Função para cortar um trecho do vídeo e salvar em um arquivo separado com vinheta e transição de fade
def cortar_video_com_vinheta(
    input_path, output_path, start_time, end_time, vinheta_path, fade_duration=1
):
    try:
        # Carrega o vídeo e corta o trecho especificado
        video = VideoFileClip(input_path).subclip(start_time, end_time)

        # Carrega a vinheta
        vinheta = VideoFileClip(vinheta_path)

        # Adiciona fade-out ao vídeo cortado e fade-in na vinheta
        video = video.crossfadeout(fade_duration)
        vinheta = vinheta.crossfadein(fade_duration)

        # Concatena o vídeo cortado com a vinheta com transição de fade
        video_final = concatenate_videoclips([video, vinheta], method="compose")

        # Salva o vídeo final
        video_final.write_videofile(output_path, codec="libx264")
        print(f"Arquivo salvo com sucesso: {output_path}")
    except Exception as e:
        print(f"Erro ao processar o vídeo: {e}")


# Caminho do vídeo original (use caminhos absolutos se necessário)
input_video = "video_completo.mp4"

# Caminho da vinheta (use caminhos absolutos se necessário)
vinheta_video = "vinheta.mp4"

# Lista de cortes a serem feitos (inicio, fim) no formato (hh, mm, ss)
cortes = [
    ((0, 22, 37), (0, 24, 30)),
    ((0, 26, 57), (0, 28, 36)),
    ((0, 29, 25), (0, 31, 40)),
    ((0, 35, 54), (0, 38, 33)),
    ((0, 38, 48), (0, 40, 48)),
    ((0, 44, 9), (0, 46, 39)),
    ((0, 55, 50), (0, 58, 22)),
]

# Duração do fade em segundos
fade_duration = 1  # ajuste conforme necessário

# Realiza os cortes, adiciona a vinheta e salva em arquivos separados
for i, (start, end) in enumerate(cortes):
    output_video = f"corte_{i+1}.mp4"
    cortar_video_com_vinheta(
        input_video, output_video, start, end, vinheta_video, fade_duration
    )

print("Cortes com vinheta e transição de fade concluídos com sucesso.")
