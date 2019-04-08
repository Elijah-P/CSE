def take(_item_name):
    _found_item = None
    if player.current_location.item is not None:
        if player.current_location.item.name.lower() == _item_name.lower():
            _found_item = player.current_location.item
    if isinstance(_found_item, Interactable):
        print("You pick up the " + _item_name)
        player.inventory.append(_found_item)
        player.current_location.item = None
    elif _found_item is None:
        print("You don't see one here")
    else:
        print("You can't pick it up")


#   def plug_in(_item_name):


def equip(_item_name):
    _found_item = None
    for _item in player.inventory:
        if _item_name.lower() == item_name.lower():
            _found_item = _item
    print("You equip the %s" % _found_item.name)
    player.inventory.append(player.weapon)
    player.weapon = _found_item


def drop(_item_name):
    _found_item = None
    for _item in player.inventory:
        if _item.name.lower() == item_name.lower():
            _found_item = _item
            print("You drop the %s" % _item.name)
    if _found_item is not None:
        if player.current_location.item is None:
            player.current_location.item = _found_item
            player.inventory.remove(_found_item)
        else:
            print("There is already an item here.")
    else:
        print("You don't have one")


class Room(object):
    def __init__(self, name, north, east, south, west, up, down, description, _item=None, money=None, enemy=None,
                 requirments=None, shop=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.item = _item
        self.money = money
        self.enemy = enemy
        self.visit = 0
        self.requirments = requirments
        self.shop = shop


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Interactable(Item):
    def __init__(self, name, description):
        super(Interactable, self).__init__(name, description)


class Building(object):
    def __init__(self, name):
        self.name = name


# SHOP
class Shop(Building):
    def __init__(self, name):
        super(Shop, self).__init__(name)
        self.storage = {}

    def ask(self):
        print("Welcome to %s, do you want to buy something" % self.name)
        _command = input(">")
        if _command in ["buy", "b", "purchase"]:
            print("Here's what we have in store;")
            for item in self.storage:
                print(self.storage[item]["Name"] + " - " + str(self.storage[item]["Cost"]) + "$")
            request = input("I want to buy >")
            for i, thing in enumerate(self.storage.keys()):
                if self.storage[thing]["Name"] == request:
                    customer_i = input("Do you want the %s" % self.storage[thing]["Name"])
                    if customer_i in ["Yes", "confirm", "affirmative"]:
                        if player.money >= self.storage[thing]["Cost"]:
                            print("You have purchased it for %d Money" % self.storage[thing]["Cost"])
                            print("You have %d Money left" % player.money)
                            player.inventory.append(self.storage[thing]["ID"])
                        elif player.money < self.storage[thing]["Cost"]:
                            if player.money <= 0:
                                print("You are broke")
                            else:
                                print("You only have %d with you" % player.money)
                                self.ask()


class Currency(Interactable):
    def __init__(self, name, description):
        super(Currency, self).__init__(name, description)


class Monay(Currency):
    def __init__(self):
        super(Currency, self).__init__("Monay", "Can be used at a shop")
        self.count = 0

#########
# HEALING


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
# WEAPONS


class Weapon(Interactable):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name, description)
        self.damage = damage


class BoxingGloves(Weapon):
    def __init__(self):
        super(BoxingGloves, self).__init__("Boxing Gloves", "Use them to punch harder", 10)


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Excalibur", "The legendary sword Excalibur", 999)


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Knife", "Can be swung faster and thrown", 35)


class BowAndArrow(Weapon):
    def __init__(self):
        super(BowAndArrow, self).__init__("Bow and Arrow", "Can be shot.", 15)


class AXE(Weapon):
    def __init__(self):
        super(AXE, self).__init__("A powerful Axe", "Can be swung with immense power", 100)
# SWITCH


class Catcus(Switches):
    def __init__(self):
        super(Catcus, self).__init__("Cactus", "Total ordinary cactus. Though there does look like a lever is "
                                               "attached, maybe you could flip it..")
# HORSES


class BlackHorse(Horse):
    def __init__(self):
        super(BlackHorse, self).__init__("Roger", "He is black and seems stubborn. Reminds you of pigs...",
                                         speed=50)


