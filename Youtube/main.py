# Projet "Youtube Downloader" 
 
# module : pytube 
 
# -*- coding: utf-8 -*-

from pytube import Youtube

url = ""
youtube_video= Youtube(url)

print(youtube_video.title)
print(youtube_video.views)

