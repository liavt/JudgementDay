# From liav:
# Variables for court:
default guilty = False
default mentionedBrother = False
default convincedAboutBrother = False

# Courthouse code

label court:
    scene courthouse
    show j at right
    with dissolve
    $ guilty = False
    $ mentionedBrother = False
    $ convincedAboutBrother = False
    j "Order, order!"
    j "We will now begin case #2158673"
    j "Our defendant: Adam Smith"
    if playersName.lower() != "adam smith":
        y "That's not my name!"
        "The judge looks confused"
        if playersName == "":
            y "Actually, I don't even remember what my name is..."
        else:
            y "My name is actually [playersName]."
        j "No, you must be mistaken. The docket says Adam Smith."
        j "If you have no more interruptions, let us continue with the trial."
    j "Representing the Restaurant Go Go Dim Sum, we have Prosecutor Mark. You may now begin your interrogation of the defendant."
    jump courtwhy

label courtwhy:
    hide j
    show p
    with dissolve
    p "Hello, I will ask you some questions and you must answer nothing but the truth. Are you ready to begin?"
    menu:
        "Yes":
            p "Great, let's start with the first question."
        "No":
            p "Well we don't have much time, so I will continue. Hopefully you can keep up."
    p "First, why did you do it?"
    menu:
        "My long lost twin brother did it, not me!":
            p "This is an interesting claim..."
            $ mentionedBrother = True
            jump courtalibi
        "I wasn't there!":
            jump courtalibi
        "Do what?":
            jump courtwhynoanswer
        "I had debts I needed to pay.":
            p "To who?"
            menu:
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
        "You have the wrong person!":
            jump courtalibifail
        "He made up the story!":
            jump courtalibifail
        "I simply wasn't there!":
            jump courtalibifail
        "He was drunk and confused me for someone else!":
            if hasBeer:
                l "Your honor, if we may raise some evidence to the claim the witness is making..."
                l "We found this beer bottle at the crime scene, behind the bartender's counter."
                b "Actually, now that you remind me, I did feel a bit hungover the night after..."
                l "Yes, clearly this settles the situation. The witness simply confused the defendant for someone who looked similar."
                p "But who would look so similar as to be confused by the witness?"
                l "We can get to that later. Right now, your honor, I request that we throw out this witness testimony as it's clearly not credible."
                j "Objection sustained. The testimony is no longer credible evidence. Prosecutor, continue with your next question."
                jump courtwhere
            else:
                jump courtalibifail

label courtalibifail:
    p "Not a very strong alibi, I have to be honest."
    p "There is a witness testimony against you and there is no evidence for your claim."
    p "I believe there is no doubt you were there, and the court should see this clearly."
    p "Onto my next question."
    $ guilty = True
    jump courtwhere

label courtwhynoanswer:
    p "Don't play dumb, we have a witness testifying they saw you."
    show b at left
    with dissolve
    l "Your honor, my defendant does not have to answer a question if they don't want to."
    j "Correct. Prosecutor, continue to your next question."
    $ guilty = True
    jump courtwhere

label courtwhere:
    p "Where were you an hour before the robbery?"
    menu:
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
    l "Your honor, it is within my client's rights."
    j "Correct, if the defendant refuses to answer a question, then you must move on to the next question."
    p "Fine."

label courtdna:
    p "We also found an almost perfect DNA match of the door handle of the restaurant. Do you have anything to say about this?"
    menu:
        "I have no clue to be honest":
            p "You seem to not have much to say."
            jump courtdnafail
        "Your test must be faulty, it wasn't me!":
            jump courtdnafaultytest
        "I did walk into the restuarant that day...":
            p "Which lines up with the results of the DNA test."
            jump courtdnafail
        "I did the crime, so yes that makes sense.":
            l "Why did you say that!"
            jump courtdnafail
        "I have evidence showing a mismatch of fingerprints" if hasFingerprints:
            p "And how is that relevant?"
            menu:
                "Isn't really.":
                    p "Please stop wasting the time of the court..."
                    jump courtdnafail
                "I don't know, I'm no scientist.":
                    p "Please stop wasting our time..."
                    jump courtdnafail
                "The test must be wrong then.":
                    jump courtdnafaultytest
                "Like I mentioned before, my long lost brother did the crime. Your DNA test simply picked up his DNA." if mentionedBrother:
                    p "A long lost brother? You are seriously claiming we have the wrong guy?"
                    menu:
                        "I plead the fifth.":
                            p "What a waste of time..."
                            jump courtdnafail
                        "Maybe?":
                            p "What a waste of time..."
                            jump courtdnafail
                        "I have heard more crazy things before.":
                            jump courtdnabrother
                        "Yes, and I can prove it.":
                            jump courtdnabrother
                        "That's exactly what I am saying! Aren't you listening?":
                            jump courtdnabrother

label courtdnabrother:
    p "Well, do you have any proof of your 'long lost brother?'"
    menu:
        "None, just trust me bro.":
            p "Please be serious in the court."
            jump courtdnafail
        "Just think about it, it explains everything!":
            p "Not really..."
            jump courtdnafail
        "I have his ID number, you can check the database!":
        # TODO put brother id number
            p "Well, what happened to the money then? Do you have proof that your brother has it?"
            jump courtmoney

label courtdnafaultytest:
    p "Do you have any evidence that this test is faulty?"
    menu:
        "No":
            p "Very well then."
        "Yes, because I know I'm innocent.":
            p "Classic defense. Everyone says that, you aren't special."
        "Yes, I know a guy who worked on it. He says it's fake news!":
            p "Nice try, but hearsay isn't valid evidence."
    jump courtdnafail

label courtdnafail:
    $ guilty = True
    p "Your honor, this test is very accurate and has never failed us. I see no reason to believe that it wasn't the defendant based on this DNA test."
    p "Onto my next question."
    p "Since you so clearly stole the money, where is it now? What did you do with the money?"
    jump courtmoney

label courtmoney:
    menu:
        "I don't recall...":
            p "You must have some clear memory issues then."
            $ guilty = True
        "I don't have the money!":
            p "The restuarant doesn't have the money either, so you must be lying."
            $ guilty = True
        "I used it to pay off my debts.":
            l "Why did you say that?!"
            $ guilty = True
        "I have my wallot to prove that I don't have the money":
            p "And how does that prove it exactly?"
            menu:
                "No idea, it's your job to investigate, not mine.":
                    p "Please take this trial seriously, your life is on the line."
                    p "Since you are clearly joking, I must only assume you are guilty and trying to distract us."
                    $ guilty = True
                "Clearly I'm broke and need the money.":
                    p "Doesn't mean that it's okay to steal."
                    $ guilty = True
                "It fell out of my pocket when I was arrested. Thus, I had no money.":
                    p "So who has the money then, if not you?"
                    menu:
                        "My twin brother":
                            if convincedAboutBrother:
                                p "Huh, it checks out with your earlier evidence too... You have a good point."
                                if guilty:
                                    p "But there is still other evidence outstanding that you have failed to mention."
                                else:
                                    l "Correct, all the evidence points to my defendant being the wrong person."
                                    p "I guess I can see that..."
                            else:
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
    j "So, what do you plead?"
    menu:
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
    if guilty:
        jump execution
    else:
        "You win!!!!"
