# Only GLOBALS

# Global variables
default hasWallet = False
default hasBeer = False
default hasFingerprints = False
default playersName = ""
default talkedToLawyer = False

# How many times time has looped
default repeats = 0

# Background images
image cell = "bg prison cell"
image courthouse = "bg court house.jpg"
image securityRoom = "bg security room.jpg"
image crimeScene = "bg crime scene.jpg"
image lawyerRoom = "bg lawyer.jpg"
image execution = "bg execution.jpg"
image freedom = "bg freedom.jpg"
image china = "bg china.jpg"

# character sprites
image y = "sprite player.png"
image c = "sprite cellmate.png"
image g = "sprite guard.png"
image l = "sprite lawyer.png"
image p = "sprite prosecutor.png"
image j = "sprite judge.png"
image b = "sprite bartender.png"
image t = "sprite evil.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define c = Character("Cellmate")
define g = Character("Guard")
define l = Character("Lawyer")
define p = Character("Prosecutor")
define j = Character("Judge")
define b = Character("Bartender")
define t = Character("Joshua")

# The game starts here.
label start:
    $ hasWallet = False
    $ hasBeer = False
    $ hasFingerprints = False
    $ talkedToLawyer = False
    jump cell
    return

default yourName = "Adam Smith"
default yourID = "106398772"
default twinsName = "Joshua"
default teinsID = "106398773"
default restaurntName = "Go GO Dim Sum"
default guardsName = "Mike"
default prosecutorsName = "Mark"