class WhiteHorse(Horse):
    def __init__(self):
        super(WhiteHorse, self).__init__("Tyrone.", "He is white and seems stuck up. Reminds you of a hairless cats...",
                                         speed=30)


class GoldenHorse(Horse):
    def __init__(self):
        super(GoldenHorse, self).__init__("Charles", "He is golden and seems really lazy. Reminds you of a person who "
                                          "lives in their parents basement...", speed=0)


class Key(Interactable):
    def __init__(self):
        super(Key, self).__init__("Key", "Can be used to unlock doors")

# GAME CONTROLLERS


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
        super(ProController, self).__init__("Pro Controller", "It's a somewhat black wireless Xbox styled "
                                            "controller.", "Blackish Gray", "Wireless")
# ENTITIES


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        target.take_damage(self.weapon.damage)
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))


class Player(object):
    def __init__(self, name, health, weapon, starting_location):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10
        self.money = 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s have %d health left" % (self.name, self.health))

    def attack(self, target):
        try:
            print("%s attack %s for %d damage" % (self.name, target.name, self.weapon.damage))
            target.take_damage(self.weapon.damage)
        except AttributeError:
            print("You can't attack with this")

    def move(self, newlocation):
        """

        :param newlocation: The variable containing a room object
        """
        self.current_location = newlocation


class Bigboss(Character):
    def __init__(self, name, health, weapon, description):
        super(Bigboss, self).__init__(name, health, weapon, armor=None)
        self.name = name
        self.health = health
        self.weapon = weapon
        self.description = description

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            print("%s is dead" % ogre)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class HorseShop(Shop):
    def __init__(self, name):
        super(HorseShop, self).__init__(name)
        self.storage = {
            "stock1": {
                "Name": my_blackhorse.name,
                "Cost": 15,
                "ID": my_blackhorse
            },
            "Stock2": {
                "Name": my_whitehorse.name,
                "Cost": 20,
                "ID": my_whitehorse
            },
            "Stock3": {
                "Name": my_goldenhorse.name,
                "Cost": 30,
                "ID": my_goldenhorse
            }
        }


# items
my_key = Key()
my_GamecubeController = GamecubeController()
my_Joycons = Joycons()
my_ProController = ProController()
my_blackhorse = BlackHorse()
my_whitehorse = WhiteHorse()
my_goldenhorse = GoldenHorse()
secret_Cactus = Catcus()
my_sword = Sword()
my_knife = Knife()
my_bow = BowAndArrow()
my_axe = AXE()
my_gloves = BoxingGloves()
my_shop = HorseShop("Pikachu Horse Shop")
Money = Monay()
healing = Bandaids()

ogre = Bigboss("Shrek", 300, my_axe, "Looks like Shrek,..ugly.")

center = Room("Center of The World.", "forest", "portal", None, "Desert", None, None,
              "A 10K TV is in front of you with SmashBros on. "
              "There are 8 open spots to play, but no controllers. "
              "There are 4 different ways to go.", None, 0, None, [my_GamecubeController, my_Joycons, my_ProController])

portal = Room("Entrance to portal.", None, "mountains", None, "center", None, None,
              "A weird portal(looking like a nether portal from minecraft). "
              "You feel a cold breeze coming from the other side.", None, 50)

mountains = Room("Middle of snowy mountain", "peak_of_mountain", "cavern", "base_of_mountain", "portal", None, None,
                 "The portal led to the middle of a mountain. "
                 "You see the peak and base of the mountain. "
                 "You also see a cavern east.", None, 25)

peak_of_mountain = Room("Peak of The Snowy Mountain", None, None, "mountains", None, None, None,
                        "You climbed up the mountain. "
                        "Your index finger is purple.", my_ProController)

cavern = Room("Inside the cavern", None, None, None, "mountains", None, None,
              "You see this buff, ripped Pikachu behind the counter. "
              "It is the owner of this shop. "
              "It yells 'PIKA PIKA' in a deep voice. "
              "You see a horse. It looks wounded.", None, 0, None, None, my_shop)

base_of_mountain = Room("The base of the Snowy Mountain", "mountains", None, None, None, None, None,
                        "You climbed down the mountain. "
                        "You see an entrance with a staircase leading down.")

