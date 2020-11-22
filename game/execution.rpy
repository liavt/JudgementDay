define timeLoopEffect = MultipleTransition([
    False, Fade(2, 2, 0, color="#fff"),
    "bg white.jpg", Pause(3.0),
    "bg white.jpg", ImageDissolve("bg timeLoop.jpg", 5),
    True
])

label execution:
    play music "execution.mp3" fadein 2.0
    scene execution with fade
    show y at left
    show l at right
    with dissolve
    l "Hey man, I'm sorry for what happened."
    l "I'm sure you tried your best."
    l "Sigh... Life is so cruel. You can't always get second chances in stuff like this."
    if not talkedToLawyer:
        l "But..."
        l "You know, had you have come to me and have been more prepared, this could have gone better."
        l "I know it's too late... But it's the least I could tell you."
        l "After all, it's your right to see your lawyer before a trial. The guards can't stop you if you insist enough."
    else:
        if hasFingerprints and hasBeer and hasWallet:
            l "It's just a shame, we had such good evidence from the crime scene."
            if mentionedBrother and not convincedAboutBrother:
                l "I liked your narrative that it was your twin brother, our evidence definitely agreed with it."
                l "But you just needed to nail the execution."
                l "While you had evidence that you didn't do it, you didn't have any evidence that it was actually your twin brother."
                l "I don't know how we could have gotten that information on our own though..."
                l "Maybe you should have asked around before the case more."
            else:
                l "You just didn't have a good enough narrative about who could have done it instead of you."
                l "You were able to prove that it wasn't you, you had no other... scapegoat... let's say to blame it on."
                l "If you had a second chance then maybe you should have tried to find who actually did the crime, it would be much more convincing."
            l "It was just not enough to convince them..."
            l "Oh well, that's it. Too late now."
        else:
            l "I don't think we had enough evidence from the crime scene, to be honest."
            l "If we had a second chance, I think we should have tried looking for more."
            l "Just a shame that you don't get second chances at things like this..."
    l "Just... have a good life up there, okay?"
    hide l with dissolve
    "Your lawyer leaves."
    show g at right
    with dissolve
    g "Your execution is in 10 minutes. Don't keep me waiting, I have some important... business.... to attend to."
    menu:
        g "Before we get to your execution, as is tradition, do you have any last words?"

        "YES":
            $ lastWords = renpy.input("Enter your last words:")
            $ lastWords = lastWords.strip()
            y "[lastWords]"
            g "Oh, I'm so touched by your words, maybe I won't execute you today."
            $ renpy.pause(1.5)
            g "...haha, just kidding, this is my favorite part of the day."
            g "Come on now, empty your pockets."
        "NO":
            g "Your loss, maybe it would have change my mind ablut your execution. Oh well, Come on now, empty your pockets."
        "[lastWords]" if lastWords is not "":
            g "Strange, I feel like I've heard it before, like a Déjà-vu."
            g "Come on now, empty your pockets."
    if repeats == 0:
        "You rummage around in your right pocket, until you feel a small object presiding there."
        "You take out the object, which is revealed to be a fortune cookie."
        y "Must have been from the Chinese restuarant."
        y "Might as well eat it at this point, right? It's the end, after all?"
    elif repeats == 1:
        "You remember the last time you were here, there was a fortune cookie in your right pocket."
        "You rummage around in your right pocket, until you feel a small object presiding there."
        "You take out the object, which is revealed to be a fortune cookie."
        y "Last time I did this, I woke up back in my cell."
        y "I guess, it won't hurt to try again."
        y "Anyways, the alternative is being executing, so let's see what happens."
    elif repeats == 2:
        "You remember the last time you were here, there was a fortune cookie in your right pocket."
        "You rummage around in your right pocket, until you feel a small object presiding there."
        "You take out the object, which is revealed to be a fortune cookie."
        y "If things hold out again, when I open this cookie, I should reawaken back in my cell."
        y "At least I seem to remember everything, but everyone else seems to think as if nothing ever happened..."
        y "It's very strange. Hey, at least I'm not dead!"
        y "Now, lets go see if the cookie keeps on giving..."
    else:
        y "Well, that didn't work out."
        y "At least I have another chance at my freedom."
        y "I think I have a better plan on what to do next time, let's see if it works out."
        y "Here we go..."
    hide g with dissolve
    "You crack open the cookie, revealing a thinly cut white paper, with a single fortune on it:"
    show screen fortune with dissolve
    pause (1)
    "{color=#f00}{b}{i}'Failure is the chance to do better next time.'{/i}{/b}{/color}"
    $ repeats = repeats + 1
    hide screen fortune with dissolve
    stop music fadeout 1.0
    play sound "time travel.flac"
    scene cell
    with timeLoopEffect
    jump cell

screen fortune:
    # modal True
    imagebutton:
        xpos 900
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "fortune.png"
