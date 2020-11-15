# From ophir:
# Variables for cell
default whyHere = 0
default moneyString = ""
default moneyInt = 0

label cell:
    scene cell
    y "Where am I??"
    show c at right
    with dissolve
    c "Hey man, what's your name?"
    menu:
        "I don't know my name, I don't know anything":
            c "You're crazy, at least you know why you're here?"
        "Enter your name":
            python:
                playersName = renpy.input("What is your name?")
                playersName = playersName.strip()
            c "What do they think you did?"
    menu:
        "I don't know":
            c "Classic. Good luck"
            jump guard
        "I stole money from a Chinese restaurant":
            python:
                whyHere = 1
        "I killed someone":
            python:
                whyHere = 2
        "Non of your business":
            python:
                whyHere = 3
    c "Did you do it?"
    if whyHere == 3:
        y "I told you, it's non of your business!"
        jump guard
    else:
        menu:
            "No":
                c "Classic. Good luck"
                jump guard
            "Yes":
                if whyHere == 1:
                    c "How much?"
                    menu:
                        "More than you can think of":
                            c "Wow, I could use some money"
                            jump guard
                        "Not that much":
                            c "Too bad, I could use some money"
                            jump guard
                        "Why? You wnat some?":
                            c "Yes, maybe I can help you for a nice amount of money"
                            default i = 0
                            while i < 3:
                                python:
                                    moneyString = renpy.input("How much does your cellmate want?\n(between 0 to 10000)", allow="0123456789")
                                    moneyString = playersName.strip()
                                    try:
                                        moneyInt = int(moneyString or 0)
                                    except ValueError:
                                        moneyInt = 0
                                c "[moneyInt]"
                                if moneyInt >= 4500 or moenyInt <= 5500:
                                    c "Yeah that will do it, I heard the guard has a mistress inside prison, her name is Rachel"
                                elif moneyInt > 5500:
                                    c "Even less will be fine"
                                else:
                                    c "Haha, try harder, I believe you can give me much more money"
                                $ i += 1
                            jump guard

label guard:
    hide c
    show g at right
    g "Come with me inmate #67584, it's time for your trial!"
