#!/usr/bin/env python3
# AUTHOR:   Ian Drobney
# DATE:     4/1/2016

import curses
import pycase


def basic_menu(list_of_items, title=''):
    # curses init stuff
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(0)

    running = True
    # which item is currently selected
    # mainly here so I don't forget it exists
    selected = 0
    max = len(list_of_items) - 1
    maxheight, maxwidth = stdscr.getmaxyx()
    maxheight -= 2
    current_top = 0
    if maxheight >= max:
        current_bottom = max
    else:
        current_bottom = maxheight

    while running:
        maxheight, maxwidth = stdscr.getmaxyx()
        maxheight -= 2
        stdscr.clear()
        curses.setsyx(0, 0)
        if title != '':
            stdscr.addstr(title + '\n')
        for i in range(current_top, current_bottom + 1):
            if i == selected:
                stdscr.addstr(str(list_of_items[i] +
                              (' ' * (maxwidth - len(list_of_items[i]) - 1))),
                              curses.A_REVERSE)
            else:
                stdscr.addstr(str(list_of_items[i]))
            if i != current_bottom:
                stdscr.addstr('\n')
        stdscr.refresh()
        input_in = stdscr.getch()
        for case in pycase.switch(input_in):
            if case(curses.KEY_DOWN):
                if selected == current_bottom:
                    if selected != max:
                        selected = selected + 1
                        current_bottom += 1
                        current_top += 1
                    else:
                        selected = 0
                        current_top = 0
                        if max >= maxheight:
                            current_bottom = maxheight
                        else:
                            current_bottom = max

                else:
                    selected += 1
                break
            if case(curses.KEY_UP):
                if selected == current_top:
                    if selected != 0:
                        selected = selected - 1
                        current_bottom -= 1
                        current_top -= 1
                    else:
                        selected = max
                        if max >= maxheight:
                            current_top = (max - maxheight)
                        else:
                            current_top = 0
                        current_bottom = max

                else:
                    selected -= 1
                break
            if case(ord('q')):
                running = False
                break
            if case(10):
                running = False
                break
            if case():
                break
                # default, if not recognised
    # curses closeout stuff
    curses.curs_set(1)
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    return selected, list_of_items[selected]
