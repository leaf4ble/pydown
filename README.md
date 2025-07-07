# pydown
Incredibly basic Python shutdown many for Linux on cross-platform distros and i3.

## Installation Shutdown Menu Setup

# 0. Download alacritty

   ```bash
   Debian/Ubuntu: apt install alacritty
   Arch: pacman -Syyu alacritty
   openSUSE: zypper install alacritty
   Gentoo: emerge --ask x11-terms/alacritty
   Fedora: dnf install alacritty
   Source: https://github.com/alacritty/alacritty
   ```
You may also need python, a bunch of distros come preinstalled with python anyway.

# 0.1. Download the file and locate it.

### 1. Open a terminal and go to the folder with `shutdown_menu.py`:
   ```bash
   cd ~/Downloads/
   ```
   (or wherever you put it)

### 2. Make it executable:
   ```bash
   chmod +x shutdown_menu.py
   ```
### 2.1. Move the file from downloads to home

   ```
   mv shutdown_menu.py ~/shutdown_menu.py
   ```

### 3. Add to your config to run it. For i3wm, put this in `~/.config/i3/config`:
   ```
   bindsym $mod+shift+e exec alacritty --title pydown -e python ~/pydown.py
   for_window [class=Alacritty" title="pydown"] fullscreen enable
   ```
   (change the key or path if you want)

### 4. Or just run it from terminal:
   ```bash
   ./shutdown_menu.py
   ```

That’s it.

# Current Issues
Locking feature is only implemented for i3wm, as well as the usage for `i3-msg`.

Status: Works on Arch. No other distros have been tested, but it is python and should universally work.

# Contributing
Pull requests are welcome.
