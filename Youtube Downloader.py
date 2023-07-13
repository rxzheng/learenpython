from pytube import YouTube
from sys import argv

link = argv[1]
yt = Youtube(link)

print("Title:", yt.title)
print("Views:", yt.views)

