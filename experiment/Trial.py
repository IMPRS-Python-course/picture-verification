import psychopy as psy

class CueTargetTrial:
    def __init__(self, cue, target, delay_screen, delay=0.5, cue_time=0, max_target_time=2):
        self._cue = cue
        self._target = target
        self._delay = delay
        self._cue_time = cue_time
        self._max_target_time = max_target_time
        self._delay_screen = delay_screen

        self.result = {
            'cue': cue.name,
            'target': target.name,
            'reaction_time': None,
            'response': None
        }
    
    def run(self):
        self._cue.show()
        if self._cue_time > 0:
            psy.core.wait(self._cue_time)

        self._delay_screen.show()
        psy.core.wait(self._delay)
        
        self._target.show()
        clock = psy.core.Clock()
        keys = psy.event.waitKeys(maxWait=self._max_target_time, keyList=['z', 'm'], clearEvents=True, timeStamped=clock)
        self.result['response'], self.result['reaction_time'] = keys[0] if keys is not None and len(keys) > 0 else (None, self._max_target_time)
