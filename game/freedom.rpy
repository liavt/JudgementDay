label freedom:
    scene freedom
    show y
    y "Wow that was weird..."
    y "I wonder what was the reason for that time loop."
    y "If it was the fortune cookie, just to be safe, I'm not opening it again..."
    y "I bet no one will ever believe me about this whole ordeal!"
    y "...and my parents have some explaining to do"
    hide y with squares
    pause(1.5)
    show y2 with squares
    y "So good to be free..."
    hide y2 with dissolve
    scene cell with fade
    show t2 with dissolve
    "You won!!! Well done, you made sure that your evil twin is now behind bars!"
    "You can now enjoy your life, worries free."
    t "Just wait when I get out of prison Adam, I'm going to make you miserable"
    t "You won't be able to sleep at night, I can asure you that!"
    hide t2
    scene freedom
    show y2 with dissolve
    "So maybe not totally free, but at least for now you can. Enjoy it while it last!"
    pause(1.5)
    "YOU WIN!!!"
    $ renpy.full_restart()
