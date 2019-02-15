class Controller(object):
    def __init__(self, color="black", controller_type="Nintendo Pro Controller"):
        self.color = color
        self.weight = 2
        self.buttons = False
        self.controller = controller_type
        self.grip = True

    def picking_up(self):
        if self.grip:
            print("You grabbed the controller realizing you need to work out more because it is too heavy.")
        else:
            print("You wanted to play a game, but too lazy and don't want to pick up the controller.")
            
    def press_button(self):
        self.buttons = True
        print("You press the buttons in a random way, because you don't know how to play games.")


my_controller = Controller("White", "Nintendo Gamecube controller")
my_controller.picking_up()