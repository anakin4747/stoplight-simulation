from enum import Enum, auto


class intersection(Enum):
    north_south_left_lights = auto()
    north_south_straight_lights = auto()
    east_west_left_lights = auto()
    east_west_straight_lights = auto()


class intersection_controller:

    def __init__(self):
        self.state = intersection.north_south_left_lights


    def get_state(self):
        return self.state


    def change_state(self):

        if self.state == intersection.north_south_left_lights:
            self.state = intersection.north_south_straight_lights 
            
        elif self.state == intersection.north_south_straight_lights:
            self.state = intersection.east_west_left_lights 

        elif self.state == intersection.east_west_left_lights:
            self.state = intersection.east_west_straight_lights 

        elif self.state == intersection.east_west_straight_lights:
            self.state = intersection.north_south_left_lights 


    def state_duration(self):

        if self.state == intersection.north_south_left_lights:
            return 10

        elif self.state == intersection.north_south_straight_lights:
            return 30

        elif self.state == intersection.east_west_left_lights:
            return 10

        elif self.state == intersection.east_west_straight_lights:
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
