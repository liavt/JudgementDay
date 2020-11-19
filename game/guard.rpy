# From ophir:
# Variables for guard
default guardAccusation = ""
default hasRachel = ""

label guard:
    hide c
    with dissolve
    hide y
    with dissolve
    show g at right
    with dissolve
    show y at left
    with dissolve
    menu:
        g "Come with me inmate #[yourID], it's time for your trial!"

        "OK, fine......":
            hide y
            with dissolve
            show g at right
            with dissolve
            g "Now, turn against the wall and put your hands on it. If you do anything suspicions, I won't hesitate to use my taser gun"
            jump court
        "I didn't do it!!! I'm not going anywhere":
            hide y
            with dissolve
            show g at right
            with dissolve
            g "If won't come with me with me in the next 5 seconds, I'll have to use my taser gun on you, and trust me, you really don't want this..."
            hide g
            with dissolve
            show y at left
            with dissolve
            y "OK, fine..........."
            hide y
            with dissolve
            show g at right
            with dissolve
            g "Now, turn against the wall and put your hands on it. If you do anything suspicions, I won't hesitate to use my taser gun"
            jump court
        "Where am I? What trial?":
            hide y
            with dissolve
            show g at right
            with dissolve
            g "If won't come with me with me in the next 5 seconds, I'll have to use my taser gun on you, and trust me, you really don't want this..."
            jump court
        "Take me to the security room":
            hide y
            with dissolve
            show g at right
            with dissolve
            g "Haha, and why would I do such a thing???"
            hide g
            with dissolve
            show y at left
            with dissolve
            y "Because I know about what you did"
            hide y
            with dissolve
            show g at right
            with dissolve
            show y at left
            with dissolve
            menu:
                g "What are you talking about?!"

                "I know you have an affair with __________":
                    $ guardAccusation = "I know you have an affair with __________"
                "I know you stole the falafel from __________":
                    $ guardAccusation = "I know you stole the falafel from __________"
                "I know what you said to __________":
                    $ guardAccusation = "I know what you said to __________"
                "I know you killed __________":
                    $ guardAccusation = "I know you killed __________"
            $ i = 0
            while i < 3:
                hide g
                with dissolve
                show y at left
                python:
                    hasRachel = renpy.input(guardAccusation)
                    hasRachel = hasRachel.strip()
                hide y
                with dissolve
                show g at right
                with dissolve
                if guardAccusation == "I know you have an affair with __________" and "rachel" in hasRachel.lower():
                    g "Oh man, who told you about her, I'm going to make him miserable!!! \nAnyway, I'll take you there"
                    jump securityRoom
                elif guardAccusation == "I know you have an affair with __________" and i == 2:
                    g "Haha, you've got nothing on me, you're going to your execution as planned"
                    g "Now, turn against the wall and put your hands on it. If you do anything suspicions, I won't hesitate to use my taser gun"
                    jump court
                g "I don't know any [hasRachel]"
                $ i += 1
            hide y
            with dissolve
            show g at right
            with dissolve
            g "Haha, you've got nothing on me, you can say whatever you want, it's not true, you're going to your execution as planned"
            g "Now, turn against the wall and put your hands on it. If you do anything suspicions, I won't hesitate to use my taser gun"
        "I want to see my lawyer":
            menu:
                g "Haha, You do not deserve a lawyer, now come with me"

                "OK, fine......":
                    hide y
                    show g at right
                    g "Now, turn against the wall and put your hands on it. If you do anything suspicions, I won't hesitate to use my taser gun"
                    jump court
                "Yes I do, according to the law, I deserve to see him":
                    hide y
                    show g at right
                    g "Oh, you're familiar with the law, I didn't know about that, I'll take you to your lawyer"
                    $ talkedToLawyer = True
                    jump lawyer
