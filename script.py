#!/usr/local/bin/python
# Run script once to convert the .MOV video files into audio mp3 files

import moviepy.editor as mp


def main():
    clip = mp.VideoFileClip("a_7_1_2.MOV")
    clip.audio.write_audiofile("a_7_1_2.mp3")


if __name__ == '__main__':
    main()
