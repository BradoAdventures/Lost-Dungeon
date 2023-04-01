import random

weapon = False
armour = False
key = False

when = ["A few years ago", "Many moons ago", "Back in my day", "A long time ago, in a galaxy far far away",
        "on the 13th of February", "2006"]
who = ["a mad man with a hat", "a King of Fashionscape", "a chopper of trees", "a Newb", "a Jedi", "a Sith Lord",
       "a Party Hat Murderer"]
kings = ["MadHatter", "KingOfNewbs", "KingOfSimps", "Dragonbiy235", "Starwalker", "Pulpateen", "YOU", "ME", "Durial321"]
residence = ["Prifddinas", "Varrock", "Falador", "Lumbridge", "Seers Village", "Draynor Village", "God Wars Dungeon",
             "The Wild"]
went = ["Bank Stand", "buy a gf, for 5k", "PK", "lure in the wild", "go bossing", "Goblin Raid to pass desert gate",
        "99 Construction party"]
happened = ["joined a simp legion", "payed my newb taxes", "got lured into the wild",
            "was extorted by the Grim Reaper for their gear", "solved a mystery", "got scammed",
            "House engulfed on itself, Giant Massacre"]

weapons = ["Mythical Dagger", "Mythical Whip", "Mythical Scimitar", "Mythical Short Bow", "Mythical long Bow"]
Gear = ["Mythical Helmet", "Mythical Platebody", "Mythical Legs", "Mythical Gloves", "Mythical Boots"]

Fortune = ["Special touches have been planned with you in mind.", "before you recieve, you must give.",
           "Bend the rod while it is still hot.", "Don't stop meow!",
           "Constant grinding can turn an iron rod into a needle.",
           "your smile is a curve that can get a lot of things straight", "You are talented with you hands",
           "You Will soon get an unexpected kisses in unexpected places.",
           "Every exit is an entrance to new experiences.",
           "Open up your mind. let your fantasies unwind",
           "Be prepared to recieve something special with no strings attached.",
           "Why not treat yourself to a good time instead of waiting for someone else to do it?",
           "Relax, and enjoy yourself.", "Tonight you will be blinded by passion",
           "You can't steal second base and keep one foot on first.",
           "Your Tongue is your ambassador."]


def Teleport():
    teleport = ["leave", "rats", "owm", "chest", "chickens", "gear", "8ball", "quiz", "boss"]
    global weapon
    global key
    global armour
    print("What is this strange room I've entered into?!")
    print("Options: Leave")
    userInput = ""
    while userInput not in teleport:
        weapon = True
        key = True
        armour = True
        userInput = input()
        if userInput == "leave":
            StartingRoom()
        elif userInput == "rats":
            roomRats()
        elif userInput == "owm":
            oldwisemanRoom()
        elif userInput == "chest":
            chestRoom()
        elif userInput == "chickens":
            Chickens()
        elif userInput == "gear":
            gearChestRoom()
        elif userInput == "8ball":
            RoomOfMystery()
        elif userInput == "quiz":
            quizRoom(check_guess)
        elif userInput == "boss":
            bossRoom()
        elif userInput == "bar":
            BarRoom()
        else:
            Teleport()


def StartingRoom():
    directions = ["up", "down", "Teleport"]
    print("Which direction should we journey upon sire?")
    print("It looks as we can either go up, or down from here.")
    userInput = ""
    while userInput not in directions:
        print("Options: up, down.")
        userInput = input()
        if userInput == "up":
            roomRats()
        elif userInput == "Teleport":
            if ServerMaster == "Brado69Dr.Eww":
                print("As you wish Lord Commander, where should we go?")
                Teleport()
            else:
                StartingRoom()
        elif userInput == "down":
            Chickens()
        else:
            print("We must chose a door sire.")
            StartingRoom()

def chestRoom():
    directions = ["back", "open chest" ]
    global weapon
    print("It appears we have found a chest!")
    print("Shall we open the chest, or adventure back to the ghost of an old wise man?")
    userInput = ""
    while userInput not in directions:
        print("Options: open chest, back")
        userInput = input()
        if userInput == "back":
            oldwisemanRoom()
        elif userInput == "open chest":
            print("This chest is full of mighty gear! " + random.choice(weapons))
            weapon = True
            emptyRoom()
        else:
            print("What are you waiting for pick a option.")
            chestRoom()

