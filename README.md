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
   chmod +x shutdown_menu.py
   ```

### 3. Add to your config to run it. For i3wm, put this in `~/.config/i3/config`:
   ```
   bindsym $mod+Shift+e exec /home/zyph/shutdown_menu.py
   ```
   (change the key or path if you want)

### 4. Or just run it from terminal:
   ```bash
   ./shutdown_menu.py
   ```

That’s it.

# Contributing
Pull requests are welcome.
