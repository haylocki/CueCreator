# CueCreator

CueCreator is a desktop application that creates CUE sheets for directories containing audio files. It can also create a CUE sheet for a single audio file containing multiple tracks, using a timings file exported from Audacity.

## Download

Download the latest release from the [GitHub Releases page](https://github.com/haylocki/CueCreator/releases).

- **Linux:** `CueCreator-v1.0.0-Linux.tar.gz`
- **Windows:** `CueCreator-v1.0.0-Windows.zip`

Extract the archive to a suitable folder before installing.

## Linux Installation

### Debian-based distributions

Install the required system packages:

```bash
sudo apt install python3-venv python3-pip
```

### Arch Linux

Install the required system package:

```bash
sudo pacman -S python-virtualenv
```

### Install CueCreator

1. Open a terminal and change to the extracted CueCreator directory:

   ```bash
   cd path/to/CueCreator
   ```

2. Run the installer:

   ```bash
   chmod +x install.sh
   ./install.sh
   ```

The installer creates a Python virtual environment, installs the required Python modules, and adds CueCreator to your applications menu.

Launch CueCreator from the applications menu or run it from the terminal using `run-cuecreator.sh`.

## Windows Installation

1. Extract the downloaded Windows ZIP archive to a suitable folder.
2. Open the extracted CueCreator folder.
3. Run `install.bat`.

The installer checks for Python 3.11, installs it if necessary and available through Windows Package Manager, creates a Python virtual environment, installs the required modules, and creates a Start Menu shortcut.

Once installation is complete, launch CueCreator from the Windows Start Menu. You can also run `run-cuecreator.bat` from the application folder.

## Usage

When CueCreator starts, a directory selection dialog opens. Select the directory containing the audio files from which you want to create a CUE file.

### Creating a CUE sheet from separate audio files

If the directory contains multiple audio files:

1. Select the directory containing the tracks.
2. Review the track information and make any necessary corrections.
3. Click **Save Cue File** to create the CUE sheet.

### Creating a CUE sheet from one file containing multiple tracks

If the directory contains a single audio file containing an entire album, you need to supply a timings file.

1. Open the audio file in Audacity.
2. Add a label at the beginning of each track (`Ctrl+B`), including the start of the first track.
3. Export the labels to a text file using Audacity's label export function.
4. In CueCreator, select the directory containing the audio file.
5. Click **Load Timings** and select the exported file.
6. Review the track information and click **Save Cue File**.

### Loading another directory

Click **Load Directory** to select a different directory of audio files.

## Requirements

- Python 3.11
- PyQt6
- Mutagen

The supplied installers create a virtual environment and install the required Python dependencies.