def emptyRoom():
    directions = ["back", "return home"]
    print("should we head back now? seems to be a mystical portal, to return to the start.")
    userInput = ""
    while userInput not in directions:
        print("Options: back, or return home?")
        userInput = input()
        if userInput == "back":
            oldwisemanRoom()
        elif userInput == "return home":
            StartingRoom()
        else:
            print("Never can make the right decision")
            emptyRoom()

def emptyRoom1():
    directions = ["forward", "right", "left"]
    print("Room of slain chickens")
    print("should we head back now?")
    print("Which direction should we go now?")
    userInput = ""
    while userInput not in directions:
        print("Options: forward, right, or left")
        userInput = input()
        if userInput == "forward":
            StartingRoom()
        elif userInput == "right":
            gearChestRoom()
        elif userInput == "left":
            RoomOfMystery()
        else:
            print("Never can make the right decision")
            emptyRoom1()

def Chickens():
    actions = ["fight", "flee"]
    print("Chickens should we kill them?")
    print("Perhaps we could cook them if it comes to it, even though it's no wagyu meat..")
    print("However not sure how we should cook them, maybe we should flee for the moment.")
    userInput = ""
    while userInput not in actions:
        print("Options: fight, or flee?")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("you killed the chickens!")
                emptyRoom1()
            else:
                print("We must find a weapon first, you flee")
                StartingRoom()
        elif userInput == "flee":
            StartingRoom()
        else:
            print("haven't figured out how this works yet?")
            Chickens()


def oldwisemanRoom1():
    directions = ["left", "down", "talk", "teleport"]
    print("The ghost of an old wise man, Care for another tell?")
    print("Should we continue our path, or listen to this crazy mans stories?")
    userInput = ""
    while userInput not in directions:
        print("Options: left, down, talk")
        userInput = input()
        if userInput == "talk":
            print(random.choice(when) + ", " + random.choice(who) + " whose named " + random.choice(kings) +
                  " who lived in " + random.choice(residence) + ", went to " + random.choice(went) + " and "
                  + random.choice(happened))
            oldwisemanRoom1()
        elif userInput == "left":
            roomRats()
        elif userInput == "down":
            chestRoom()
        elif userInput == "teleport":
            if weapon:
                print("Ooooh No, something magical, is pulling us inward! OH MY!")
                BarRoom()
        else:
            print("is it that hard to type, left or down? really?")
            oldwisemanRoom1()

def oldwisemanRoom():
    directions = ["left", "down", "talk", "teleport"]
    print("The ghost of an old wise man, appears")
    print("Perhaps if we talk to the ghost, could provide valuable information?")
    print("Shall we go down into the next room, or shall we enter back into the room to the left?")
    userInput = ""
    while userInput not in directions:
        print("Options: left, down, talk")
        userInput = input()
        if userInput == "talk":
            print(random.choice(when) + ", " + random.choice(who) + " whose named " + random.choice(kings) +
                  " who lived in " + random.choice(residence) + ", went to " + random.choice(went) + " and "
                  + random.choice(happened))
            oldwisemanRoom1()
        elif userInput == "left":
            roomRats()
        elif userInput == "down":
            chestRoom()
        else:
            print("is it that hard to type, left, down, or talk? really?")
            print("must be a mad man not to listen to his stories could be magical.")
            oldwisemanRoom()


def roomRats():
    actions = ["fight", "down", "right"]
    print("This room has a cluster of mice!")
    print("Should we kill them, or should we go enter through the door on the the right")
    print("However we may always go down!")
    global key
    userInput = ""
    while userInput not in actions:
        print("Options: fight, right, down?")
        userInput = input()
        if userInput == "fight":
            key = True
            print("you defeated the measley mice.")
            print("as well have you found a random key!")
            roomRats()
        elif userInput == "right":
            if key:
                print("You here a mummer, sounding like tells of the past.")
                oldwisemanRoom()
            else:
                print("We have to acquire a key first!")
                roomRats()
        elif userInput == "down":
            print("let's head to the starting room")
            StartingRoom()
        else:
            print("pick a direction noob lord")
            roomRats()


