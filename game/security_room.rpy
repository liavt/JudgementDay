default searchInput = ""

label securityRoom:
    scene securityRoom with fade
    stop music fadeout 1.0
    play music "security room.mp3" fadein 1.0
    pause(1)
    show y at left with dissolve
    show g at right with dissolve
    g "Here you go, you have 5 minutes, not a second more!"
    hide g with dissolve
    y "Let's check this"
    hide y
    jump securityRoomExplore

label securityRoomExplore:
    show screen roomSensors
    call screen empty

screen empty:
    zorder 0

label pc:
    hide screen roomSensors
    show screen pcInit
    pause(2)
    hide screen pcInit
    show screen pcHome
    # "enter id to search"
    pause(1)
    jump search

label search:
    python:
        accepted_strings = ["smith", "adam", "joshua", "106398772", "106398773"]
        searchInput = renpy.input("What is your input?")
        searchInputLower = searchInput.strip().lower()
        is_search_accepted = False
        for acc_str in accepted_strings:
            if acc_str in searchInputLower:
                is_search_accepted = True
                break
    if is_search_accepted:
        hide screen pcHome
        show screen pcResults
    else:
        hide screen pcHome
        "Prisoner '[searchInput]' was not found on the system..."
        menu:
            "What do you want to do next?"

            "Try another input":
                show screen pcHome
                jump search
            "Exit System":
                jump securityRoomExplore

    call screen empty

label adamResult:
    hide screen pcResults
    show screen pcAdam
    pause(1)
    y "I look like a shadow of myself... I got to get out of this prison."
    hide screen pcAdam
    show screen pcResults
    call screen empty

label joshuaResult:
    hide screen pcResults
    show screen pcJoshua
    pause(1)
    y "This guy looks just like me! All these years I was sure I was an orphan."
    y "Who are you, JOSHUA SMITH?"
    hide screen pcJoshua
    show screen pcResults
    call screen empty

label leave:
    hide screen roomSensors
    show y at left with dissolve
    y "Guard Mike!"
    y "I'm done."
    show g at right with dissolve
    g "It's time for your trial."
    g "No need to remind you not to say a single word about.. you know ..."
    stop music fadeout 1.0
    jump court

screen roomSensors:
    on "hide" action Hide("displayTextScreen")
    imagebutton:
        xpos 780
        ypos 427
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Jump("pc")
        hovered Show("displayTextScreen", displayText = "Investigate", xPosition = 780, yPosition = 427)
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        idle "leave button.png"
        hover "leave button hover.png"
        action Jump("leave")

screen pcInit:
    modal True
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "pcInitModal.png"
        hover "pcInitModal.png"
    # # X button
    # imagebutton:
    #     xpos 380
    #     ypos 160
    #     xanchor 0.5
    #     yanchor 0.5
    #     idle "x button.png"
    #     hover "x button.png"
    #     action Hide("walletPicked"), Show("walletOnFloor")
    # # open wallet sensoe
    # imagebutton:
    #     xpos 765
    #     ypos 370
    #     xanchor 0.5
    #     yanchor 0.5
    #     idle "empty.png"
    #     hover "yellow.png"
    #     action Hide("walletPicked"), Show("walletOpened")

screen pcHome:
    # modal True
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "pcHomeScreen.png"
        hover "pcHomeScreen.png"

screen pcResults:
    modal True
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "pcResults.png"
        hover "pcResults.png"
    imagebutton:
        xpos 598
        ypos 280
        xanchor 0.5
        yanchor 0.5
        idle "AdamResult.png"
        hover "AdamResultHover.png"
        action Jump("adamResult")
    imagebutton:
        xpos 598
        ypos 370
        xanchor 0.5
        yanchor 0.5
        idle "JoshuaResult.png"
        hover "JoshuaResultHover.png"
        action Jump("joshuaResult")
    imagebutton:
        xpos 850
        ypos 480
        xanchor 0.5
        yanchor 0.5
        idle "pcLogout.png"
        hover "pcLogoutHover.png"
        action Hide("pcResults"), Jump("securityRoomExplore")

screen pcAdam:
    # modal True
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "pcAdam.png"
        hover "pcAdam.png"

screen pcJoshua:
    # modal True
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "pcJoshua.png"
        hover "pcJoshua.png"

screen displayTextScreen:
    zorder 100
    default displayText = ""
    vbox:
        xpos xPosition
        ypos yPosition
        xanchor 0.5
        yanchor 0.5
        frame:
            # background None
            xpadding 15
            ypadding 15
            text displayText
