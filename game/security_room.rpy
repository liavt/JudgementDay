label securityRoom:
    scene securityRoom
    g "Here you go, you have 5 minutes, not a second more!"
    hide g
    show y at left
    y "Let's check this"
    jump securityRoomExplore

label securityRoomExplore:
    show screen pcSensor
    call screen empty

screen empty:
    zorder 0

screen pcSensor:
    zorder 0
    imagebutton:
        xpos 780
        ypos 427
        xanchor 0.5
        yanchor 0.5
        idle "empty.png"
        hover "yellow.png"
        action Show("pcInit")

screen pcInit:
    modal True
    on "hide" action Hide("displayTextScreen")
    zorder 1
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "pcInitModal.png"
        hover "pcInitModal.png"
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