forest = Room("Entrance to Forest", "inside_forest", None, "center", None, None, None,
              "There is a sign saying, 'D-NT -ET -OST.' "
              "Letters are missing on the sign. Fog surrounds the entrance.")

inside_forest = Room("Inside the Forest.", "Boss", "Lost_Woods", "Forest", "Dungeon", None, None,
                     "There are 3 paths. "
                     "You hear a roaring noise from the northern path")

Lost_Woods = Room("Lost Woods", None, "L1", None, "inside_forest", None, None,
                  "There are a lot of paths. "
                  "Seems like if you go the wrong way you'll be brought back to the entrance")

L1 = Room("Lost_Woods", "Lost_Woods", "L2", "Lost_Woods", "Lost_Woods", None, None, "")

L2 = Room("Lost_Woods", "Lost_Woods", "Lost_Woods", "L3", "Lost_Woods", None, None, "")

L3 = Room("Lost_Woods", "L4", "Lost_Woods", "Lost_Woods", "Lost_Woods", None, None, "")

L4 = Room("Lost_Woods", "Lost_Woods", "Lost_Woods", "Lost_Woods", "L5", None, None, "")

L5 = Room("Lost_Woods", "Lost_Woods", "Lost_Woods", "L6", "Lost_Woods", None, None, "")

L6 = Room("Lost_Woods", "L7", "Lost_Woods", "Lost_Woods", "Lost_Woods", None, None, "")

L7 = Room("End of Lost Woods", "Lost_Woods", "Lost_Woods", "Lost_Woods", "Lost_Woods", None, None,
          "You have found a key on the floor, could be used somewhere else here in the forest. "
          "To leave, you assume you can take any direction to be taken back to the entrance of the lost woods.", my_key)

Dungeon = Room("Dungeon", None, "inside_forest", None, None, None, None,
               "You're inside a dark somewhat smelly dungeon."
               " Careful, traps might be here. To go through you would need a key to enter.")
# Path is D3, D5, D7, D8, D9

