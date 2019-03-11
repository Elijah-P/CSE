class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Interactable(Item):
    def __init__(self, name, description):
        super(Interactable, self).__init__(name, description)


class Switches(Item):
    def __init__(self, name, description):
        super(Switches, self).__init__(name, description)
        self.switch = False

    def turn_on(self):
        self.switch = True

    def turn_off(self):
        self.switch = False


class Horse(Item):
    def __init__(self, name, description, speed):
        super(Horse, self).__init__(name, description)
        self.speed = speed

    def go_faster(self):
        self.speed += 10

    def go_slower(self):
        self.speed -= 10


class Weapon(Interactable):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name, description)
        self.damage = damage


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Excalibur", "The legendary sword Excalibur", 999)

    def swing_sword(self):
        ogre -= 999


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Knife", "Can be swung faster and thrown", 50)

    def stab(self):
        ogre -= 50

    def throw(self):
        ogre -= 100

class 



class Catcus(Switches):
    def __init__(self):
        super(Catcus, self).__init__("Cactus", "Total ordinary cactus. Though there does look like a lever is "
                                               "attached, maybe you could flip it..")


class BlackHorse(Horse):
    def __init__(self):
        super(BlackHorse, self).__init__("Roger", "He is black and seems stubborn. Reminds you of pigs...", speed=50)


class WhiteHorse(Horse):
    def __init__(self):
        super(WhiteHorse, self).__init__("Tyrone", "He is white and seems stuck up. Reminds you of a hairless cats...",
                                         speed=30)


class GoldenHorse(Horse):
    def __init__(self):
        super(GoldenHorse, self).__init__("Charles", "He is golden and seems really lazy. Reminds you of a person who "
                                                     "lives in their parents basement...", speed=0)


class Key(Interactable):
    def __init__(self):
        super(Key, self).__init__("Key", "Can be used to unlock doors")


class Controller(Interactable):
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
my_GamecubeController = GamecubeController()
my_Joycons = Joycons()
my_ProController = ProController()
my_blackhorse = BlackHorse()
my_whitehorse = WhiteHorse()
my_goldenhorse = GoldenHorse()
Cactus = Catcus()

command = input(">_")
if "pick up" in command:
    item_name = command[8:]
    found_item = None
    for thing in room.items:
        if thing.name == item_name:
            found_item = thing
    if isinstance(found_item, Interactable):
        print("You pick up the " + item_name)
        player.inventory.append(found_item)
    elif found_item is None:
        print("You don't see one here")
    else:
        print("You can't pick it up")


"pick up key"
