#!/usr/bin/python3

import traffic
import time
import curses

# Can be increased to speed up program
CLK_DIVISION = 1
YELLOW_LIGHT_DURATION = 5

def print_lights(stdscr, lights, color):
    for row, col in lights:
        stdscr.addch(row, col, "0", curses.color_pair(color))


def main(stdscr):

    inter = traffic.intersection()

    # Curses initialization
    curses.curs_set(0)
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    # curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # Switch this line for the one above to use a different color for yellow lights
    # since Windows command prompts don't support colors the same way UNIX based ones do
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)


    while True:

        # Rotate lights
        inter.change_state()

        # Collecting green light locations
        green_lights = inter.get_state()
        green_light_positions = [light.green for light in green_lights]

        # Collecting red light locations
        red_light_positions = inter.get_red_lights() # array of tuples of traffic light objects

        # Print road to window
        stdscr.addstr(0, 0, traffic.road)

        # Printing red and green lights
        print_lights(stdscr, green_light_positions, 3)
        print_lights(stdscr, red_light_positions, 1)

        # Flush to screen
        stdscr.refresh()

        # Wait for green duration
        time.sleep(inter.state_duration() / CLK_DIVISION)


        # Green lights turn to yellow
        yellow_lights = green_lights
        yellow_light_positions = [light.yellow for light in yellow_lights]

        # Print yellow and clear green lights
        print_lights(stdscr, yellow_light_positions, 2)
        print_lights(stdscr, green_light_positions, 0)

        stdscr.refresh()

        # Wait for Yellow in between
        time.sleep(YELLOW_LIGHT_DURATION / CLK_DIVISION)


# Call main from wrapper to auto handle terminal config
curses.wrapper(main)

