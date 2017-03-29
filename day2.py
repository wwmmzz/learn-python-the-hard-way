from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.",\
                 "Nice job,you died...jackass."\
                 "Such a luser.",\
                 "I have a smallpuppy that`s batter at this."]
    print quips[randint(0,len(quips)-1)]
    exit(1)


def central_corridor():
    print"The Gothons of Planst Percal #25  have incaded your ship and destroyed"
    print"your entir crew. You are the last surviving menber and you last."

    print"mission is to ger the neution destruct bomb from the"
    print"weapons Armory."
    print"put it in the brige, and blow the ship up after gettinginto an"
    print"escape pod"
    print"\n"
    print"You`re running down the central corridor to the WeaponsArmory when"
    print"a Gothon jumps out ,red scaly skin, dark grimy teeth, and wvil cliwn costume"
    print"flowing around his hate filled body. He`s blocking thedoor to the"
    print"Armory and about to pull a weapson to blast you."


    action = raw_input(">")


    if action == "shoot!":
        print "Quick on the draw you yank out your blastter and fire it at the Gothon."
        print "His clown costume is flowing and moving around his body, which throws"
        print "completely ruins hid brand new costume his mother bought him, which"
        print "makes him fly into an insane tage and blast you repestedly in the face until"
        print "you are dead, Then he eats you."
        return 'death'
    elif action == "dodge!":
        print "Like a world class boxer you dodge, weave,slip and righ"
        print "as the Gthon`s blaster cranks a laser pastt your head."
        print "In the middle of your artful doge your foot slipsand you"
        print "bang your head on the metal wall and pass out."
        print "You wake up shortly after only to die as the Gothonstomps on"
        print "your head and eats you."
        return "death"
    elif action == "tell a joke":
        print "Luck for you they made you learn Gothon inslts in the academy."
        print "You tell the one Gothon joke you know:"
        print "Lbbs zvgure vf fb sng,jura fur fvgf nevhaq gur fvgf nebhaq gur unhfr,fur fvgf nebhaq gur ubhfr"
        print "The Gothon stops, tries not to laugh, then busts outlaughing and can`t move:"
        print "While he`s laughing uou run up and shoot him squarein the head"
        print "putting him down, then jump through the Weapon  Armory door."
        return 'laser_weapon_armory'
    else:
        print "DOES NOT COMPTE!"
        return 'central_corridor'
def laser_weapon_armory():
    print "You do a dive roll into the Weapon Armory, crouvh and scan the room"
    print "for more Gothon that might be hidding. It`s dead quiet."
    print "You stand up and run to the far side of the room and  find the"
    print "neutron bomb in its container. There`s a keypad lock on the box"
    print "and you need this code to get the bomb out. If you get the the code"
    print "wrong 10 times then the lock closes forever and you  can`t"
    print "get the bomb. The code is 3 digits."
    code = 2
    guess = int(raw_input("keypad"))
    guesses = 0

    while guess != code and guesses < 10:
        print "BZZZZEDDD!"
        guesses += 1
        guess = raw_input("[keypad]>")
    if guess == code:
                print "The container clicks open and the seal breaks, letting gas out."
                print "You grab the neutron bomb and run as fast as you can to the"
                print "bridge where you must place it int the right spot."
                return 'the_bridge'
    else:
                print "The lock buzzes one last time and then you hear a sickening"
                print "melting sound as the mechan is fused together."
                print "you decide to sit there, and finally the Gothon blow up the"
                print "ship from their ship and you die."
                return 'death'



def the_bridge():
    print "You burst on to the Bridge with rhe neutorn desstruct bomb"
    print "under your arm and surprise 5 Gothon who ate trying to"
    print "take contron of the ship.Each of them has an even uglier"
    print "clown costume than the last. The haven`t pulled their"
    print "weapons out yet, as they see the active bomb under your"
    print "arm and don`t want too set it off."

    action = raw_input(">")

    if action == "throw the bomb":
        print "In a panic you throw the bomb at the group of Gothons"
        print "and make a leap for the door. Tight as you drop it a"
        print "Gothon shoots you righ in the back and killing you"
        print "As you die you see another Gothon frantocally try to disarm "
        print "the bomb. you die knowing they will probably blow up when"
        print "it goes off"
        return 'death'
    elif action == "slowly place the bomb":
        print  "You point your blaster at this the bomb under your arm"
        print "and the Gothon put their hands up and start to sweat."
        print "You inch backward to the door, open it, and then care fully"
        print "place the bomb on the floor,pointing your blaster at it"
        print "You then jump back through the door, punch the close button"
        print "and blast the lock so the Gothon can`t get out."
        print "Now that the bomb is placed you run to the escaped podto" 
        print "get off this tin can"
        return 'escape_pod'
    else:
        print "DOES NOT COMPUTE!"
        return 'the_bridge'


def escape_pod():
    print "You rush through the ship desperately trying to make it to"
    print "the escape pod before the whole ship explodes. It seems  like"
    print "hardly any Gothons are on the ship, so your run is clear  off"
    print "interference. You get to the chamber with the escape pods, and"
    print "now nees to pick one to take. Some of them could be damaged"
    print "but you don`t have time to look. There is 5 pods, Which one"
    print "do you take?"


    good_pod = 4
    guess = raw_input("[pod #]> ")


    if int(guess) != good_pod:
        print "You jump into pod %s and hit the eject button." %guess
        print "The pod escapes out into the vold of space, then"
        print "implodes as the hull ruptures, crushing your body"
        print "into jam jelly"
        return 'death'
    else:
        print "You jump into pod %s and hit the eject button." %guess
        print "The pod easlly slide out into space heading to"
        print "the planet below. As it files to the planet, you look"
        print "back and see your ship implode then explode like a"
        print "bright star, taking out the Gothon ship at the same"
        print "timr. You won!"
        exit(0)


ROOMS = {
    'death':death,
    'central_corridor':central_corridor,
    'laser_weapon_armory':laser_weapon_armory,
    'the_bridge': the_bridge,
    'escape_pod': escape_pod

    }


def runner(map,start):
    next = start


    while True:
        room = map[next]
        print "\n__________"
        next = room()


runner(ROOMS,'central_corridor')


