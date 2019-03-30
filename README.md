# Jupyter-Beeper
A beep generator for Jupyter Notebooks (also IPython and Jupyter-Lab) that doesn't display a reproduction widget.

This library was created to solve an ongoing problem originated when creating multiple beeps with individual InvisibleAudio objects: even though the objects are displayed as blank widgets (and not the standard audio reproduction widget, with the playback controls), they still each take space thus disrupting the layout of the cell's output. This implementation uses a single display instance, updating it with a new InvisibleAudio object on each call to beep() but without changing the cell's output layout. A destructor was needed, in order to change the display instance back to a blank HTML object to prevent the sound from auto-playing every time the notebook is opened (given that the invisible widget is stored and functional on the cell's output).

## Usage

```python
import jupyter_beeper

b = jupyter_beeper.Beeper()

# Default config is frequency=440 Hz, secs=0.7 seconds, and
# blocking=False (b.beep() will return when the sound begins)
b.beep()

# We have to put a sleep statement, since the previous call 
# for b.beep() is non blocking, and then it will overlap with
# the next call to b.beep()
time.sleep(2)

# This will not return until the beep is completed
b.beep(frequency=530, secs=0.7, blocking=True)
```
