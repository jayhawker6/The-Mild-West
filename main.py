import json
import time

import easygui as gui

from dankwood import PlaceParams


# Define Classes
class FatalSystemError(Exception):
    def __init__(self, message="Give the class a string to work with you dummy or it defaults to this!"):
        self.message = message
        super().__init__(self.message)


# Load Data

data = json.load(open('json.json'))

# Initialize some vars
title = "The Mild West"

global pressed
strength = 1
stupidity = 1
wtff = 1
damage = 1
bullcastrated = False


# Define Functions
def ohgod():  # Let's... Move on.
    gui.msgbox("Let's just move on.", title, "Yeah...")


def addwtff(x=1):
    global wtff
    oldwtff = wtff
    wtff += x
    tempstr = "WTF Factor: " + str(oldwtff) + " --> " + str(wtff)
    gui.msgbox(tempstr, "The Mild West", "...What the...")


def adddamage(x=1):
    global damage
    olddamage = damage
    damage += x
    tempstr = "Damage: " + str(olddamage) + " --> " + str(damage)
    gui.msgbox(tempstr, "The Mild West", "(Flex at the haters with your new might)")


def milkbull():
    while True:
        global buttons
        global pressed
        gui.msgbox(data["3"], title, "What")  # But something is VERY wrong
        buttons = ["I know what I'm doing!", "What do you mean?", "Ignore Narrator"]
        pressed = gui.buttonbox("This is a bull.", title, buttons)

        if pressed == "I know what I'm doing!" or pressed == "Ignore Narrator":  # I Know what i'm doing!
            gui.msgbox("Okay, Weirdo. Just saying... That's DISGUSTING.", title,
                       "Shut up and tell the story.")  # Weirdo.
            gui.msgbox("You drink that milk out of that udder and wait... It's real milk? What!?", title,
                       "Always Has Been...")
            addwtff(2)
            gui.msgbox("How the hell did you do that? Still Disgusting but I applaud. Anyways, Time to move on.", title,
                       "Trudge Onward!")
            break

        elif pressed == "What do you mean?":  # What do you mean?
            gui.msgbox(data["2"], title, "So what am I milking?")  # What am I milking?
            pressed = gui.buttonbox("I think you know EXACTLY what you are \"Milking,\" Pardner.", title,
                                    ["Oh god...", "No really i'm clueless what is it?"])
            gui.msgbox(data["4"], title, "I'm sorry!")
            gui.msgbox("Anyways, Time to move on.", title, "But i'm still hungry!")
            break


def castratebull():
    while True:
        pressed = gui.buttonbox("What in tarnation gave you the urge to choose that option!", title,
                                ["*Shrug*", "Nevermind..."])
        if pressed == "*Shrug*":  # Shrugs
            pressed = gui.buttonbox(data["5"], title, ["On second Thought...", "Booyah!"])
            if pressed == "Booyah!":  # Booyah
                pressed = gui.buttonbox("Well, okay then! Guess there's no stopping you.", title,
                                        ["Nope!", "Actually there is..."])
                if pressed == "Nope!":  # No stopping them now
                    gui.msgbox("Damn you.", title, "hehehehehe")
                    gui.msgbox(data["11"], title, data["12"])
                    gui.msgbox(data["13"], title, "Oh god I hate myself!")
                    gui.msgbox(data["14"], title, "OH MY EARS OH PLEASE NO SPARE ME")
                    gui.msgbox(data["15"], title, "AAAAAA")
                    gui.msgbox(data["16"], title, "IS IT OVER YET?! PLEASE MAKE IT END!")
                    gui.msgbox("But it's not over.", title, "NOOOOOOOOOO END THE PAIN ALREADY!!!")
                    gui.msgbox("You repeat everything you just did, all over again.", title, "WHY!!!")
                    gui.msgbox("And it's worse, because the whole time the bull hurts more than before", title,
                               "PLS NO!")
                    gui.msgbox("I think we will leave it there.", title, "Thank god.")
                    gui.msgbox("Let us have a moment of silence for the PTSD you gave that bull...", title, "...")
                    time.sleep(5)
                    gui.msgbox("*Salutes the cow*", title, "...")
                    break

                else:  # Well Actually...
                    gui.msgbox(data["6"], title, "Yeah that's right, no where left for you to go :)")  # It's over fool
                    raise FatalSystemError("Die in a fire you wretched prick! Take that! HAHAHAHA!!!")
            else:  # on second thought...
                gui.msgbox(data["7"], title, "I guess")
                break
        else:
            gui.msgbox(data["7"], title, "Sorry!")
            break


# Begin the Bull shiz
buttons = ["Milk", "Slaughter", "Castrate"]
pressed = gui.buttonbox(data["1"], title, buttons)
if pressed == "Milk":  # Chose to milk the bull
    milkbull()
elif pressed == "Slaughter":
    gui.msgbox(data["8"], title, "Well that was simple.")
    gui.msgbox(data["9"], title, "How dare that bull do such a thing!")
    gui.msgbox(data["10"], title, "Cool! ... Gross!")
    adddamage(2)
    gui.msgbox("Let's move on to dankwood already.", title, "As if I have a choice...")
elif pressed == "Castrate":  # Castrate
    castratebull()
if bullcastrated:
    gui.msgbox("So... with THAT thing over, let's move onto dankwood.", title, "Yes PLEASE.")
gui.msgbox("You travel forth into DankWood, with little regard for the other things around you.", title, "ONWARD!")

dankwood = PlaceParams("DankWood")

if dankwood.hatobtained:
    gui.msgbox("WHY YOU FILTHY CHEATER! HOW DARE YOU START WITH THE HAT ALREADY!", title, "Screw me :(")
    raise FatalSystemError("Cheating Filth!")
