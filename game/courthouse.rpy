# From liav:
# Variables for court:
default guilty = False
default mentionedBrother = False
default convincedAboutBrother = False

# Courthouse code

label court:
    scene courthouse with fade
    play music "courthouse.mp3" fadein 1.0
    $ guilty = False
    $ mentionedBrother = False
    $ convincedAboutBrother = False

    show l
    with dissolve
    l "Hey, the case is starting."
    if not talkedToLawyer:
        l "I'm your lawyer for the case."
        l "I wish we had time earlier to talk but I guess this'll have to do."
    l "They are going to have you answer some questions."
    l "Just answer as truthfully as possible, I'll try to back you up when I can"
    if not hasNotebook:
        l "Before we go, take this notebook."
        l "If you find or hear any information that could help you in your case, make sure to write it down."
        hide screen quick_menu
        $ hasNotebook = True
        show screen quick_menu
        "Tip: you can open your notebook by pressing the {color=#34bdeb}Notebook{/color} button under the dialogue box."
    show j at right
    with dissolve
    j "Order, order!"
    l "Ah, the case is starting!"
    l "Just act natural, you'll be fine."
    hide l
    with dissolve
    j "We will now begin case #2158673"
    j "Our defendant: [yourName]"
    j "ID number: #[yourID]"
    show y at left
    with dissolve
    if playersName.lower() != yourName.lower():
        y "That's not my name!"
        "The judge looks confused"
        if playersName == "":
            y "Actually, I don't even remember what my name is..."
        else:
            y "My name is actually [playersName]."
        j "No, you must be mistaken. The docket says [yourName]."
        j "If you have no more interruptions, let us continue with the trial."
    else:
        y "[yourName] is indeed my name..."
    hide y
    with dissolve
    show p
    with dissolve
    j "Representing the Restaurant [restaurntName], we have Prosecutor [prosecutorsName]."
    j "You may now begin your interrogation of the defendant."
    jump courtwhy

label courtwhy:
    hide j
    with dissolve
    show p
    with dissolve
    menu:
        p "Hello, I will ask you some questions and you must answer nothing but the truth. Are you ready to begin?"

        "Yes":
            p "Great, let's start with the first question."
        "No":
            p "Well we don't have much time, so too bad. I must continue. Hopefully you can keep up."
        "I'm guilty alright, just skip the formalities!":
            show l at right
            with dissolve
            l "WHAT?"
            "Your lawyer facepalms"
            p "Huh, that's an easy confession. I guess that's it."
            $ guilty = True
            hide l
            with dissolve
            jump courtplea
        "I have no idea why I'm here! I don't want to answer any questions, just get me out of here!":
            show l at right
            with dissolve
            l "You really don't know any answer to your questions?"
            "Your lawyer facepalms"
            p "I guess I won't pester the defendant too much."
            p "If he really doesn't know anything, I will forfeit my time. Clearly the evidence will speak for itself."
            $ guilty = True
            hide l
            with dissolve
            jump courtplea
    menu:
        p "First, why did you do it?"

        "My long lost twin brother did it, not me!":
            p "This is an interesting claim..."
            $ mentionedBrother = True
            jump courtalibi
        "I wasn't there!":
            jump courtalibi
        "Do what?":
            jump courtwhynoanswer
        "I had debts I needed to pay.":
            menu:
                p "To who?"

                "The Mafia":
                    pass
                "The Government":
                    pass
                "Russia":
                    pass
                "My Family":
                    p "You must have a very turbulent family life..."
            p "We will have to do a further case in the future to prosecute them. We want to continue learning about you, so I will continue since you implied that you did it."
            $ guilty = True
            jump courtwhere

label courtalibi:
    p "Well, do you have an alibi?"
    show b at left
    with dissolve
    p "We have a witness testify that he saw you walk through the door around the time of the robbery."
    p "He is the bartender of the place, so he was behind the counter."
    menu:
        p "Do you have anything to say about the witness testimony?"

        "You have the wrong person!":
            jump courtalibifail
        "He made up the story!":
            jump courtalibifail
        "I simply wasn't there!":
            jump courtalibifail

        "He was drunk and confused me for someone else!" if not hasBeer:
            jump courtalibifail
        "{color=#34bdeb}He was drunk and confused me for someone else!{/color}" if hasBeer:
            show l at right
            with dissolve
            l "Your honor, if we may raise some evidence to the claim the witness is making..."
            l "We found this beer bottle at the crime scene, behind the bartender's counter."
            b "Actually, now that you remind me, I did feel a bit hungover the night after..."
            l "Yes, clearly this settles the situation. The witness simply confused the defendant for someone who looked similar."
            p "But who would look so similar as to be confused by the witness?"
            l "We can get to that later. Right now, your honor, I request that we throw out this witness testimony as it's clearly not credible."
            hide b
            show j at left
            with dissolve
            j "Objection sustained. The testimony is no longer credible evidence. Prosecutor, continue with your next question."
            hide j
            with dissolve
            hide l
            with dissolve
            p "Hpmh."
            jump courtwhere

