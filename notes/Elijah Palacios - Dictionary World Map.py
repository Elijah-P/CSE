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
    ""
    "PATH2FOREST": {
        "NAME": "ENTRANCE TO FOREST",
        "DESCRIPTION": "There is a sign saying, "Beware of 
                       "In front of hyrule castle.",
        "PATHS": {
            "NORTH": "TOWER"
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
