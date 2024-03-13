# Projet "Youtube Downloader" 
 
# module : pytube 
 
# -*- coding: utf-8 -*-

from pytube import YouTube

url = "https://www.youtube.com/watch?v=9bZkp7q19f0"

youtube_video = YouTube(url)
print("TITRE: " + youtube_video.title)
print("NB VUES:", youtube_video.views)

print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print("  ", stream)

# stream = youtube_video.streams.get_by_itag(18)
stream = youtube_video.streams.get_highest_resolution()
print("Steam vidéo: ", stream)
print("Téléchargement...")
stream.download()
print("OK")
