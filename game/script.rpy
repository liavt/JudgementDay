# Only GLOBALS

# Background images
image courthouse = "bg court house.jpg"
image cell = "bg prison cell"

# character sprites
image c = "sprite cellmate.png"
image g = "sprite guard.png"
image l = "sprite lawyer small.png"
image p = "sprite prosecutor.png"
image j = "sprite judge.png"
image b = "sprite bartender.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define c = Character("Cellmate")
define g = Character("Guard")
define l = Character("Lawyer")
define p = Character("Prosecutor")
define j = Character("Judge")
define b = Character("Bartender")

# The game starts here.

label start:
    jump cell
    return
