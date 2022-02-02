import os


class FatalSystemError(Exception):
    def __init__(self, message="Give the class a string to work with you dummy or it defaults to this!"):
        self.message = message
        super().__init__(self.message)


def keycontinue():
    os.system("pause")


# noinspection SpellCheckingInspection
errorlist = tuple([
    "Well crap. The house burned down!",
    "OH GOD THE LEECHES THEY'RE IN MY EYeEeeEieIEIEIEIEeesss..."
])

print("Welcome to the python programming hellscape!")
print("Here you will endure the painful story of coding a python program.")
print("Enjoy!")
keycontinue()

while True:
    a = input("You have unimagineable piles of homework. What shall you do? >>|[ ")
    if a.lower() == "burn" or a.lower() == "burn it!":
        a = input("Are you ABSOLUTELY SURE that you want to burn it? This might not be the best place to do it! "
                  ">>|[ ")
        if a.lower() == "yes":
            print("kk")
            raise FatalSystemError(errorlist[0])
    elif a.lower() == "finish":
        print("Nope.")
    elif a.lower() == "kill":
        print("You grab a knife from the kitchen and stab it straight through the paper, over and over again.")
        keycontinue()
        print("Unfortunately the stacks of paper do not respond in any way. You go put the knife back.")
        keycontinue()
    elif a.lower() == "throw":
        print("You pick some of it up and throw, as it goes a little ways but slowly floats back down to the floor.")
        keycontinue()
    elif a.lower() == "bleed":
        print("You pick up the pile of paper. Time to go on a field trip!")
        keycontinue()
        print("You take it to the beach. As you wade into the water you grab leeches because... idk why'd you expect "
              "a good story?")
        keycontinue()
        print("Anyways you have some leeches and now that you've grabbed a few you head back over to that godforsaken "
              "stack of paper. It had this coming...")
        keycontinue()
        print("You pour the leeches onto that evil pile of disgusting useless schoolwork. The leeches latch onto the "
              "paper...")
        keycontinue()
        print("And they then decide that the paper has no blood in it so they head for you.")
        keycontinue()
        raise FatalSystemError(errorlist[1])
    elif a.lower() == "torture":
        print("You head over the the stretcher you have in the corner for the neibour's kid's. It will serve a "
              "different purpose this time!")
        keycontinue()
        print("The paper goes onto the two ropes, you pull and... The paper tears. It lets out no moans or wails of "
              "agony, as alas, you were just defeated by an inanimate object. Oh the humanity!!!")
        keycontinue()
    else:
        raise SystemExit
