#!/usr/bin/env python3
import sys
import os
sys.stdout.write('\033]0;Shutdown Menu\007')
sys.stdout.flush()
import curses
import subprocess

opts = ['Lock', 'Logout', 'Shutdown', 'Reboot']
cmds = [
    ['i3lock'],
    ['i3-msg', 'exit'],
    ['systemctl', 'poweroff'],
    ['systemctl', 'reboot']
]

def main(stdscr):
    c = 0
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for i, o in enumerate(opts):
            s = '> ' + o if i == c else '  ' + o
            x = w//2 - len(s)//2
            y = h//2 - len(opts)//2 + i
            stdscr.addstr(y, x, s)
        k = stdscr.getch()
        if k == curses.KEY_UP:
            c = (c - 1) % len(opts)
        elif k == curses.KEY_DOWN:
            c = (c + 1) % len(opts)
        elif k in [10, 13]:
            subprocess.Popen(cmds[c])
            break
        elif k == 27:
            break

curses.wrapper(main) 
