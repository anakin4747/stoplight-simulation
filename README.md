# Stoplight Simulation

I created a traffic light simulator using Python and the Ncurses library for
displaying.

![traffic light](docs/intersection-image.png)

This program can be ran by either cloning this repo and running:

    $ make

Just ensure you have the ncurses library downloaded. It needs to be installed
if you are on windows.

The docker image can be run with the following commands:

    $ docker pull anakin7474/stoplight:latest

    $ docker run -it --rm anakin7474/stoplight

