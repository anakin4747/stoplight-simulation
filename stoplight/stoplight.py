#!/usr/bin/python3

import traffic
import time
import curses

CLK_DIVISION = 10
YELLOW_LIGHT_DURATION = 5

inter = traffic.intersection_controller()


def draw_intersection(stdscr):

    # Remove cursor
    curses.curs_set(0)
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Print road to window
    stdscr.addstr(0, 0, traffic.road)
    stdscr.refresh()

    lights = [

        (10, 30, "0", curses.color_pair(3)), # South green
        (10, 32, "0", curses.color_pair(3)), # South left green
        (11, 30, "0", curses.color_pair(2)), # South yellow
        (11, 32, "0", curses.color_pair(2)), # South left yellow
        (12, 30, "0", curses.color_pair(1)), # South red
        (12, 32, "0", curses.color_pair(1)), # South left red

        (22, 36, "0", curses.color_pair(1)), # North left red
        (22, 38, "0", curses.color_pair(1)), # North red
        (23, 36, "0", curses.color_pair(2)), # North left yellow
        (23, 38, "0", curses.color_pair(2)), # North yellow
        (24, 36, "0", curses.color_pair(3)), # North left green
        (24, 38, "0", curses.color_pair(3)), # North green

        (16, 42, "0", curses.color_pair(1)), # West left red
        (14, 42, "0", curses.color_pair(1)), # West red
        (16, 44, "0", curses.color_pair(2)), # West left yellow
        (14, 44, "0", curses.color_pair(2)), # West yellow
        (16, 46, "0", curses.color_pair(3)), # West left green
        (14, 46, "0", curses.color_pair(3)), # West green

        (18, 26, "0", curses.color_pair(1)), # East left red
        (20, 26, "0", curses.color_pair(1)), # East red
        (18, 24, "0", curses.color_pair(2)), # East left yellow
        (20, 24, "0", curses.color_pair(2)), # East yellow
        (18, 22, "0", curses.color_pair(3)), # East left green
        (20, 22, "0", curses.color_pair(3)), # East green

    ]

    while True:

        for row, col, char, color in lights:
            stdscr.addch(row, col, char, color)
        stdscr.refresh()

        inter.change_state()
        stdscr.addstr(0, 0, str(inter.get_state()))
        stdscr.refresh()

        # Wait for green duration
        time.sleep(inter.state_duration() / CLK_DIVISION)

        stdscr.addstr(0, 0, "Yellow")
        stdscr.refresh()
        # Wait for Yellow in between
        time.sleep(YELLOW_LIGHT_DURATION / CLK_DIVISION)


curses.wrapper(draw_intersection)

