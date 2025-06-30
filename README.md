# Reinforce

Simple python script which concatenates audio files from Anki flashcards to aid with passive reinforcement.

# Usage

1. In Anki, export selected notes as .txt into input folder located in the same directory as the script.
2. Edit the script to specify the path to your Anki collection's media folder.
3. Open a terminal and navigate to the directory containing the script, then run "python reinforce.py" (or possibly "python3 reinforce.py")
4. Upon completion, the output will be located at output/output.mp3.

# Dependencies

pydub

# To do

- [x]   Basic functionality
- [ ]    Account for other audio formats
- [ ]    Example input and output files
- [ ]    Config file to contain user variables
- [ ]    Settings and customizability
- [ ]    Anki plugin
