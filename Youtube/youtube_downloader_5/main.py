# -*- coding: utf-8 -*-
# Projet "Youtube Downloader" 
 
# module : pytube 


from pytube import YouTube

url = "https://www.youtube.com/watch?v=9bZkp7q19f0"

BASE_YOUTUBE_URL = "https://www.youtube.com"

'''while True:
    url = input("Donnez l'url de la vidéo Youtube à télécharger: ")
    #if url[:len(BASE_YOUTUBE_URL)] == BASE_YOUTUBE_URL:
    if url.lower().startswith(BASE_YOUTUBE_URL):
        break
    print("ERREUR : Vous devez rentrer une URL de video Youtube")
'''


# vérifier que l'url commence par "https://www.youtube.com"
# si ce n'est pas le cas 
# - afficher une erreur
# - reposer la question

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Progression du téléchargement {int(percent)}%")



youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print("TITRE: " + youtube_video.title)
print("NB VUES:", youtube_video.views)

print("")
print("CHOIX DES RÉSOLUTIONS")
streams = youtube_video.streams.filter(progressive=True, file_extension='mp4')
index = 1
for stream in streams:
    print(f"{index} - {stream.resolution}")
    index += 1

while True:
    res_num = input("Choisissez la résolution: ")
    if res_num == "":
        print("ERREUR : Vous devez rentrer un nombre")
    else:
        try:
            res_num_int = int(res_num)
        except:
            print("ERREUR : Vous devez rentrer un nombre")
        else:
            if not 1 <= res_num_int <= len(streams):
                print("ERREUR : Vous devez rentrer un nombre entre 1 et", len(streams))
            else:
                break

itag = streams[res_num_int-1].itag
# print("itag: ", itag)
# 1 - 360p
# 2 - 720p
# Choisissez la résolution: 
# stream.resolution
# stream.itag

# Demander le choix de la résolution


stream = youtube_video.streams.get_by_itag(itag)
# stream = youtube_video.streams.get_highest_resolution()
# print("Steam vidéo: ", stream)
print("Téléchargement...")
stream.download()
print("OK")
