# Ebonfall Manor - Horror Game

import time

# Helper function for delays
def wait(seconds=1):
    time.sleep(seconds)

# Helper function for display text
def display_text(text):
    for line in text.split("\n"):
        print(line)
        # wait(1)
    print("\n")

# Start of the game
def intro():
    display_text("""
    Chapter 1: The Beginning
    ------------------------------------
    "As your carriage rocked along the tortuous path, the wind howled.
    Before you, Ebonfall Manor towered, its shadow extending across the foggy cliffs.
    The letter disintegrated under your fingers, a painful reminder that you were now the owner of this home."
    """)
    wait(2)
    first_action()

# Chapter 1 actions
def first_action():
    display_text("""
    You stand at the entrance of the crumbling Ebonfall Manor.
    What would you like to do?
    1. Enter the Manor.
    2. Run away.
    """)
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        enter_manor()
    else:
        display_text("You run away, but the curse of Ebonfall Manor follows you forever. The End.")
        return

# Chapter 2 - Exploring the basement
def enter_manor():
    display_text("""
    As you step inside, the atmosphere is suffocating. Shadows seem to move in the corner of your eyes.
    A ghostly servant appears and says, "Beware, evil powers reside in this manor. Venture downstairs to uncover the truth."
    """)
    wait(2)
    display_text("Do you:")
    display_text("""
    1. Go to the basement.
    2. Ignore the servant and explore the hallways upstairs.
    """)
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        basement()
    else:
        display_text("The hallways lead you into a never-ending maze, and you are consumed by the curse. The End.")
        return

def basement():
    display_text("""
    Chapter 2: The Basement
    ------------------------------------
    Once you were downstairs in the basement, the temperature dropped.
    Weird patterns carved onto the stone, and damp seeped through the walls.
    Whispers sounded the faintest all around you.
    """)
    wait(2)
    display_text("You discover a cursed artifact on an altar.")
    display_text("""
    Do you:
    1. Take the artifact.
    2. Leave it and escape the basement.
    """)
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        display_text("The artifact reveals a vision of your ancestor's dark rituals.")
        shifting_walls()
    else:
        display_text("You leave the artifact but awaken a malevolent spirit. It consumes you. The End.")
        return

# Chapter 3 - Shifting walls and reality
def shifting_walls():
    display_text("""
    Chapter 3: Shifting Reality
    ------------------------------------
    The manor's walls gave off the impression that they were alive.
    The shadows became longer and darker, and doors led to places that were not there before.
    Now the core of the manor lay open to you.
    """)
    wait(2)
    display_text("You must navigate the shifting rooms to locate an ancient journal.")
    display_text("""
    Do you:
    1. Follow the ghostly apparitions guiding your way.
    2. Search randomly through the distorted rooms.
    """)
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        dark_ritual()
    else:
        display_text("The rooms shift endlessly, and you are trapped in a nightmare forever. The End.")
        return

# Chapter 4 - Uncovering the ritual
def dark_ritual():
    display_text("""
    Chapter 4: The Ritual
    ------------------------------------
    With an unearthly wrath, the storm outside raged. 
    The ground shook as lightning struck the dimly lit hallways, creating bizarre shadows.
    Time was of the essence.
    """)
    wait(2)
    display_text("You piece together the journal pages and learn about the dark ritual that cursed your family.")
    display_text("""
    Do you:
    1. Prepare the ritual to banish the entity.
    2. Ignore the ritual and confront the entity directly.
    """)
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        final_confrontation(ritual=True)
    else:
        final_confrontation(ritual=False)

# Chapter 5 - Final confrontation
def final_confrontation(ritual):
    display_text("""
    Chapter 5: The Grand Ballroom
    ------------------------------------
    The last page of the journal burned in your palm. The air crackled with excitement as the chandelier moved overhead.
    The force responsible for the Ebonfall family's curse stood before you.
    """)
    wait(2)
    if ritual:
        display_text("You perform the ritual, and the entity screeches as it is banished. The curse is lifted. You survive.")
        display_text("The End. You have freed Ebonfall Manor.")
    else:
        display_text("You confront the entity directly, but its power overwhelms you. You are consumed by the curse.")
        display_text("The End.")

# Start the game
intro()