D1 = Room("Dungeon", "D3", "D6", None, "D4", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D2 = Room("Dungeon", "D7", "D5", None, "D6", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D3 = Room("Dungeon", "D1", "D8", None, "D5", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D4 = Room("Dungeon", "D7", "D2", None, "D6", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D5 = Room("Dungeon", "D3", "D7", None, "D1", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D6 = Room("Dungeon", "D1", "D8", None, "D2", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D7 = Room("Dungeon", "D8", "D4", None, "D2", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D8 = Room("Dungeon", "D3", "D5", "D9", "D4", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D9 = Room("Dungeon", "inside_forest", None, None, None, None, None, "You see that there are three teleporters here, one"
                                                                    " to the north, east, and west")

Boss = Room("Boss Room.", "Chest", None, "inside_forest", None, None, None,
            "You see a big ogre. "
            "He is breathing heavily and has a wound on his leg.", None, 0)

Chest = Room("In front of treasure chest", None, None, "Boss", None, None, None,
             "After killing the ogre, you are in front of a chest. "
             "It is creaked open.", my_Joycons)

Desert = Room("Desert", "Front_of_Pyramid", "center", "Oasis", "Cactus", None, None,
              "You walked far enough and are now in a desert. "
              "It's really hot and you could possibly die staying in here to long."
              "You would need some type of animal to travel through the desert without dying of exhaustion")

Oasis = Room("???", "Desert", None, "Spikes", None, None, None,
             "You have reached a place filled with water and trees."
             "You have the urge to jump in. Just got to go south...")

Spikes = Room("Spikes/Ded", None, None, None, None, None, None,
              "You died after jumping into the 'water', but can't be blamed. "
              "You were dizzy, super hot, wanted water to satisfy you. Sadly you died."
              "No one will miss you, and this adventure is over super quickly."
              "Ha. Ha. HAAAAAaaa..."
              "OK time to try again.")

Cactus = Room("In front of a cactus", None, "Desert", None, None, None, None,
              "You are in front of a totally normal cactus.", secret_Cactus)

Front_of_Pyramid = Room("In front of Upside down Pyramid", "Inside_pyramid", "Right_of_Pyramid", "Desert",
                        "Left_of_Pyramid", None, None,
                        "The pyramid is somewhat buried inside the sand."
                        "You see the entrance but can't enter it. "
                        "The door seems slammed shut, but no where to open it."
                        "Oh well? Might as well go back..")

Right_of_Pyramid = Room("Right of Pyramid", None, "Back_of_Pyramid", None, "Front_of_Pyramid", None, None, "")

Left_of_Pyramid = Room("Left of Pyramid", None, "Front_of_Pyramid", None, "Back_of_Pyramid", None, None, "")

Back_of_Pyramid = Room("Back of Pyramid", None, "Left_of_Pyramid", None, "Right_of_Pyramid", None, None, "")

Inside_pyramid = Room("Inside the Pyramid", None, "P1", "Front_of_Pyramid", None, None, None,
                      "Surprisingly you're inside and it's actually pretty dull."
                      "You see ladders around leading 'UP' to a hole in the ceiling."
                      "Looks like a lot of floors.")

P1 = Room("Inside the Pyramid", None, None, None, "Inside_pyramid", "P2", None, "")

P2 = Room("Inside the Pyramid", "P3", None, None, None, None, "P1", "")

P3 = Room("Inside the Pyramid", None, None, "P2", "P4", None, None, "")

P4 = Room("Inside the Pyramid", None, "P3", None, None, "P5", None, "")

P5 = Room("Inside the Pyramid", "P6", None, None, None, None, "P4", "")

P6 = Room("Inside the Pyramid", None, None, "P5", None, "Top_of_Pyramid", None, "")

Top_of_Pyramid = Room("Top of Pyramid", None, None, None, None, None, "P6",
                      "You are on top of the upside down pyramid, weird. You see the game controller in front of you."
                      "To get down there are two ways. You can go through the pyramid, or jump into this pool you see "
                      "at the very bottom. It looks deep enough to survive.", my_GamecubeController)

Boss.enemy = ogre
# players
player = Player("You", 999, my_gloves, center)

playing = True
directions = ["north", "south", "east", "west", "up", "down"]
short_directions = ["n", "s", "e", "w", "u", "d"]


# Controller
while playing:
    player.current_location.visit += 1
    print(player.current_location.name)
    if player.current_location.visit < 2:
        print(player.current_location.description)
    if player.current_location.item is not None:
        print("There is a %s in here" % player.current_location.item.name)
    if player.current_location.money is not None:
        print("There is $%d here" % player.current_location.money)

    command = input(">_")
    if command in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
#   if current_node == world_map['CHEST']: # CHANGING DESCRIPTION
#    world_map["BOSS"]["DESCRIPTION"] = "Boss is dead"  # BOSSES ^
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.lower() in directions:
        try:
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]
            player.move(room_object)
        except KeyError:
            print("I can't go that way.")
        except AttributeError:
            print("This does not exist")
    elif command.lower() in ["get money", "take money"]:
        player.money += player.current_location.money
        print("You picked up $%d" % player.current_location.money)
        player.current_location.money = 0
    elif "attack" in command:
        new_target = command[7:]
        current_target = None
        if player.current_location.enemy is not None:
            if player.current_location.enemy.name == new_target:
                current_target = player.current_location.enemy
        if issubclass(type(current_target), Character):
            player.attack(current_target)
            print("")
            current_target.attack(player)
            print("")
        elif current_target is None:
            print("That doesnt exist!")
        else:
            print("You can't attack it")
    elif command.lower()in ["look", "look around", "l"]:
        print(player.current_location.description)
    elif command.lower() in ["check bag", "i", "b", "inventory"]:
        for itemy in player.inventory:
            print(itemy.name)
        else:
            print("You have no items")
    elif "equip" in command:
        item_name = command[6:]
        equip(item_name)

    elif "pick up" in command:
        item_name = command[8:]
        take(item_name)

    elif "take" in command:
        item_name = command[5:]
        take(item_name)

    elif "drop" in command:
        item_name = command[5:]
        drop(item_name)

    elif "place down" in command:
        item_name = command[11:]
        drop(item_name)

    elif command.lower() in ["shop", "buy"]:
        if isinstance(player.current_location.shop, Shop):
            player.current_location.shop.ask()

    else:
        print("Command Not Recognized")
