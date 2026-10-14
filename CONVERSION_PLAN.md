# Qt6 Conversion Plan

## Overview
Convert the CueCreator project from PyQt5 to PyQt6

## Issues to Address

### 1. Dependencies
- Update pyproject.toml: change "pyqt5>=5.15" to "PyQt6>=6.0"
- Update setup.py: change "pyqt5>=5.15" to "PyQt6>=6.0"

### 2. Import Statements
Change all imports from PyQt5 to PyQt6:
- `from PyQt5.QtWidgets import ...` → `from PyQt6.QtWidgets import ...`
- `from PyQt5.QtCore import ...` → `from PyQt6.QtCore import ...`
- `from PyQt5.QtGui import ...` → `from PyQt6.QtGui import ...`

### 3. API Changes
Check for API changes between Qt5 and Qt6:
- `app.exec_()` → `app.exec()`
- Some method signatures might have changed
- Some deprecated APIs might have been removed

### 4. Files to Convert
All Python files in `src/cuecreator/`:
- Cue_Creator.py
- Album.py
- Audio_Tree_Widget.py
- Audio_Info_Delegate.py
- Track_List.py
- Track_Item_Delegate.py
- Track_Info.py
- Track_Number.py
- Format_Time.py
- Read_Tags.py
- Save_Cue_File.py
- Load_Tracks.py
- Load_Tracks_Dialog.py
- Load_Timings_Dialog.py
- Album_Tree_Widget.py

### 5. Test Steps
1. Update dependencies
2. Update all import statements
3. Update API calls where needed
4. Test the application
5. Fix any runtime issues

## Files Modified

### Configuration Files
- pyproject.toml
- setup.py

### Python Source Files
- src/cuecreator/Cue_Creator.py
- src/cuecreator/Album.py
- src/cuecreator/Audio_Tree_Widget.py
- src/cuecreator/Audio_Info_Delegate.py
- src/cuecreator/Track_List.py
- src/cuecreator/Track_Item_Delegate.py
- src/cuecreator/Track_Info.py
- src/cuecreator/Track_Number.py
- src/cuecreator/Format_Time.py
- src/cuecreator/Read_Tags.py
- src/cuecreator/Save_Cue_File.py
- src/cuecreator/Load_Tracks.py
- src/cuecreator/Load_Tracks_Dialog.py
- src/cuecreator/Load_Timings_Dialog.py
- src/cuecreator/Album_Tree_Widget.py

## Testing

### Initial Test
```bash
cd /home/ian/src/CueCreator
python3 src/cuecreator/Cue_Creator.py
```

### Dependencies Test
```bash
cd /home/ian/src/CueCreator
pip install -e . --break-system-packages
```

## Potential Issues

### 1. API Changes
Some methods might have changed between Qt5 and Qt6:
- `QApplication.exec_()` → `QApplication.exec()`
- Some widget methods might have changed

### 2. Image Loading
The project uses hardcoded images (icon.png, file.png, etc.) - these might need to be updated if Qt6 has different requirements

### 3. Signal/Slot Changes
Some signal/slot syntax might have changed

## Resources

- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [PyQt6 Migration Guide](https://www.riverbankcomputing.com/static/Docs/PyQt6/migration_guide.html)