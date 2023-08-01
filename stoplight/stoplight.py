#!/usr/bin/python3

import traffic
import time
import curses

CLK_DIVISION = 10
YELLOW_LIGHT_DURATION = 5


def main(stdscr):

    inter = traffic.intersection_controller()

    # Curses initialization
    curses.curs_set(0)
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)


    while True:

        # Rotate lights
        inter.change_state()

        # Collecting green light locations
        green_lights = inter.get_state() # tuple of traffic light objects

        green_light_positions = [light.green for light in green_lights]


        # Collecting red light locations
        red_lights = inter.get_red_lights() # array of tuples of traffic light objects
        red_light_positions = []

        # Maybe move this to get_red_lights()
        for tup in red_lights:
            for pair in tup:
                red_light_positions.append(pair.red)

        # Print road to window
        stdscr.addstr(0, 0, traffic.road)

        # Printing green lights
        for row, col in green_light_positions:
            stdscr.addch(row, col, "0", curses.color_pair(3))

        # Print red lights
        for row, col in red_light_positions:
            stdscr.addch(row, col, "0", curses.color_pair(1))

        # Flush to screen
        stdscr.refresh()



        # Wait for green duration
        time.sleep(inter.state_duration() / CLK_DIVISION)

        # Green lights turn to yellow
        yellow_lights = green_lights

        # Collect yellow lights
        yellow_light_positions = [light.yellow for light in yellow_lights]

        # Print yellow lights
        for row, col in yellow_light_positions:
            stdscr.addch(row, col, "0", curses.color_pair(2))

        # Clear green lights
        for row, col in green_light_positions:
            stdscr.addch(row, col, "0")

        stdscr.refresh()

        # Wait for Yellow in between
        time.sleep(YELLOW_LIGHT_DURATION / CLK_DIVISION)


# Call main from wrapper to auto handle terminal config
curses.wrapper(main)

