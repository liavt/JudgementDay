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
    scene crimeScene
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
    show y at center
    y "Someone drank those three bar liqueurs to the bottom."
    y "It must have been the bartender"
    $ hasBeer = True
    hide y
    jump crimeScene

label leavePopUp:
    show y at left
    menu:
        "Call the lawyer":
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
        action Hide("fingerPrintsSensor"), Hide("walletOnFloor"), Hide("fortuneCookiesBowl"), Hide("bottlesSensor"), Hide("leaveButton"), Jump("leavePopUp")

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
        action Jump("bottles")

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
    # open wallet sensoe
    imagebutton:
        xpos 640
        ypos 300
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Hide("cookieOpened")


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
