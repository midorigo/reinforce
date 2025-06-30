import os
import re
from pydub import AudioSegment

#User variables
input_path = "input/Selected Notes.txt"
media_path = "/home/wold/Sync/Anki/Anki2/User 1/collection.media/"
silence_interval_ms = 3000

with open(input_path, 'r', encoding='utf-8') as input:
    audio_files = []
    for line in input:
        audio_files.extend(re.findall(r"\[sound:(.*?)\]", line))
    concatenated = AudioSegment.empty()
    silence = AudioSegment.silent(duration=silence_interval_ms)
    for filename in audio_files:
        file_path = media_path + filename
        print(file_path)
        audio = AudioSegment.from_file(file_path, format="mp3") + silence
        concatenated += audio
    concatenated.export("output/output.mp3", format="mp3")
