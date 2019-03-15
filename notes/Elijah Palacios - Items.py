class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Building(object):
    def __init__(self, name):
        self.name = name


class Shop(Building):
    def __init__(self, name):
        super(Shop, self).__init__(name)
        self.storage = {}


class HorseShop(Shop):
    def __init__(self, name):
        super(HorseShop, self).__init__(name)
        self.storage = {
            "stock1": {
                "Name": my_blackhorse.name,
                "Cost": 15
            },
            "Stock2": {
                "Name": my_whitehorse.name,
                "Cost": 20
            },
            "Stock3": {
                "Name": my_goldenhorse,
                "Cost": 30
            }
        }


class Interactable(Item):
    def __init__(self, name, description):
        super(Interactable, self).__init__(name, description)


class Currency(Interactable):
    def __init__(self, name, description):
        super(Currency, self).__init__(name, description)


class Monay(Currency):
    def __init__(self):
        super(Currency, self).__init__("Monay", "Can be used at a shop")
        self.count = 0

class HealingItem(Interactable):
    def __init__(self, name, description):
        super(HealingItem, self).__init__(name, description)


class Bandaids(HealingItem):
    def __init__(self):
        super(Bandaids, self).__init__("BandAids", "Can heal your health")

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
    def __init__(self, name, description):
        super(Weapon, self).__init__(name, description)


class BoxingGloves(Weapon):
    def __init__(self):
        super(BoxingGloves, self).__init__("Boxing Gloves", "Use them to punch harder")



class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Excalibur", "The legendary sword Excalibur")



class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Knife", "Can be swung faster and thrown")


class BowAndArrow:
    def __init__(self):
        super(BowAndArrow, self).__init__("Bow and Arrow", "Can be shot.")





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
my_sword = Sword()
my_knife = Knife()
my_bow = BowAndArrow()
my_gloves = BoxingGloves()
my_shop = HorseShop("Pikachu Horse Shop")
Money = Monay()
healing = Bandaids()




