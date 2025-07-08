# pydown
Incredibly basic Python shutdown many for Linux on cross-platform distros and i3.
# [Download](https://github.com/leaf4ble/pydown/releases/download/untagged-ff106f207a5f0fed3df2/pydown.py)

## Installation Shutdown Menu Setup

# 0. Download alacritty

   ```bash

   Note: You might need to elevate your privileges using `doas`, `sudo`, `su` or logging in as `root` 
   
   Debian/Ubuntu: apt install alacritty
   Arch: pacman -Syyu alacritty
   openSUSE: zypper install alacritty
   Gentoo: emerge --ask x11-terms/alacritty
   Fedora: dnf install alacritty
   Source: https://github.com/alacritty/alacritty
   ```
You may also need python, a bunch of distros come preinstalled with python anyway.

# 0.1. Download the file and locate it.

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
   bindsym $mod+shift+e exec alacritty --title pydown -e python ~/pydown.py
   for_window [class=Alacritty" title="pydown"] fullscreen enable
   ```
   (change the key or path if you want)

### 4. Or just run it from terminal:
   ```bash
   ./pydown.py
   ```

That’s it.

# Current Issues
Locking feature is only implemented for i3wm, as well as the usage for `i3-msg`. Universal release would be nice.

Status: Works on Arch. No other distros have been tested, but it is python and should universally work.

# Contributing
Pull requests are welcome.
