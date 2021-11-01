import os
from os import listdir
from os.path import isfile, join

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

import time
startTime = time.perf_counter()
cwd = 'Z:\\eivholt\\RGS'
# r=root, d=directories, f = files
fileCount, mp3Count = 0, 0
totalRuntimeSecs = 0
for r, d, f in os.walk(cwd):
    for file in f:
        fileCount += 1
        if file.endswith(".mp3"):
            print()
            mp3Count += 1
            filePath = os.path.join(r, file)
            #print(file)
            audio = MP3(filePath, ID3=EasyID3)
            try:
                print(audio["title"])
            except KeyError:
                print(file)
            totalRuntimeSecs += audio.info.length
            print(round(audio.info.length/60, 2), "minutes")

print("File/MP3 count:", fileCount, "/", mp3Count)
print("Audio runtime total:")
#print(round(totalRuntimeSecs/60, 1), "minutes.")
print(round(totalRuntimeSecs/60/60, 2), "hours.")
print("Elapsed:", round(time.perf_counter() - startTime, 1), "s")