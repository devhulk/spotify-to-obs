import os
import sys
import subprocess
import shutil
import datetime
from mutagen.mp3 import MP3
from pydub import AudioSegment

playlist = sys.argv[1]
playlist_name = "devhulk" + str(datetime.datetime.now())

p = subprocess.Popen(["spotdl", "download", playlist], cwd="./playlists")
p.wait()

# Create folder for downloaded songs
p = subprocess.Popen(["mkdir", playlist_name], cwd="./playlists")
p.wait()

# Move songs into generated playlist folder
for filename in os.listdir("./playlists"):
    f = os.path.join("./playlists", filename)
    if os.path.isfile(f) and os.path.basename != playlist_name:
        shutil.move(f, f"./playlists/{playlist_name}")


# Grab location of songs
directory = f"./playlists/{playlist_name}"

song_list = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename != ".DS_Store" :
        seg = AudioSegment.from_mp3(f)
        song_list.append(seg)

combined_music = song_list[0] 

for song in song_list[1:]:
    combined_music += song


combined_music.export(f"./{playlist_name}.mp3", format="mp3")
