# The script of the game goes in this file.

# From liav:
# Variables for court:
# Set these before
default hasWallet = False
default hasBeer = False
default hasFingerprints = False
default playersName = ""
default talkedToLawyer = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define c = Character("Cellmate")
define g = Character("Guard")
define l = Character("Lawyer")
define p = Character("Prosecutor")
define j = Character("Judge")
define b = Character("Bartender")

# Background images
image courthouse = "BG_Court House2.jpg"

# character sprites
image cellmate = "sprite cellmate.png"
image guard = "sprite guard.png"
image lawyer = "sprite lawyer.png"
image prosecutor = "sprite prosecutor.png"
image judge = "sprite judge.png"
image bartender = "sprite bartender.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene courthouse

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show y happy

    # These display lines of dialogue.

    y "You've created a new Ren'Py game."

    y "Once you add a story, pictures, and music, you can release it to the world!"
    jump court

    # This ends the game.

    return

# Courthouse code

default guilty = False

label court:
    scene bg courthouse
    show j
    j "Order, order!"
    j "We will now begin case #2158673"
    j "Our defendant: Adam Smith"
    if playersName.lower() != "adam smith":
        y "That's not my name!"
        "The judge looks confused"
        if playersName == "":
            y "Actually, I don't even remember what my name is..."
        else:
            y "My name is actually [playersName]."
        j "No, you must be mistaken. The docket says Adam Smith."
        j "If you have no more interruptions, let us continue with the trial."
    j "Representing the Restaurant _________, we have Prosecutor ______. You may now begin your interrogation of the defendant."
    jump courtwhy

label courtwhy:
    p "Hello, I will ask you some questions and you must answer nothing but the truth. Are you ready to begin?"
    menu:
        "Yes":
            p "Great, let's start with the first question."
        "No":
            p "Well we don't have much time, so I will continue. Hopefully you can keep up."
    p "First, why did you do it?"
    menu:
        "My long lost twin brother did it, not me!":
            p "This is an interesting claim..."
            jump courtalibi
        "I didn't do it!":
            jump courtalibi
        "I wasn't there!":
            jump courtalibi
        "Do what?":
            jump courtwhynoanswer
        "I plead the fifth?":
            jump courtwhynoanswer
        "I had debts I needed to pay.":
            p "To who?"
            menu:
                "The Mafia":
                    pass
                "The Government":
                    pass
                "Russia":
                    pass
                "My Family":
                    p "You must have a very turbulent family life..."
            p "We will have to do a further case in the future to prosecute them. We want to continue learning about you, so I will continue since you implied that you did it."
            $ guilty = True
            jump courtwhere

label courtalibi:
    p "Well, do you have an alibi?"
    show b
    p "We have a witness testify that he saw you walk through the door around the time of the robbery."
    p "He is the bartender of the place, so he was behind the counter."
    menu:
        "You have the wrong person!":
            jump courtalibifail
        "He made up the story!":
            jump courtalibifail
        "I simply wasn't there!":
            jump courtalibifail
        "He was drunk and confused me for someone else!":
            if hasBeer:
                l "Your honor, if we may raise some evidence to the claim the witness is making..."
                l "We found this beer bottle at the crime scene, behind the bartender's counter."
                b "Actually, now that you remind me, I did feel a bit hungover the night after..."
                l "Yes, clearly this settles the situation. The witness simply confused the defendant for someone who looked similar."
                p "But who would look so similar as to be confused by the witness?"
                l "We can get to that later. Right now, your honor, I request that we throw out this witness testimony as it's clearly not credible."
                j "Objection sustained. The testimony is no longer credible evidence. Prosecutor, continue with your next question."
                jump courtwhere
            else:
                jump courtalibifail

label courtalibifail:
    p "Not a very strong alibi, I have to be honest."
    p "There is a witness testimony against you and there is no evidence for your claim."
    p "I believe there is no doubt you were there, and the court should see this clearly."
    p "Onto my next question."
    $ guilty = True
    jump courtwhere

label courtwhynoanswer:
    p "Don't play dumb, we have a witness testifying they saw you."
    show b
    l "Your honor, my defendant does not have to answer a question if they don't want to."
    j "Correct. Prosecutor, continue to your next question."
    $ guilty = True
    jump courtwhere

label courtwhere:
    p "Where were you an hour before the robbery?"
    menu:
        "Preparing the escape vehicle":
            $ guilty = True
            p "Your honor, this aligns perfectly with the details of the robbery."
            p "This is strong evidence that the defendant is indeed guilty."
        "At the airport, flying in as a tourist":
            p "So you are a tourist to this area?"
            l "Yes, the defendant was a tourist. That explains why he went into a Chinese restaurant."
        "Watching TV and eating popcorn on my couch":
            p "Fairly classic excuse."
        "I don't really know...":
            jump courtwherefail
        "I plead the fifth":
            jump courtwherefail
    jump courtdna

label courtwherefail:
    $ guilty = True
    p "What will you tell me then? Classic guilty defendant, dodging every question."
    "The prosecutor looks annoyed."
    l "Your honor, it is within my client's rights."
    j "Correct, if the defendant refuses to answer a question, then you must move on to the next question."
    p "Fine."

label courtdna:
    p "We also found an almost perfect DNA match of the door handle of the restaurant. Do you have anything to say about this?"
