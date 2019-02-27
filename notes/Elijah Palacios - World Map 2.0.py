class Room(object):
    def __init__(self, name, north, east, south, west, up, down, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.entity = []


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 999

    def move(self, newlocation):
        """

        :param newlocation: The variable containing a room object
        """
        self.current_location = newlocation


class boss(object):
    def __init__(self, description):
        self.health = 200
        self.description = description


pig = boss("piglafer")

center = Room("Center of The World.", "forest", "portal", None, "Desert", None, None,
              "A 10K TV is in front of you with SmashBros on. "
              "There are 8 open spots to play, but no controllers. "
              "There are 4 different ways to go.")

portal = Room("Entrance to portal.", None, "mountains", None, "center", None, None,
              "A weird portal(looking like a nether portal from minecraft). "
              "You feel a cold breeze coming from the other side.")

mountains = Room("Middle of snowy mountain", "peak_of_mountain", "cavern", "base_of_mountain", "portal", None, None,
                 "The portal led to the middle of a mountain. "
                 "You see the peak and base of the mountain. "
                 "You also see a cavern east.")

peak_of_mountain = Room("Peak of The Snowy Mountain", None, None, "mountains", None, None, None,
                        "You climbed up the mountain. "
                        "Your index finger is purple.")

cavern = Room("Inside the cavern", None, None, None, "mountains", None, None,
              "You see this buff, ripped Pikachu behind the counter. "
              "It is the owner of this shop. "
              "It yells 'PIKA PIKA' in a deep voice. "
              "You see a horse. It looks wounded.")

base_of_mountain = Room("The base of the Snowy Mountain", "mountains", None, None, None, None, None,
                        "You climbed down the mountain. "
                        "You see an entrance with a staircase leading down.")

forest = Room("Entrance to Forest", "inside_forest", None, "Center", None, None, None,
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
          "To leave, you assume you can take any direction to be taken back to the entrance of the lost woods.")

Dungeon = Room("Dungeon", None, "inside_forest", None, None, None, None,
               "You're inside a dark somewhat smelly dungeon."
               " Careful, traps might be here. To go through you would need a key to enter.")
                       #
D1 = Room("Dungeon", "D3", "D6", None, "D4", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D2 = Room("Dungeon", "D7", "D5", None, "D6", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")
                                        #
D3 = Room("Dungeon", "D1", "D8", None, "D5", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D4 = Room("Dungeon", "D7", "D2", None, "D6", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")
                            #
D5 = Room("Dungeon", "D3", "D7", None, "D1", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D6 = Room("Dungeon", "D1", "D8", None, "D2", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")
                       #
D7 = Room("Dungeon", "D8", "D4", None, "D2", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")
                                  #
D8 = Room("Dungeon", "D3", "D5", "D9", "D4", None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

D9 = Room("Dungeon", "inside_forest", None, None, None, None, None, "You see that there are three teleporters here, one to the"
                                                         " north, east, and west")

Boss = Room("Boss Room.", "Chest", None, "inside_forest", None, None, None,
            "You see a big ogre. "
            "He is breathing heavily and has a wound on his leg.")

Chest = Room("In front of treasure chest", None, None, "Boss", None, None, None,
             "After killing the ogre, you are in front of a chest. "
             "It is creaked open.")

Desert = Room("Desert", "Front_of_Pyramid", "Center", "Oasis", "Cactus", None, None,
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
              "You are in front of a totally normal cactus.")

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
                      "at the very bottom. It looks deep enough to survive.")

player = Player(center)
Boss.entity = [pig]

playing = True
directions = ["north", "south", "east", "west", "up", "down"]

# Controller
while playing:
    print(player.current_location.entity)
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
#   if current_node == world_map['CHEST']: # CHANGING DESCRIPTION
#    world_map["BOSS"]["DESCRIPTION"] = "Boss is dead"  # BOSSES ^
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.lower() in directions:
        try:
            # command = "north"
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]

            player.move(room_object)
        except KeyError:
            print("I can't go that way.")
        except AttributeError:
            print("This does not exist")
    else:
        print("Command Not Recognized")