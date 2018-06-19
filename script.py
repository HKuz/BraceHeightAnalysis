#!/usr/local/bin/python
# Run script once to convert the .MOV video files into audio mp3 files

import os
import moviepy.editor as mp


def main():
    source_dir = "./SourceFiles/"
    for filename in os.listdir(source_dir):
        print(filename)
        full_path = os.path.abspath(source_dir + filename)
        clip = mp.VideoFileClip(full_path)
        clip.audio.write_audiofile(full_path[:-3] + "mp3")


if __name__ == '__main__':
    main()
