# From ophir:
# Variables for cell
default whyHere = 0
default moneyString = ""
default moneyInt = 0

label cell:
    scene cell
    show y at left
    y "Where am I??"
    hide y
    show c at right
    with dissolve
    c "Hey man, what's your name?"
    hide c
    show y at left
    menu:
        "I don't know my name, I don't know anything":
            hide y
            show c at right
            c "You're crazy, at least you know why you're here?"
        "Enter your name":
            python:
                playersName = renpy.input("What is your name?")
                playersName = playersName.strip()
            hide y
            show c at right
            c "What do they think you did?"
    hide c
    show y at left
    menu:
        "I don't know":
            hide y
            show c at right
            c "Classic. Good luck"
            jump guard
        "I stole money from a Chinese restaurant":
                $ whyHere = 1
        "I killed someone":
                $ whyHere = 2
        "None of your business":
                $ whyHere = 3
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
            "No":
                hide y
                show c at right
                c "Classic. Good luck"
                jump guard
            "Yes":
                if whyHere == 1:
                    hide y
                    show c at right
                    c "How much?"
                    hide c
                    show y at left
                    menu:
                        "More than you can think of":
                            hide y
                            show c at right
                            c "Wow, I could use some money"
                            jump guard
                        "Not that much":
                            hide y
                            show c at right
                            c "Too bad, I could use some money"
                            jump guard
                        "Why? You want some?":
                            hide y
                            show c at right
                            c "Yes, maybe I can help you for a nice amount of money"
                            $ i = 0
                            while i < 3:
                                hide c
                                show y at left
                                python:
                                    moneyString = renpy.input("How much do you want to tell him?\n(between 0 to 10000)", allow="0123456789")
                                    moneyString = moneyString.strip()
                                    try:
                                        moneyInt = int(moneyString)
                                    except ValueError:
                                        moneyInt = 0
                                if moneyInt >= 4500 and moneyInt <= 5500:
                                    hide y
                                    show c at right
                                    c "Yeah that will do it, I heard the guard has a mistress inside prison, her name is Rachel"
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
                            jump guard
