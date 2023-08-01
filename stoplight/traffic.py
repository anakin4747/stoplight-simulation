
class traffic_light:
    # Each color is a tuple which holds the position of the light
    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green


class intersection_controller:

    # Pairs of traffic light objects represent the 4 states of the lights
    north_south_left_lights = (traffic_light((22, 36), (23, 36), (24, 36)), \
                                traffic_light((12, 32), (11, 32), (10, 32)))

    north_south_straight_lights = (traffic_light((22, 38), (23, 38), (24, 38)), \
                                    traffic_light((12, 30), (11, 30), (10, 30)))

    east_west_left_lights = (traffic_light((18, 26), (18, 24), (18, 22)), \
                                traffic_light((16, 42), (16, 44), (16, 46)))

    east_west_straight_lights = (traffic_light((20, 26), (20, 24), (20, 22)), \
                                    traffic_light((14, 42), (14, 44), (14, 46)))


    # Choose any state to start in
    def __init__(self):
        self.state = self.north_south_left_lights


    # Returns the current pair of green lights
    def get_state(self):
        return self.state


    def get_red_lights(self):
        red_light_states = [ self.north_south_left_lights, \
                             self.north_south_straight_lights, \
                             self.east_west_left_lights, \
                             self.east_west_straight_lights ]
        red_light_states.remove(self.state)
        return red_light_states
    

    def change_state(self):

        # Rotate through 4 states

        if self.state == self.north_south_left_lights:
            self.state = self.north_south_straight_lights 
            
        elif self.state == self.north_south_straight_lights:
            self.state = self.east_west_left_lights 

        elif self.state == self.east_west_left_lights:
            self.state = self.east_west_straight_lights 

        elif self.state == self.east_west_straight_lights:
            self.state = self.north_south_left_lights 


    def state_duration(self):

        # Return period of time for lights to be green

        if self.state == self.north_south_left_lights or \
            self.state == self.east_west_left_lights:
            return 10

        elif self.state == self.north_south_straight_lights or \
            self.state == self.east_west_straight_lights:
            return 30


road = """

                            |     |     |
                            |     |     |
                            |  |  |  ^  |
                            |  |  |  |  |
                            |  |  |  |  |
                            |  |  |  |  |
                            |  v  |  |  |
                            |     |     |
                            | 0 0 |     |
                            | 0 0 |     |
                            | 0 0 |     |
----------------------------             ------------------------------- 
                                          0 0 0
            <-------                                <------
                                          0 0 0
----------------------------             ------------------------------- 
                      0 0 0
            ------->                                ------>
                      0 0 0
----------------------------             ------------------------------- 
                            |     | 0 0 |
                            |     | 0 0 |
                            |     | 0 0 |
                            |     |     |
                            |  |  |  ^  |
                            |  |  |  |  |
                            |  |  |  |  |
                            |  |  |  |  |
                            |  v  |  |  |
                            |     |     |
"""