def gearChestRoom():
    actions = ["back", "open chest"]
    print("This room appears to have a another chest inside it, should we take a peak?")
    global armour
    userInput = ""
    while userInput not in actions:
        print("Options: open chest, or back")
        userInput = input()
        if userInput == "open chest":
            print(Gear[0:5])
            print("Returning to the room of slain chickens")
            armour = True
            emptyRoom1()
        elif userInput == "back":
            emptyRoom1()
        else:
            print("Figure out how to type simp.")
            gearChestRoom()


def RoomOfMystery():
    actions = ["up", "right", "fortune"]
    print("This dark mysterious room, seems to have a dark floating orb in the middle of it.")
    print("Our inspection of this dark orb reveals that it is a magic 8ball!")
    print("Should we travel up, go back right, or receive our fortune?")
    userInput = ""
    while userInput not in actions:
        print("Options: up, right, fortune")
        userInput = input()
        if userInput == "up":
            quizRoom(check_guess)
        elif userInput == "right":
            emptyRoom1()
        elif userInput == "fortune":
            print(random.choice(Fortune))
            RoomOfMystery1()
        else:
            print("Still we get to this block of decisions...")
            RoomOfMystery()


def RoomOfMystery1():
    actions = ["up", "right", "fortune"]
    print("Interesting fortune, sounds kinda perverted...")
    print("However should we travel up, go back right, or receive our fortune?")
    userInput = ""
    while userInput not in actions:
        print("Options: up, right, fortune")
        userInput = input()
        if userInput == "up":
            quizRoom(check_guess)
        elif userInput == "right":
            emptyRoom1()
        elif userInput == "fortune":
            print(random.choice(Fortune))
            RoomOfMystery1()
        else:
            print("Still we get to this block of decisions...")
            RoomOfMystery1()


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry wrong answer, try again")
                attempt = attempt + 1
            if attempt == 3:
                print("The correct answer is", answer)

def quizRoom(check_guess):
    global score
    print("Welcome, may you pass my exam?")
    print("You must be a wise one if you desire pass")
    print("To pass you must correctly answer all 3 questions!")
    score = 0
    print("Let's take a dive into some history")
    guess1 = input("Who committed the 2006 Falador Massacre?" + " ")
    check_guess(guess1, "Durial321")
    guess2 = input("What is a POH?" + " ")
    check_guess(guess2, "player owned house")
    guess3 = input("Which is the ultimate gaming experience, osrs, or rs3?" + " ")
    check_guess(guess3, "osrs")
    print("Ahhh yess you've passed with a score of " + str(score) + " The dense clouds disperce")
    while True:
        if score >= 3:
            bossRoom()
        elif score <= 3:
            quizRoom(check_guess)
        else:
            quizRoom(check_guess)


def bossRoom():
    actions = ["fight", "flee" "talk"]
    global armour
    print("There seems to be a Guard in front of the staircase?")
    print("With our armour and weapons, we should be able to defeat him easily!")
    userInput = ""
    while userInput not in actions:
        print("Would we Desire to fight, flee, or talk?")
        userInput = input()
        if userInput == "fight":
            if armour:
                print("The Guard shocked, drops his weapon, striking him down with ease.")
                print("You dash for the stairs")
                stairs1()
            else:
                print("You flee!")
                quizRoom(check_guess)
        elif userInput == "flee":
            print("you escape back to the QuizRoom!")
            quizRoom(check_guess)
        elif userInput == "talk":
            print("you approach the Guard, and he exclaims.")
            print("My King we've finally found you, we've been searching everywhere for you!")
            stairs()
        else:
            print("One day you'll figure it out Newb!")
            bossRoom()


