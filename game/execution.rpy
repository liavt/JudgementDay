define timeLoopEffect = MultipleTransition([
    False, Fade(2, 2, 0, color="#fff"),
    "bg white.jpg", Pause(3.0),
    "bg white.jpg", ImageDissolve("bg timeLoop.jpg", 5),
    True
])

label execution:
    scene execution
    show y at left
    show l at right
    with dissolve
    if not talkedToLawyer:
        l "Hey man, I'm sorry for what happened."
        l "You know, had you have come to me and have been more prepared, this could have gone better."
        l "I know it's too late... But it's the least I could tell you."
        l "After all, it's your right to see your lawyer before a trial. The guards can't stop you."
    l "Just... have a good life up there, okay?"
    hide l with dissolve
    "Your lawyer leaves."
    show g at right
    with dissolve
    g "Your execution is in 10 minutes. Don't keep me waiting, I have some important... business.... to attend to."
    g "Come on, empty your pockets."
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
    "You crack open the cookie, revealing a thinly cut white paper, with a single fortune on it:"
    "'Failure is the chance to do better next time.'"
    $ repeats = repeats + 1
    scene cell
    with timeLoopEffect
    jump start
