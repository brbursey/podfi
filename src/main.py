from pydub import AudioSegment
from tqdm import tqdm
import os

def main():
    print("greetings")
    merge()


def merge():
    '''Lets add all the lofi songs together with AudioSegment'''
    new_song = AudioSegment.empty()

    for song in os.listdir("lofi_songs"):
        lofi = AudioSegment.from_file(os.path.abspath("lofi_songs/" + song), format="mp3")
        new_song += lofi

    new_song.export("playlist/test.mp3",
        tags={"album": "The Tests", "artist": "Podfi 0"},
        cover="krabbs.png")


if __name__ == "__main__":
    main()