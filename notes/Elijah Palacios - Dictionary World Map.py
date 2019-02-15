world_map = {
    "CENTER": {
        "NAME": "Center of The World.",
        "DESCRIPTION": "A 10K TV is in front of you with SmashBros on. "
                       "There are 8 open spots to play, but no controllers. "
                       "There are 4 different ways to go.",
        "PATHS": {
            "NORTH": "FOREST",
            "EAST": "PORTAL",
            "SOUTH": "RANDOM",  # NOT MADE YET
            "WEST": "DESERT",
            "UP": "GOD",    # NOT MADE YET
            "DOWN": "CAVE"  # NOT MADE YET
        }
    },
    "PORTAL": {
        "NAME": "Entrance to portal.",
        "DESCRIPTION": "A weird portal(looking like a nether portal from minecraft). "
                       "You feel a cold breeze coming from the other side.",
        "PATHS": {
            "EAST": "MOUNTAINS",
            "WEST": "CENTER"
        }
    },
    "MOUNTAINS": {
        "NAME": "Middle of snowy mountain",
        "DESCRIPTION": "The portal led to the middle of a mountain. "
                       "You see the peak and base of the mountain. "
                       "You also see a cavern east.",
        "PATHS": {
            "NORTH": "PEAK OF MOUNTAIN",
            "EAST": "CAVERN",
            "SOUTH": "BASE OF MOUNTAIN",
            "WEST": "PORTAL"
        }
    },
    "PEAK OF MOUNTAIN": {
        "NAME": "Peak of the Snowy Mountain.",
        "DESCRIPTION": "You climbed up the mountain. "
                       "Your index finger is purple.",
        "PATHS": {
            "SOUTH": "MOUNTAINS"
        }
    },
    "CAVERN": {
        "NAME": "Inside the cavern",
        "DESCRIPTION": "You see this buff, ripped Pikachu behind the counter. "
                       "It is the owner of this shop. "
                       "It yells 'PIKA PIKA' in a deep voice. "
                       "You see a horse. It looks wounded.",
        "PATHS": {
            "WEST": "MOUNTAINS"
        }
    },
    "BASE OF MOUNTAIN": {
        "NAME": "The base of the Snowy Mountain.",
        "DESCRIPTION": "You climbed down the mountain. "
                       "You see an entrance with a staircase leading down.",
        "PATHS": {
            "NORTH": "MOUNTAINS"
        }
    },
    "FOREST": {
        "NAME": "Entrance to Forest.",
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

    },
    "LOST WOODS": { # WORK LATER
        "NAME": "Lost Woods",
        "DESCRIPTION": "There are a lot of paths. "
                       "Seems like if you go the wrong way you'll be brought back to the entrance",
        "PATHS": {
            "WEST": "INSIDE FOREST"
        }
    },
    "DUNGEON": { # WORK LATER
        "NAME": "Dungeon",
        "DESCRIPTION": "You're inside a dark somewhat smelly dungeon."
                       " Careful, traps might be here",
        "PATHS": {
            "EAST": "INSIDE FOREST"

        }
    },
    "BOSS": {
        "NAME": "Boss Room.",
        "DESCRIPTION": "You see a big ogre. "
                       "He is breathing heavily and has a wound on his leg.",
        "PATHS": {
            "NORTH": "CHEST",
            "SOUTH": "INSIDE FOREST"
        }
    },
    "CHEST": {
        "NAME": "In front of treasure chest",
        "DESCRIPTION": "After killing the ogre, you are in front of a chest. "
                       "It is creaked open.",
        "PATHS": {
            "SOUTH": "BOSS"
        }
    },
    "DESERT": {
        "NAME": "Desert",
        "DESCRIPTION": "You walked far enough and are now in a desert. "
                       "It's really hot and you could possibly die staying in here to long.",
        "PATHS": {
            "NORTH": "FRONT OF PYRAMID",
            "EAST":  "CENTER",
            "SOUTH": "OASIS",
            "WEST": "CACTUS"
        }
    },
    "OASIS": {
        "NAME": "???",
        "DESCRIPTION": "You have reached a place filled with water and trees."
                       "You have the urge to jump in. Just got to go south...",
        "PATHS": {
           "SOUTH": "SPIKES",
           "NORTH": "DESERT"
        }
    },
    "SPIKES": {
        "NAME": "Spikes/Ded",
        "DESCRIPTION": "You died after jumping into the 'water', but can't be blamed. "
                       "You were dizzy, super hot, wanted water to satisfy you. Sadly you died."
                       "No one will miss you, and this adventure is over super quickly."
                       "Ha. Ha. HAAAAAaaa..."
                       "OK time to try again."
    },
    "CACTUS": {
        "NAME": "In front of a cactus",
        "DESCRIPTION": "You are in front of a totally normal cactus.",
        "PATHS": {
            "EAST": "DESERT"
        }
    },
    "FRONT OF PYRAMID": {
        "NAME": "In front of Upside down Pyramid",
        "DESCRIPTION": "The pyramid is somewhat buried inside the sand."
                       "You see the entrance but can't enter it. "
                       "The door seems slammed shut, but no where to open it."
                       "Oh well? Might as well go back..",
        "PATHS": {
            "SOUTH": "DESERT",
            "EAST": "RIGHT OF PYRAMID",
            "WEST": "LEFT OF PYRAMID",
            "NORTH": "INSIDE PYRAMID"
        }
    },
    "INSIDE PYRAMID": {
        "NAME": "Inside the pyramid",
        "DESCRIPTION": "Surprisingly you're inside and it's actually pretty dull."
                       "You see ladders around leading 'UP' to a hole in the ceiling."
                       "Looks like a lot of floors.",
        "PATHS": {
            "EAST": "P1"
        }
    },
    "P1": {
        "NAME": "Inside the pyramid",
        "DESCRIPTION": "",
        "PATHS": {
            "UP": "P2"
        }
    },
    "P2": {
        "NAME": "Inside the pyramid",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "P3"
        }
    },
    "P3": {
        "NAME": "Inside the pyramid",
        "DESCRIPTION": "",
        "PATHS": {
            "WEST": "P4"
        }
    },
    "P4": {
        "NAME": "Inside the pyramid",
        "DESCRIPTION": "",
        "PATHS": {
            "UP": "P5"
        }
    },
    "P5": {
        "NAME": "Inside the pyramid",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "P6"
        }
    },
    "RIGHT OF PYRAMID": {
        "NAME": "Right of pyramid",
        "DESCRIPTION": "There is nothing unordinary here.",
        "PATHS": {
            "WEST": "FRONT OF PYRAMID",
            "EAST": "BACK OF PYRAMID"
        }
    },
    "LEFT OF PYRAMID": {
        "NAME": "Left of pyramid",
        "DESCRIPTION": "There is nothing unordinary here.",
        "PATHS": {
            "WEST": "BACK OF PYRAMID",
            "EAST": "FRONT OF PYRAMID"
        }
    },
    "BACK OF PYRAMID": {
        "NAME": "Back of Pyramid",
        "DESCRIPTION": "There is nothing unordinary here.",
        "PATHS": {
            "WEST": "RIGHT OF PYRAMID",
            "EAST": "LEFT OF PYRAMID"
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
    if current_node == world_map['CHEST']: # CHANGING DESCRIPTION
        world_map["BOSS"]["DESCRIPTION"] = "Boss is dead"  # BOSSES ^
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
