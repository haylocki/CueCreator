## Linux Install:

**To install on debian based systems:**

`sudo apt install python3.10-venv pip`

**To install on Arch Linux based systems:**

`sudo pacman -S python-virtualenv`

**Change directory to where you downloaded CueCreator**

`cd path/to/CueCreator`

**Create a python virtual environment:**

`python3 -m venv cueenv`

**Activate the virtual environment:**

`source cueenv/bin/activate`

**Install the requied python modules:**

`pip install pyqt5 mutagen`

**Run the application:**

`python ./src/Cue_Creator.py`

**To run the application in the future:**

`source path/to/CueCreator/cueenv/bin/activate`

`python path/to/CueCreator/src/Cue_Creator.py`

# Usage:

When run the application will open a Directory Dialog.
Select the directory containing the audio files you want to create a cue file for.

The main window will now open listing all the audio files found in the selected directory.
Missing or incorrect information can be changed by double clicking on the appropriate item.

If the Directory contains multiple audio files then you can save the cue file by clicking on the "Save Cue File" button.

If the Directory only has a single audio file that contains multiple tracks you need to provide a timings file by clicking on "Load Timings".
Then you can save the cue file by clicking on the "Save Cue File" button.

You can create a timings file by loading the audio file into audacity and adding a label at the start of each track (don't forget the first track).
Then export the labels to a text file. You will then have a compatible timings file that can be loaded with the "Load Timings" button. 

To load a new directory click on the "Load Directory" button.




