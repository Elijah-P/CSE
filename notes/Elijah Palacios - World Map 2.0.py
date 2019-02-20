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

Lost_Woods = Room("Lost Woods", None, None, None, "inside_forest", None, None,
                  "There are a lot of paths. "
                  "Seems like if you go the wrong way you'll be brought back to the entrance")

Dungeon = Room("Dungeon", None, "inside_forest", None, None, None, None,
               "You're inside a dark somewhat smelly dungeon."
               " Careful, traps might be here")

Boss = Room("Boss Room.", "Chest", None, "inside_forest", None, None, None,
            "You see a big ogre. "
            "He is breathing heavily and has a wound on his leg.")

Chest = Room("In front of treasure chest", None, None, "Boss", None, None, None,
             "After killing the ogre, you are in front of a chest. "
             "It is creaked open.")

Desert = Room("Desert", "Front_of_Pyramid", "Center", "Oasis", "Cactus", None, None,
              "You walked far enough and are now in a desert. "
              "It's really hot and you could possibly die staying in here to long.")

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
                        "Left_of_pyramid", None, None,
                        "The pyramid is somewhat buried inside the sand."
                        "You see the entrance but can't enter it. "
                        "The door seems slammed shut, but no where to open it."
                        "Oh well? Might as well go back..")

Inside_pyramid = Room("Inside the Pyramid", None, "P1", None, None, None, None,
                      "Surprisingly you're inside and it's actually pretty dull."
                      "You see ladders around leading 'UP' to a hole in the ceiling."
                      "Looks like a lot of floors.")

P1 = Room("Inside the Pyramid", None, None, None,)

current_node = center
print(current_node.name)