label courtalibifail:
    p "Not a very strong alibi, I have to be honest."
    p "There is a witness testimony against you and there is no evidence for your claim."
    p "I believe there is no doubt you were there, and the court should see this clearly."
    p "Onto my next question."
    $ guilty = True
    jump courtwhere

label courtwhynoanswer:
    show b at left
    with dissolve
    p "Don't play dumb, we have a witness testifying they saw you."
    show l at right
    with dissolve
    l "Your honor, my defendant does not have to answer a question if they don't want to."
    hide b
    with dissolve
    show j at left
    with dissolve
    j "Correct. Prosecutor, continue to your next question."
    hide j
    with dissolve
    hide l
    with dissolve
    $ guilty = True
    jump courtwhere

label courtwhere:
    hide b
    with dissolve
    menu:
        p "Where were you an hour before the robbery?"

        "Preparing the escape vehicle":
            $ guilty = True
            p "Your honor, this aligns perfectly with the details of the robbery."
            p "This is strong evidence that the defendant is indeed guilty."
        "At the airport, flying in as a tourist":
            p "So you are a tourist to this area?"
            l "Yes, the defendant was a tourist. That explains why he went into a Chinese restaurant."
        "Watching TV and eating popcorn on my couch":
            p "Fairly classic excuse."
        "I don't really know...":
            jump courtwherefail
    jump courtdna

label courtwherefail:
    $ guilty = True
    p "What will you tell me then? Classic guilty defendant, dodging every question."
    "The prosecutor looks annoyed."
    show l at right
    with dissolve
    l "Your honor, it is within my client's rights."
    show j at left
    with dissolve
    j "Correct, if the defendant refuses to answer a question, then you must move on to the next question."
    p "Fine."
    hide l
    with dissolve
    hide j
    with dissolve

label courtdna:
    menu:
        p "We also found an almost perfect DNA match of the door handle of the restaurant. Do you have anything to say about this?"

        "I have no clue to be honest":
            p "You seem to not have much to say."
            jump courtdnafail
        "Your test must be faulty, it wasn't me!":
            jump courtdnafaultytest
        "I did walk into the restuarant that day...":
            p "Which lines up with the results of the DNA test."
            jump courtdnafail
        "I did the crime, so yes that makes sense.":
            show l at right
            l "Why did you say that!"
            hide l
            with dissolve
            jump courtdnafail
        "{color=#34bdeb}I have evidence showing a mismatch of fingerprints{/color}" if hasFingerprints:
            jump courtdnafingerprints

label courtdnafingerprints:
    menu:
        p "And how is that relevant?"

        "Isn't really.":
            p "Please stop wasting the time of the court..."
            jump courtdnafail
        "I don't know, I'm no scientist.":
            p "Please stop wasting our time..."
            jump courtdnafail
        "The test must be wrong then.":
            jump courtdnafaultytest
        "{color=#34bdeb}Like I mentioned before, my long lost brother did the crime. Your DNA test simply picked up his DNA.{/color}" if mentionedBrother:
            p "A long lost brother? You are seriously claiming we have the wrong guy?"
            menu:
                "Seriously? A long lost brother?"

                "Maybe?":
                    p "What a waste of time..."
                    jump courtdnafail
                "I have heard more crazy things before.":
                    jump courtdnabrother
                "Yes, and I can prove it.":
                    jump courtdnabrother
                "That's exactly what I am saying! Aren't you listening?":
                    jump courtdnabrother

default brotherIDNumber = ""

