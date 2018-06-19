#!/usr/local/bin/python
# Script to convert original .MOV video files to both .MP3 and .WAV audio files

import os
import subprocess
# import moviepy.editor as mp


def main():
    # Create wav files from videos (run once)
    mov_to_wav()

    # Create mp3 files from videos (run once)
    # mov_to_mp3()


def mov_to_wav():
    """
    Uses subprocess to run ffmpeg commands in the shell to convert original
        .MOV files to .WAV audio files
    """
    source_dir = "./SourceFiles/"
    source_path = os.path.abspath(source_dir) + "/"
    dest_path = os.path.abspath("./WAVFiles") + "/"

    for filename in os.listdir(source_dir):
        print(filename)
        if filename == ".DS_Store":
            continue

        src_file = source_path + filename
        dest_file = dest_path + filename[:-3] + ".wav"
        command = "ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {}".format(
            src_file, dest_file)
        subprocess.call(command, shell=True)


def mov_to_mp3():
    """
    Uses moviepy library to convert original .MOV files to .MP3 audio files
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
