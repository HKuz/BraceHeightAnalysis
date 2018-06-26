#!/usr/local/bin/python
# Script to read and plot the mp3 file waveforms

import os
import wave
import matplotlib.pyplot as plt
import numpy as np


def main():
    source_dir = "./WAVFiles/"

    plt.figure(figsize=(12, 12))
    plot_index = 1
    for filename in os.listdir(source_dir):
        if filename == ".DS_Store":
            continue

        with wave.open(source_dir + filename, "rb") as spf:
            # Extract Raw Audio from File
            signal = spf.readframes(-1)
            signal = np.fromstring(signal, "Int16")

            # Split the data into channels [COMMENTED OUT]
            # channels = [[] for channel in range(spf.getnchannels())]
            # for index, datum in enumerate(signal):
            #     channels[index % len(channels)].append(datum)

            # Get time from indices
            fs = spf.getframerate()  # sampling frequency
            time = np.linspace(0, len(signal) / fs, num=len(signal))
            # Channel time calculation
            # time = np.linspace(0, len(signal) / len(channels) / fs,
            #                    num=len(signal) / len(channels))

        plt.subplot(3, 3, plot_index)
        plt.tight_layout()
        plt.title("Signal: {}".format(filename[2:-4]))
        plt.axis(ymin=-9000, ymax=9000)
        plt.plot(time, signal)
        # for channel in channels:
        #     plt.plot(time, channel)
        plot_index += 1

    plt.savefig("SignalWavePlots.pdf")
    plt.show()
    plt.clf()


if __name__ == '__main__':
    main()