label courtdnabrother:
    menu:
        p "Well, do you have any proof of your 'long lost brother?'"

        "None, just trust me bro.":
            p "Please be serious in the court."
            jump courtdnafail
        "Just think about it, it explains everything!":
            p "Not really..."
            jump courtdnafail
        "{color=#34bdeb}I have his ID number, you can check the database!{/color}":
            python:
                brotherIDNumber = renpy.input("What is your brother's ID number?", allow="0123456789")
                brotherIDNumber = brotherIDNumber.strip()
            show j at left
            with dissolve
            j "I'm checking the system right now..."
            if brotherIDNumber == teinsID:
                j "It checks out."
                j "There is an entry in the system for [twinsName] Smith..."
                j "His ID number is [teinsID] while our defendant's ID number is..."
                j "Oh wow, that's peculiar. It's one below: [yourID]"
                show l at right
                with dissolve
                l "Your honor, it all checks out. You must have gotten the wrong person."
                j "Makes sense to me. Prosecutor, continue on."
                hide j
                with dissolve
                hide l
                with dissolve
                p "Well, what happened to the money then? Do you have proof that you don't have it?"
                $ convincedAboutBrother = True
                jump courtmoney
            else:
                j "That ID number doesn't belong to anyone with the last name Smith..."
                hide j
                with dissolve
                p "It's settled, the defendant is clearly making something up."
                jump courtdnafail


label courtdnafaultytest:
    menu:
        p "Do you have any evidence that this test is faulty?"

        "No":
            p "Very well then."
        "Yes, because I know I'm innocent.":
            p "Classic defense. Everyone says that, you aren't special."
        "Yes, I know a guy who worked on it. He says it's fake news!":
            p "Nice try, but hearsay isn't valid evidence."
        "{color=#34bdeb}Yes, I have some fingerprint tests from the crime scene which contradict the DNA{/color}" if hasFingerprints:
            jump courtdnafingerprints
    jump courtdnafail

label courtdnafail:
    $ guilty = True
    p "Your honor, this test is very accurate and has never failed us. I see no reason to believe that it wasn't the defendant based on this DNA test."
    p "Onto my next question."
    p "Since you so clearly stole the money, where is it now? What did you do with the money?"
    jump courtmoney

label courtmoney:
    menu:
        p "Where is the money?"

        "I don't recall...":
            p "You must have some clear memory issues then."
            $ guilty = True
        "I don't have the money!":
            p "The restuarant doesn't have the money either, so you must be lying."
            $ guilty = True
        "I used it to pay off my debts.":
            l "Why did you say that?!"
            $ guilty = True
        "{color=#34bdeb}I have my wallet to prove that I don't have the money{/color}" if hasWallet:
            menu:
                p "And how does that prove it exactly?"

                "No idea, it's your job to investigate, not mine.":
                    p "Please take this trial seriously, your life is on the line."
                    p "Since you are clearly joking, I must only assume you are guilty and trying to distract us."
                    $ guilty = True
                "Clearly I'm broke and need the money.":
                    p "Doesn't mean that it's okay to steal."
                    $ guilty = True
                "It fell out of my pocket when I was arrested. Thus, I had no money.":
                    menu:
                        p "So who has the money then, if not you?"

                        "{color=#34bdeb}My twin brother{/color}" if convincedAboutBrother:
                            p "Huh, it checks out with your earlier evidence too... You have a good point."
                            if guilty:
                                p "But there is still other evidence outstanding that you have failed to mention."
                            else:
                                show l at right
                                with dissolve
                                l "Correct, all the evidence points to my defendant being the wrong person."
                                p "I guess I can see that..."
                                hide l
                                with dissolve
                        "My twin brother" if not convincedAboutBrother:
                            p "What an outlandish idea. With no proof, I can't take you seriously."
                            $ guilty = True
                        "The Mafia":
                            p "Funny joke. Please don't be a comedian during your final hours."
                            $ guilty = True
                        "I don't know, I just know I'm innocent!":
                            p "With no proof, I can't take you seriously."
                            $ guilty = True
                        "You, clearly!":
                            p "Your honor, this trial is clearly a joke."
                            $ guilty = True
    jump courtplea

label courtplea:
    p "Your honor, that ends my interrogation."
    p "I rest my case."
    hide p
    with dissolve
    show j
    with dissolve
    menu:
        j "So, what do you plead?"

        "Guilty":
            $ guilty = True
        "Not guilty":
            pass
    j "Then that settles it."
    j "The court finds you..."
    if guilty:
        j "Guilty, on a charge of robbery of a Chinese restuarant."
        j "Your sentence:"
        j "Execution."
    else:
        j "Not guilty."
        j "You have shown sufficient evidence that it was indeed your twin brother who commited the crime."
        j "He will be appearing before the court shortly."
        j "I apologize for wasting your time, I hope it didn't take too long."
    j "This court is adjourned."
    hide j
    with dissolve
    if guilty:
        jump execution
    else:
        jump freedom
