#!/usr/local/bin/python
# Script to convert original .MOV video files to both .mp3 and .WAV audio files

import os
import subprocess
import moviepy.editor as mp


def main():
    # command = "ffmpeg -i C:/test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"
    # subprocess.call(command, shell=True)
    mov_to_mp3()


def mov_to_mp3():
    """
    Uses moviepy library to convert original .MOV files to .mp3 audio files
    """
    source_dir = "./SourceFiles/"
    source_path = os.path.abspath(source_dir) + "/"
    dest_path = os.path.abspath("./MP3Files") + "/"
    for filename in os.listdir(source_dir):
        print(filename)
        if filename == ".DS_Store":
            continue
        clip = mp.VideoFileClip(source_path + filename)
        clip.audio.write_audiofile(dest_path + filename[:-3] + "mp3")


if __name__ == '__main__':
    main()
