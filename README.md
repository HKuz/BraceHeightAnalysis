# Bow Brace Height Tuning Analysis

This project compares recorded sound differences shooting a traditional recurve bow at different brace heights within its recommended range.

Brace height is the measurement from the deepest part of the riser's throat to the bow string. Typically, the bow's manufacturer includes a recommended range of brace heights for that given bow. Theoretically, there's an optimal distance that naturally sounds quieter than the others. This is different for every bow, and can be from person to person as well.

To find the optimal brace height distance, I recorded myself saying the brace height for that round, then shooting 3 arrows each for brace heights every 1/8" from 7 1/2" to 8 1/2". I used [FFmpeg](https://ffmpeg.org) software to convert the videos to a .WAV audio file, and Python standard library `wave` module with `matplotlib` to plot the waveforms.

## Project Dependencies

The project uses an [Anaconda](www.anaconda.com) environment to manage the necessary Python packages, versions, and dependencies. These are listed in the `environment.yml` file. After forking and cloning this project to your local machine, you can recreate this environment in your default path by running the following command:

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

To deactivate the environment, run:

```bash
source deactivate
```

A non-Python requirement is the FFmpeg software that's used to convert video files to .WAV format.


## Results

The plots showing the waveform from each video's sound track are stored in the `Plots` directory as `.pdf` files. There's also a Jupyter notebook that re-creates the charts inline. A number of different brace heights generated plots with similar amplitudes, so there was no clear "winner". However, I chose the 8 1/8" measurement since it was consistently near the lowest values for each shot.
