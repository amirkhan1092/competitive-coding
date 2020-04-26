import youtube_dl
import os

y = {}

path = 'C:/Users/amirkhan/Desktop'
os.chdir(path)

url = 'https://youtu.be/FSB9ZOPU7BE?list=RDFSB9ZOPU7BE'

with youtube_dl.YoutubeDL(y) as ydl:
    print('downloading... '+ url)
    ydl.download([url])
print('downloaded')