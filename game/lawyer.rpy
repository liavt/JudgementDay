label lawyer:
    scene lawyerRoom
    show l at right with dissolve
    l "What would you like to talk to me about, my client?"
    show y at left with dissolve
    y "Sir, you are the best lawyer my money could afford. You got to help me with my situation."
    l "Today your trial is taking place, so there is not much we can do."
    l "Let me ask you the simplest but most difficult question there is."
    l "Did you do it?"
    menu:
        "NO":
            l "I had a feeling. I don't offer it usually, but I offer you to visit the crime scene for one last time.
            maybe you'll figure something out."
            y "Thank you sir, it means a lot to me."
            jump crimeSceneIntro
        "YES":
            l "I had a feeling. we will try our best today."
            l "May God be with you."
        "I don't know what you're talking about":
            l "Great tactic. Do you also want to claim temporary insanity?"
    hide l
    show g at center with dissolve
    g "Come on. Time has come to go to the courthouse."
    jump court

label crimeSceneIntro:
    scene crimeScene with fade
    pause(1)
    show screen goGoDimSumModal with dissolve
    pause(3)
    hide screen goGoDimSumModal with dissolve
    pause(1)
    show y at center
    y "So, I guess this is where this whole mess started."
    y "Let's search for some clues."
    hide y

label crimeScene:
    show screen fingerPrintsSensor
    show screen walletOnFloor
    show screen fortuneCookiesBowl
    show screen bottlesSensor
    show screen leaveButton
    show screen bonsaiSensor
    call screen restaurant


label money:
    show y at center
    y "My wallet is clearly empty.. I should keep it"
    $ hasWallet = True
    hide y
    jump crimeScene

label fingerprints:
    show y at center
    y "Look at those strange fingerprints. I'll keep them in mind."
    $ hasFingerprints = True
    hide y
    jump crimeScene

label bottles:
    # show y at center
    y "Someone drank this pink liqueur down to the bottom. It must have been the bartender."
    $ hasBeer = True
    hide y
    jump crimeScene

label fortune:
    python:
        list_of_fortunes = []
        list_of_fortunes.append("It never pays to kick a skunk.")
        list_of_fortunes.append("While you have this day, fill it with life. While you're in this moment, give it your own special meaning and purpose and joy.")
        list_of_fortunes.append("The measure of time to your next goal is the measure of your discipline.")
        list_of_fortunes.append("All troubles you have can pass away very quickly.")
        list_of_fortunes.append("YOUR FAILURES WILL LEAD YOU TO YOUR SUCCESS.")
        list_of_fortunes.append("Before the beginning of great brilliance, there must be chaos.")
        list_of_fortunes.append("If you take a single step to your journey, you'll succeed; it's not best to fail.")
        list_of_fortunes.append("Truth is an unpopular subject. Because it is unquestionably correct.")
        list_of_fortunes.append("All the world may not love a lover but they will be watching him.")
        list_of_fortunes.append("The human spirit is stronger than anything that can happen to it.")
        fortune = renpy.random.choice(list_of_fortunes)
    "{color=#f00}{b}{i}\"[fortune]\"{/i}{/b}{/color}"
    jump crimeScene

label leavePopUp:
    menu:
        "Call the lawyer":
            show y at left with dissolve
            show l at right with dissolve
            l "I hope you found what you were looking foor. let's go to the courthouse."
            jump court
        "Maybe I'm still missing something..":
            hide y
            jump crimeScene

screen restaurant:
    zorder 0

screen leaveButton:
    zorder 0
    imagebutton:
        xpos 0
        ypos 0
        idle "leave button.png"
        hover "leave button hover.png"
        action Hide("fingerPrintsSensor"), Hide("walletOnFloor"), Hide("fortuneCookiesBowl"), Hide("bottlesSensor"), Hide("bonsaiSensor"), Hide("leaveButton"), Jump("leavePopUp")

screen fingerPrintsSensor:
    zorder 0
    imagebutton:
        xpos 829
        ypos 463
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Show("fingerprints")

screen bottlesSensor:
    zorder 0
    imagebutton:
        xpos 1057
        ypos 363
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Show("bottlesModal")

screen bonsaiSensor:
    zorder 0
    imagebutton:
        xpos 663
        ypos 503
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Show("bonsaiModal")

screen walletOnFloor:
    zorder 0
    imagebutton:
        xpos 404
        ypos 680
        xanchor 0.5
        yanchor 0.5
        idle "wallet on floor.png"
        hover "wallet yellow.png"
        action Show("walletPicked"), Hide("walletOnFloor")

screen fortuneCookiesBowl:
    zorder 0
    imagebutton:
        xpos 270
        ypos 490
        xanchor 0.5
        yanchor 0.5
        idle "fortune cookies bowl small.png"
        hover "fortune cookies bowl small yellow.png"
        action Show("cookiePicked")


## MODALS

