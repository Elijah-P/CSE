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


center = Room("Center of The World.", "Entrance to Forest.", "Entrance to portal.", None, "Desert", None, None,
              "A 10K TV is in front of you with SmashBros on. "
              "There are 8 open spots to play, but no controllers. "
              "There are 4 different ways to go.")

portal = Room("Entrance to portal.")

current_node = center
print(current_node.name)
