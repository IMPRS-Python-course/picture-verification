from psychopy import core, visual, sound

class Stimulus:
    def __init__(self, window, psy_object, name):
        self.name = name
        self._window = window
        self._psy_obj = psy_object

    def show(self):
        self._psy_obj.draw()
        self._window.flip()

class TextStimulus(Stimulus):
    def __init__(self, window, text, name='', color=-1):
        super().__init__(window, visual.TextStim(window, text=text, color=color), name)

class AudioStimulus(TextStimulus):
    def __init__(self, window, path, name='', text='+', color=-1):
        super().__init__(window, text, name, color)
        self._audio = sound.Sound(path)

    def show(self):
        super().show()
        self._audio.play()
        core.wait(self._audio.getDuration())

class ImageStimulus(Stimulus):
    def __init__(self, window, path, name):
        super().__init__(window, visual.ImageStim(window, image=path), name)
