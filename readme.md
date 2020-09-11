# IMPRS Python course: word-picture verification task

This is the GIT respository for a simple word-picture verification task written in Python using Psychopy.

## Installation

In order to run the python versions of the experiments, or python script files, you will need to have Python 3 installed.
Specifically, the project has been developed and tested using Python 3.8, although it might also be compatible with other versions of Python 3.
You will also need to install package dependencies before being able to run certain scripts.
You can do this by running `pip install -r requirements.txt` from the command line, or possibly `pip3 install -r requirements.txt` on Linux.
We recommend using a virtual environment to manage Python package versions on a per-project basis.

## Stimuli

An overview of the stimuli can be found in the `stimuli.csv` file.
This is also the file that is used by the experiment code itself to load the stimuli.
Stimulus images can be found in the `images` folder.

## Experiment

The main experiment script is `experiment.py`, with several helper files inside `experiment` folder.
