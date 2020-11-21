# From ophir:
# Variables for cell
default whyHere = 0
default moneyString = ""
default moneyInt = 0

label cell:
    play music "cell.mp3" fadein 1.0
    scene cell
    pause(1)
    $ renpy.block_rollback()
    show y at left
    with dissolve

    if repeats > 0:
        $ renpy.take_screenshot()
        $ renpy.save("1-" + str(repeats), "Loop #" + str(repeats))

    if repeats == 1:
        y "Huh, I didn't die?"
        y "What the...."
        y "I'm back in the cell?"
        y "I'm supposed to be dead..."
    elif repeats == 2:
        y "Again, I'm back..."
        y "It's like, every time I am about to die, I come back here."
        y "It has to be the darn fortune cookie!"
        y "But I wonder what could end the loop..."
    elif repeats == 3:
        y "Like expected, I'm back to the cell."
        y "Will I ever leave the loop? I hope."
        y "At least I should know more than last time."
        y "If I'm stuck here forever, I might as well take the time to discover the real truth..."
        y "Maybe I'm innocent after all, and with the right knowledge, I can convince the court too!"
    elif repeats >= 4:
        y "I'm back to the start."
        y "From my memory, I think this is time loop #[repeats]?"
        y "I hope it doesn't run out, I really don't want to die..."
    else:
        y "Where am I??"
    hide y
    with dissolve
    show c at right
    with dissolve
    c "Hey man, what's your name?"
    hide c
    with dissolve
    show y at left
    with dissolve
    if repeats == 1:
        y "Wait, don't you remember what happened?"
        y "I'm supposed to be dead!"
        show c at right
        with dissolve
        c "Nah man, you must be crazy."
        c "You just showed up, cops brought you in 10 minutes ago."
        c "Look very much alive to me, maybe not for long."
        y "No no... I already talked to you. I went to trial."
        y "They found me guilty... and then I was supposed to be executed."
        y "And now... I'm here! And you don't remember a thing?"
        c "Nope. You must have had a bad dream or something, I don't know."
        c "Before you go full cuckoo, what's your name at least?"
        hide c
    menu:
        c "What is your name?"

        "I don't know my name, I don't really remember anything..":
            hide y
            show c at right
            c "You're crazy, do you at least you know why you're here?"
        "Enter your name":
            python:
                playersName = renpy.input("What is your name?")
                playersName = playersName.strip()
            hide y
            show c at right
            c "So, [playersName], what do they think you did?"
    # Reason for prison
    hide c
    show y at left
    if repeats == 1:
        show y at center
        y "(To yourself) It looks like he doesn't remember anything..."
        y "He is giving the same responses as last time."
        y "Maybe this is some sort of time loop?"
        y "But why do I remember the last loop, but he doesn't?"
        y "It's like the whole world reset but myself."
        y "I wonder if I can use this to my advantage..."
        hide y
        show c at right
        c "Hey! Don't ignore me like that!"
        hide c
    show y at left
    menu:
        c "What do they think you did?"

        "I don't know":
            hide y
            show c at right
            c "Classic response. Good luck"
            jump guard
        "I stole money from a Chinese restaurant":
                $ whyHere = 1
        "I killed someone":
                $ whyHere = 2
        "None of your business":
                $ whyHere = 3
    # Did it or not
    hide y
    show c at right
    c "Did you do it?"
    if whyHere == 3:
        hide c
        show y at left
        y "I told you, it's none of your business!"
        jump guard
    else:
        hide c
        show y at left
        menu:
            c "Did you do it?"

            "No":
                hide y
                show c at right
                c "Classic. Good luck."
                jump guard
            "Yes":
                if whyHere == 1:
                    hide y
                    show c at right
                    show y at left
                    # Money loop
                    menu:
                        c "How much?"

                        "More than you can think of":
                            hide y
                            show c at right
                            menu:
                                c "Wow, I could use a couple thousand right now."
                                "Too bad you aren't getting any!":
                                    c "No need to rub it in my face like that. After all, we are both in prison."
                                    jump guard
                                "I could give you some... in exchange for some dirt on this place.":
                                    c "That could be a good exchange."
                                    c "How much are you offering?"
                                    jump celloffermoney
                        "Not that much":
                            hide y
                            show c at right
                            c "Too bad, I could use a couple thousand right about now."
                            jump guard
                        "Why? You want some?":
                            hide y
                            show c at right
                            c "Yes, maybe I can help you for a nice sum of money"
                            jump celloffermoney
                elif whyHere == 2:
                    hide y
                    show c at right
                    c "Well, don't kill me, okay?"
                    c "Good luck at your court."
                elif whyHere == 3:
                    hide y
                    show c at right
                    c "You did do the crime, but you won't tell me what it is? Harsh."
                jump guard

label celloffermoney:
    $ i = 0
    while i < 3:
        hide c
        show y at left
        python:
            moneyString = renpy.input("How much money do you want to tell him?\n(between 0 to 10000)", allow="0123456789")
            moneyString = moneyString.strip()
            try:
                moneyInt = int(moneyString)
            except ValueError:
                moneyInt = 0
        if moneyInt >= 4500 and moneyInt <= 5500:
            hide y
            show c at right
            c "Yeah that will do it."
            menu:
                c "As long as you promise to give me the money afterwards, I can help you."
                "Sure":
                    c "I heard the guard for your cell has a mistress inside prison, her name is {color=#34bdeb}Rachel{/color}."
                    c "Rachel is the warden's fiancé."
                    c "If he finds out, the guard is surely done for."
                    c "I'm sure you can threaten him with this info to get some access to places you normally... shouldn't."
                    c "Hack into the system or something, could help you in you case."
                    show y at left
                    y "Isn't that illegal? I'm already in prison."
                    c "I mean, what do you have to lose? Either you hack into the system and cheat yourself to an innocent sentence..."
                    c "...or you get executed."
                    c "Look, the choice is yours. If you make it out alive though, you owe me that money."
                    c "Good luck man."
                    hide y
                    with dissolve
                "No way, the money's mine!":
                    c "Your loss."
                    c "Good luck, hopefully you wont get executed so you can use the money."
            jump guard
        elif moneyInt > 5500:
            hide c
            show y at left
            c "Nah, you are clearly faking it. No way you stole more than $5000 from a Chinese place."
        else:
            hide c
            show y at left
            c "Haha, try harder, I believe you can give me much more money. If you don't have more than a couple thousand, what's the point?"
        $ i += 1

label intro:
    scene prisonZoomOut with dissolve:
        ease 7 zoom 1.4
    pause (5)
    scene cell with dissolve
    jump cell
