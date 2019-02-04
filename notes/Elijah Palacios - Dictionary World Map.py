world_map = {
    "CENTER": {
        "NAME": "Center of The World.",
        "DESCRIPTION": "A 10K TV is in front of you with SmashBros on. "
                       "There are 8 open spots to play, but no controllers. "
                       "There are 4 different ways to go.",
        "PATHS": {
            "NORTH": "FOREST",
            "EAST": "PORTAL",
            "SOUTH": "RANDOM",
            "WEST": "DESERT",
            "UP": "GOD",
            "DOWN": "CAVE"
        }
    },
    "PORTAL": {
        "NAME": "Entrance to portal.",
        "DESCRIPTION": "A weird portal(looking like a nether portal from minecraft). "
                       "You feel a cold breeze coming from the other side.",
        "PATHS": {
            "EAST": "MOUNTAINS.",
            "WEST": "CENTER"
        }
    },
    "FOREST": {
        "NAME": "Entrance to Forest. ",
        "DESCRIPTION": "There is a sign saying, 'D-NT -ET -OST.' "
                       "Letters are missing on the sign. Fog surrounds the entrance.",
        "PATHS": {
            "NORTH": "INSIDE FOREST",
            "SOUTH": "CENTER"
        }
    },
    "INSIDE FOREST": {
        "NAME": "Inside the Forest.",
        "DESCRIPTION": "There are 3 paths. "
                       "You hear a roaring noise from the northern path",
        "PATHS": {
            "NORTH": "BOSS",
            "EAST": "LOST WOODS",
            "SOUTH": "FOREST",
            "WEST": "DUNGEON"
        }

    }
}

# Other Variables
current_node = world_map["CENTER"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# Controller
while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node["PATHS"][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")
