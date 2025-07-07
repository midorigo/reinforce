import argparse
import os
import re
from pydub import AudioSegment

parser = argparse.ArgumentParser(prog='reinforce', description='Concatenate audio files from Anki cards')
parser.add_argument('-f',
                    '--filename',
                    default='input/Selected Notes.txt',
                    help='File to operate on, e.g. \"input/Selected Notes.txt\"')
parser.add_argument('-b',
                    '--base',
                    default=os.environ.get("HOME")+'/.local/share/Anki2/User 1/collection.media',
                    help='Path of collection.media directory; default=\"~/.local/share/Anki2/User 1/collection.media/\"')
parser.add_argument('-s',
                    '--silence',
                    default=3000,
                    type=int,
                    help='Length in miliseconds of silence to insert between audio clips; default=3000')
args = parser.parse_args()

input_dir = os.getcwd() + "/input/"
if not os.path.exists(input_dir):
    os.makedirs(input_dir)
output_dir = os.getcwd() + "/output/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_name = "Reinforce.mp3"
output_path = output_dir + output_name

with open(args.filename, 'r', encoding='utf-8') as input:
    audio_files = []
    for line in input:
        audio_files.extend(re.findall(r"\[sound:(.*?)\]", line))
    concatenated = AudioSegment.empty()
    silence = AudioSegment.silent(duration=args.silence)
    for i, filename in enumerate(audio_files):
        print(f"({i + 1}/{len(audio_files)}) {filename}")
        file_path = args.base + filename
        audio = AudioSegment.from_file(file_path, format="mp3") + silence
        concatenated += audio
    concatenated.export(output_path, format="mp3")
    print(f"File written to {output_path}") 