screen goGoDimSumModal:
    modal True
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "go go dim sum modal.png"

screen walletPicked:
    modal True
    on "hide" action Hide("displayTextScreen")
    zorder 1
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "wallet picked.png"
        hover "wallet picked.png"
    # X button
    imagebutton:
        xpos 380
        ypos 160
        xanchor 0.5
        yanchor 0.5
        idle "x button.png"
        hover "x button.png"
        action Hide("walletPicked"), Show("walletOnFloor")
    # open wallet sensoe
    imagebutton:
        xpos 765
        ypos 370
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Hide("walletPicked"), Show("walletOpened")



screen walletOpened:
    modal True
    on "hide" action Hide("displayTextScreen")
    zorder 1
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "wallet opened.png"
        hover "wallet opened.png"
    # X button
    imagebutton:
        xpos 380
        ypos 160
        xanchor 0.5
        yanchor 0.5
        idle "x button.png"
        hover "x button.png"
        action Hide("walletOpened"), Show("walletOnFloor")
    # ID sensor
    imagebutton:
        xpos 480
        ypos 300
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Hide("walletOpened"), Show("walletOpenedID")
    # # Money sensor
    # imagebutton:
    #     xpos 812
    #     ypos 207
    #     xanchor 0.5
    #     yanchor 0.5
    #     idle "empty.png"
    #     hover "yellow.png"
    #     action Show("displayTextScreen", displayText = "well, it's empty...", xPosition = 812, yPosition = 207)

screen walletOpenedID:
    modal True
    on "hide" action Hide("displayTextScreen")
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "wallet opened with id.png"
        hover "wallet opened with id.png"
    # X button
    imagebutton:
        xpos 380
        ypos 160
        xanchor 0.5
        yanchor 0.5
        idle "x button.png"
        hover "x button.png"
        action Hide("walletOpenedID"), Show("walletOnFloor")
    # Money sensor
    imagebutton:
        xpos 812
        ypos 207
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Hide("walletOpenedID"), Jump("money"), Show("displayTextScreen", displayText = "well, it's empty...", xPosition = 812, yPosition = 207)


screen cookiePicked:
    modal True
    on "hide" action Hide("displayTextScreen")
    zorder 1
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "fortune cookies closed modal.png"
        hover "fortune cookies closed modal.png"
    # X button
    imagebutton:
        xpos 380
        ypos 160
        xanchor 0.5
        yanchor 0.5
        idle "x button.png"
        hover "x button.png"
        action Hide("cookiePicked")
    # open wallet sensoe
    imagebutton:
        xpos 640
        ypos 300
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Hide("cookiePicked"), Show("cookieOpened")

screen cookieOpened:
    modal True
    on "hide" action Hide("displayTextScreen")
    zorder 1
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "fortune cookies opened modal.png"
        hover "fortune cookies opened modal.png"
    # X button
    imagebutton:
        xpos 380
        ypos 160
        xanchor 0.5
        yanchor 0.5
        idle "x button.png"
        hover "x button.png"
        action Hide("cookieOpened")
    # cookie sensor
    imagebutton:
        xpos 740
        ypos 250
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Hide("cookieOpened"), Jump("fortune")


screen fingerprints:
    modal True
    on "hide" action Hide("displayTextScreen")
    zorder 1
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "fingerprints modal.png"
        hover "fingerprints modal.png"
    # X button
    imagebutton:
        xpos 380
        ypos 160
        xanchor 0.5
        yanchor 0.5
        idle "x button.png"
        hover "x button.png"
        action Hide("fingerprints")
    # show fingerprints sensor
    imagebutton:
        xpos 590
        ypos 270
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Hide("fingerprints"), Jump("fingerprints")

screen bottlesModal:
    modal True
    on "hide" action Hide("displayTextScreen")
    zorder 1
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "bottles modal.png"
        hover "bottles modal.png"
    # X button
    imagebutton:
        xpos 380
        ypos 160
        xanchor 0.5
        yanchor 0.5
        idle "x button.png"
        hover "x button.png"
        action Hide("bottlesModal")
    # bottles sensor
    imagebutton:
        xpos 560
        ypos 480
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Hide("bottlesModal"), Jump("bottles")

screen bonsaiModal:
    modal True
    on "hide" action Hide("displayTextScreen")
    zorder 1
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "bonsai modal.png"
        hover "bonsai modal.png"
    # X button
    imagebutton:
        xpos 380
        ypos 160
        xanchor 0.5
        yanchor 0.5
        idle "x button.png"
        hover "x button.png"
        action Hide("bonsaiModal")

screen displayTextScreen:
    zorder 100
    default displayText = ""
    vbox:
        xpos xPosition
        ypos yPosition
        xanchor 0.5
        yanchor 0.5
        frame:
            background None
            xpadding 15
            ypadding 15
            text displayText

style textScreenFrame is frame:
    color "#fff"
