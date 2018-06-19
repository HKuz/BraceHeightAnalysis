#!/usr/local/bin/python
# Script to read and plot the mp3 file waveforms

import os
import wave
import matplotlib.pyplot as plt
import numpy as np


def main():
    source_dir = "./WAVFiles/"

    plt.figure(figsize=(12, 12))
    index = 1
    for filename in os.listdir(source_dir):
        if filename == ".DS_Store":
            continue

        with wave.open(source_dir + filename, "rb") as spf:
            # Extract Raw Audio from File
            signal = spf.readframes(-1)
            signal = np.fromstring(signal, "Int16")
            fs = spf.getframerate()  # sampling frequency

        time = np.linspace(0, len(signal) / fs, num=len(signal))

        plt.subplot(3, 3, index)
        plt.tight_layout()
        plt.title("Signal: {}".format(filename[2:-4]))
        plt.axis(ymin=5000, ymax=9000)
        plt.plot(time, signal)
        index += 1

    plt.savefig("SignalWavePlotsTopTight.pdf")
    plt.show()
    plt.clf()


if __name__ == '__main__':
    main()
