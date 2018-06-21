# Bow Brace Height Tuning Analysis

This analysis uses Python to compare the recorded sound differences shooting my traditional recurve bow at different brace heights within its recommended range.

Brace height is the measurement from the deepest part of the bow's riser's throat to the bow string. The manufacturer will include a recommended range for a given bow, but theoretically, there's an optimal distance that will naturally sound quieter than the others.

To find this distance, I recorded myself shooting 3 arrows each at brace heights every 1/8". I then used [FFmpeg](https://ffmpeg.org) software to convert the videos to a .WAV audio file, and Python standard library `wave` module with `matplotlib` to plot the waveforms.

## Project Dependencies

The project uses an [Anaconda](www.anaconda.com) environment to house the necessary Python packages, versions, and dependencies. These are listed in the `environment.yml` file. After you've forked and cloned this project to your local machine, you can recreate this environment in your default path by running the following command:

```bash
conda env create –f environment.yml
```

If you'd like to specify a different path, run:

```bash
conda env create –f environment.yml –p <other path>
```

To activate this environment, run:

```bash
source activate bhtune
```

A non-Python requirement is the FFmpeg software that's used to convert video files to .WAV format.


## Results

The plots showing the waveform from each video's sound track are stored in the `Plots` directory as `.pdf` files. A number of different brace heights generated plots with similar amplitudes, so there was no clear "winner". However, I chose the 8 and 1/8 measurement since it was consistently near the lowest values for each shot.


