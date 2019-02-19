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

inside_forest = Room("")

current_node = center
print(current_node.name)
