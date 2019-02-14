class Controller(object):
    def __init__(self, color , controller_type = "Nintendo Pro Controller"):
        self.color = color
        self.weight = int("2 pounds")
        self.buttons = False
        self.controller = controller_type
        self.grip = True

    def picking_up(self):
        if self.grip:
            print("You grabbed the controller realizing you need to work out more because it is too heavy.")
        else:
            print("You wanted to play a game, but too lazy and don't want to pick up the controller.")


Controller.picking_up()