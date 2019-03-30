from IPython.display import display, Audio, HTML
import numpy as _np
import time as _time
import random as _rand

class InvisibleAudio(Audio):
    '''
    IPython.display.Audio, but without it being displayed. It still takes space in the output 
    layout tough.
    '''
    def _repr_html_(self):
        audio = super()._repr_html_()
        audio = audio.replace('<audio', f'<audio onended="this.parentNode.removeChild(this)"')
        return f'<div style="display:none">{audio}</div>'

class Beeper:
    ''' Makes sound on client using javascript (works with remote server) '''
    def __init__(self):
        self.id = _rand.randint(0, 10000000000000000000)
        display(HTML(""), display_id=str(self.id))

    def beep(self, frequency=440, secs=0.05, blocking=False):
        '''
        Make a beep, self explanatory...

        Args:
            frequency (int): Frequency (in Hertz) of the beep to be produced. Default is 440.
            secs (float): Duration (in seconds) of the beeps. Default is 0.05
            blocking (bool): If True, then the method will not return until the beep is completed. 
                             If False, then the method will return immediatly after begining the beep.
                             Default if False.
        '''
        framerate = 44100
        t = _np.linspace(0, secs, int(framerate * secs))
        data = _np.sin(2 * _np.pi * frequency * t)

        self.beeper = InvisibleAudio(data, rate=framerate, autoplay=True)
        display(self.beeper, display_id=str(self.id), update=True)
        if blocking:
            _time.sleep(secs)

    def __del__(self):
        display(HTML(""), display_id=str(self.id))
