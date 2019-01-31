world_map = {
    "CENTER": {
        "NAME": "Center of The World.",
        "DESCRIPTION": "This is the center of the current world you're in. "
                       "There are 4 different paths visible.",
        "PATHS": {
            "NORTH": "ZELDA",
            "EAST": "MARIO",
            "SOUTH": "RANDOM",
            "WEST": "POKEMON",
            "UP": "GOD",
            "DOWN": "CAVE"
        }
    },
    "ZELDA": {
        "NAME": "Hyrule castle.",
        "DESCRIPTION": "In the Zelda world. "
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
        