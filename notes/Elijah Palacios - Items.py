class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Key(Item):
    def __init__(self):
        super(Key, self).__init__("Key", "Can be used to unlock doors")


class Controller(Item):
    def __init__(self, name, description, color, controller_type):
        super(Controller, self).__init__(name, description)
        self.color = color
        self.type = controller_type


class GamecubeController(Controller):
    def __init__(self):
        super(GamecubeController, self).__init__("Gamecube Controller", "This controller is black. It is wired",
                                                 "Black", "Wired")


class Joycons(Controller):
    def __init__(self):
        super(Joycons, self).__init__("JoyCons", "The left Joycon is red, and the right is Blue.", "Blue and Red",
                                      "Wireless")


class ProController(Controller):
    def __init__(self):
        super(ProController, self).__init__("Switch Pro Controller", "It's a somewhat black wireless Xbox styled "
                                                                     "controller.", "Blackish Gray", "Wireless")


my_key = Key()
my_GamecubeController = GamecubeController
my_Joycons = Joycons
my_ProController = ProController