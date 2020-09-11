import psychopy as psy
from experiment import Item, TextStimulus, CueTargetTrial
from numpy.random import permutation
import pandas as pd

# Load and prepare window and stimuli objects
window = psy.visual.Window(color=1)
stimuli = permutation(Item.load_items('stimuli.csv', window))
break_screen = TextStimulus(window, 'You can take a break now.\nPress any key to continue.')
fixation_screen = TextStimulus(window, '+')

# Generate correct and incorrect trials, and shuffle them
correct_trials = [CueTargetTrial(stimulus.text, stimulus.image, fixation_screen, cue_time=1) for stimulus in stimuli]
incorrect_trials = [CueTargetTrial(distractor.text, stimulus.image, fixation_screen, cue_time=1)
                    for stimulus, distractor in zip(stimuli, list(stimuli[1:]) + list(stimuli[:1]))]
trials = permutation(correct_trials + incorrect_trials)

# Run the actual experiment, with breaks at regular intervals
break_interval = 24
for i, trial in enumerate(trials):
    trial.run()  # Run a single trial
    
    # Show a break at regular intervals
    if (i + 1) % break_interval == 0:
        break_screen.show()
        psy.event.waitKeys()
    
    # Show the fixation screen for 1 second
    fixation_screen.show()
    psy.core.wait(1)

# Convert the results into a dataframe, and save to CSV
results = pd.DataFrame([trial.result for trial in trials])
results.to_csv('results.csv', index_label='order')
