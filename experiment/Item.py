from .Stimulus import TextStimulus, AudioStimulus, ImageStimulus
import pandas as pd

class Item:
    @staticmethod
    def load_items(file, window):
        return [Item(row, window) for i, row in pd.read_csv(file).iterrows()]
    
    def __init__(self, data, window):
        self.name = data['item']
        self._data = data
        self.preload(window)

    def preload(self, window):
        self.preload_audio(window)
        self.preload_images(window)
        self.preload_text(window)

    def preload_audio(self, window):
        if 'audio_file' in self._data:
            self.sound = AudioStimulus(window, self._data['audio_file'], self.name)
    
    def preload_images(self, window):
        if 'image_file' in self._data:
            self.image = ImageStimulus(window, self._data['image_file'], self.name)
    
    def preload_text(self, window):
        if 'text' in self._data:
            self.text = TextStimulus(window, self._data['text'], self.name)
