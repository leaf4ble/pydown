# pydown
Incredibly basic Python shutdown many for Linux on cross-platform distros and WM's.

## Installation Shutdown Menu Setup

# 0.9. Download the file and locate it.

### 1. Open a terminal and go to the folder with `pydown.py`:
   ```bash
   cd ~/Downloads/
   ```
   (or wherever you put it)

### 2. Make it executable:
   ```bash
   chmod +x pydown.py
   ```
### 2.1. Move the file from downloads to home

   ```
   mv pydown.py ~/pydown.py
   ```

### 3. Add to your config to run it. For i3wm, put this in `~/.config/i3/config`:
   ```
   bindsym $mod+Shift+e exec python3 ~/pydown.py
   ```
   (change the key or path if you want)

### 4. Or just run it from terminal:
   ```bash
   ./pydown.py
   ```

That’s it.

# Current Issues
Locking feature is only implemented for i3wm, as well as the usage for `i3-msg`.


# Contributing
Pull requests are welcome.