def stairs():
    Winner = ["I AM THE KING", "I AM NO KING"]
    userInput = ""
    while userInput not in Winner:
        print("The Guard shouting we've found the KING, WE'VE FOUND HIM!")
        print("As all the people gather shouting MY KING, MY KING!")
        print("Mind blown, with no recollection of anything, you stop and think")
        print("Options: I AM THE KING, or I AM NO KING")
        userInput = input()
        if userInput == "I AM THE KING":
            print("MAAAAAAAY, I PITTY THE FOOOOOOOO")
            quit()
        elif userInput == "I AM NO KING":
            print("I don't know any of you people!!!")
            print("starts chopping everyones toes off, and traps them in the dungeon to serve the old wise man.")
            quit() #turn into a cut scene of life sentence listening to the wise old man
        else:
            print("This is no moment to freeze Sire, what will you do?!")
            stairs()


def stairs1():
    combat = ["kill", "kill self"]
    print("Racing up the stairs, covered in blood, struck in fear")
    print("You start to hear screaming and shouting in a distant daze, as you see people running towards you.")
    userInput = ""
    while userInput not in combat:
        print("In a Daze; you begin to charge at them, ready to slice them down")
        print("You noticed that, they all stopped in their tracks out of pure terror, as you hear.")
        print("OOOOHHH NOOO, WHAT HAS BECOME OF THE KING?!?!")
        print("Options: kill, or kill self?")
        userInput = input()
        if userInput == "kill":
            print("Rains through murdering everyone in sight")
            print("In a split section, you briefly spot a small object, before you know it.")
            print("A peasant child throws a pebble, hit you in the eye and knocks you out.")
            quit()
        elif userInput == "kill self":
            print("What have I done?! I shall honor the last of my respect and end this MEOOOOWWW!")
            quit()
        else:
            print("Stumbled in defeat, and distraught, my mind broken, I need to react!")
            stairs1()


def BarRoom():
    actions = ["teleport", "Drink Beer", "StartingRoom"]
    gulp = "Gulp! \nGulp!"
    print("We appear, within a BarRoom, with a deep never ending cellar, full of barrels...")
    print("Taking a drink, out of one of the barrels. as we've suspected, you exclaim!")
    print("Screaming, it's beer! it's beer!! Your scream, echoing down the halls")
    print("You're positive someone must've heard your screams")
    userInput = ""
    while userInput not in actions:
        print("Options: Drink Beer")
        userInput = input()
        if userInput == "there is no place like home":
            StartingRoom()
        elif userInput == "Drink Beer":
            print("You guzzle down beer until you past out.")
            print(gulp)
            print("Waking back up, hungover you question if you should have another beer?")
            print("You wake up, sober for the first time within what feels as years.")
            print("To over come this fear you drink another beer.")
            print(gulp)
            print("You appeared to have gone into, another century of drinking, with no awareness.")
            print("Growing old, drunk, and weak, you begin to feel like these are your last days.")
            print("Thinking should we count, this as a victory royale? No need to conform to other peoples standards,"
                  "the lack of need to perform for other people, not working but only for survival needs")
            print("Should we have another beer?")
            print(gulp)
            print("Within your final breaths, Drinking your last beer")
            print("Dazing of into a day dream, of you drinking your beer, on a nice sunny beach.")
            print("You Remember, the excitement of being so positive someone heard your screams.")
            quit()
        elif userInput == "teleport":
            if ServerMaster == "Brado69Dr.Eww":
                print("Tally ho's everywhere, lets scram!")
                Teleport()
            else:
                print("Maybe there is another way to teleport out of here, if only there was a sign..")
                BarRoom()
        else:
            print("Maybe we could teleport back out of this place, if only the GREAT CREATOR would give me a sign?!")
            BarRoom()


if __name__ == "__main__":
    while True:
        print("You awake, Dazed and Confused, laying on the ground")
        print("Rising from the ground, in the midst of your eyes debluring, unable to remember anything.")
        print("You're noticing, you're in the middle of a dark and misty dungeon.")
        print("You only see a sign, that states 'there is no place like home'")
        print("Lost and confused; You think, who am I?")
        name = input()
        print("I suppose we are, " +name+ ", I hope the voice in my head isn't lying...")
        ServerMaster = name
        StartingRoom()