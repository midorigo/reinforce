import argparse
import os
import re
from pydub import AudioSegment

parser = argparse.ArgumentParser(prog='reinforce', description='Concatenate audio files from Anki cards')
parser.add_argument('filename', default='input/Selected Notes.txt', help='File to operate on, e.g. \"input/Selected Notes.txt\"')
parser.add_argument('-b', '--base', default=os.environ.get("HOME")+'/.local/share/Anki2/User 1/collection.media', help='Path of collection.media directory; default=\"~/.local/share/Anki2/User 1/collection.media/\"')
parser.add_argument('-s', '--silence', default=3000, type=int, help='Length of silence to insert between audio clips in ms; default=3000')
args = parser.parse_args()

output_path = "output/Selected Notes.mp3"

with open(args.filename, 'r', encoding='utf-8') as input:
    audio_files = []
    for line in input:
        audio_files.extend(re.findall(r"\[sound:(.*?)\]", line))
    concatenated = AudioSegment.empty()
    silence = AudioSegment.silent(duration=args.silence)
    for filename in audio_files:
        file_path = args.base + filename
        audio = AudioSegment.from_file(file_path, format="mp3") + silence
        concatenated += audio
        print(file_path)
    concatenated.export(output_path, format="mp3")
    print(f"File written to {os.getcwd()}/{output_path}") 
