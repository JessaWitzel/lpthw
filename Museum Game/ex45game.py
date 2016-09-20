#My museum game beause I'm tired of my games killing people. :)
import random

class Player(object):
    def __init__(self, name):
        self.name = name
        self.pocket = []

    def pocket_it(self, item):
        self.pocket.append(item)

    def check_pocket():
        #List what is currently in Player's pocket
        print pocket


class Exhibit(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

all_exhibits = []

def create_exhibits():
    exhibits_fd = open("/home/jessa/lpthw/Museum Game/exhibits.txt", "r")
    exhibits = exhibits_fd.read()
    exhibits_fd.close()

    exhibits = exhibits.split("-----")

    for item in exhibits:
        clean_item = item.strip()
        exhibit = clean_item.split("\n", 1)
        e = Exhibit(exhibit[0].strip(), exhibit[1].strip())
        all_exhibits.append(e)
    return all_exhibits

create_exhibits()
strange_spacefacts = {}

def import_strangefacts():
    strangefacts_fd = open("/home/jessa/lpthw/Museum Game/strangefacts.txt", "r")
    strangefacts = strangefacts_fd.read()
    strangefacts_fd.close()

    facts = strangefacts.split("-----")
    for item in facts:
        clean_item = item.strip()
        strangefacts = clean_item.split(":", 1)
        strange_spacefacts[strangefacts[0].strip()] = strangefacts[1].strip()

import_strangefacts()

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exit = False

    def enter(self, player):
        self.exit = False
        while not self.exit: #While self.exit is false call self.explore
            self.explore(player)
#default setting of a room is to enter and if there is nothing to explore, exit.
    def explore(self, player):
        self.exit = True


class Dinosaur(Room):

    def explore(self, player):
        print(self.description)
        choice = raw_input("What would you like to explore next? Type 'exit' to leave the room or type the name of the place in this room you would like to explore. > ")
        if "exit" == choice:
            print "You have exited the %s. Where would you like to go?" % self.name
            self.exit = True
        elif "look" in choice:
            print(self.description)
        elif "sand" in choice:
            self.sand(player)
        elif "skeleton" in choice:
            print "The skeleton has a placard beside it."
            print all_exhibits[0].description
        elif "timeline" in choice:
            print all_exhibits[1].description

    def sand(self, player):
        print """There is a tub of sand beneath a big sign with instructions.
                A paleontologist is a scientist who studies fossils. Today you are going to
                be an amateur paleontologist. A fossil is the remains or impression of a prehistoric
                organism preserved in a mold or cast in rock.
                In this sand are 5 fossils and 5 regular artifacts.
                Can you tell the difference? Type 'True' if the artifact you find is a fossil and
                'False' if it is not."""

        artifacts = {
                    'rusty bottlecap': False, 'ammonite': True, 'trilobite': True, 'coral': True,
                    'gastropod': True, 'vertebrate': True, 'chopstick': False,
                    'token': False, 'agate slice': False, 'old bolt': False
                    }

        while len(artifacts) > 0:
            random_artifact = random.choice(artifacts.keys())
            print "You go digging and pull up a %s." % random_artifact
            if random_artifact == "token":
                print "You found the token!"
                player.pocket_it(random_artifact)
                break
            else:
                guess = raw_input("Type 'True' if you think it is a fossil. Otherwise type 'False' > ")
                if guess == str(artifacts[random_artifact]):
                    print "That is correct!"
                else:
                    print "That is incorrect."
            del artifacts[random_artifact]

        if len(artifacts) == 0:
            print "There are no more items in the sand. You have already played this game."


class SpaceExploration(Room):

    def explore(self, player):
        print(self.description)
        choice = raw_input("What would you like to explore?")
        if 'exit' in choice:
            self.exit = True
        elif 'look' in choice:
            print(self.description)
        elif "left" in choice or "star" in choice:
            print "The star has a placard beside it."
            print all_exhibits[2].description
        elif "strange" in choice or "facts" in choice or "straight" in choice:
            print "You rotate through a list of 5 strange facts. Click enter for a new strange fact. Enter 'exit' to leave this game."
            while len(strange_spacefacts) > 0:
                choice = raw_input("> ")
                if 'exit' in choice:
                    print("Ok, fine, quitter.")
                    break
                space_fact = random.choice(strange_spacefacts.keys())
                print "Here is your fact about %s." %space_fact
                print strange_spacefacts[space_fact]
                del strange_spacefacts[space_fact]
        elif "planets" in choice or "right" in choice:
            planets = ["Earth", "Jupiter", "Mercury", "Uranus", "Venus", "Saturn", "Neptune", "Mars"]
            planets_in_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
            player_planets = []
            n = 0
            print "There are 8 planets in our solar system. Here they are in no particular order:", planets
            print "Start by typing the name of the planet closest to the sun and press enter."
            print "If you have gotten the first planet correct you will see 'Correct, what is the next furthest planet from the sun' and it will print your list so far."
            while player_planets != planets_in_order:
                guess = raw_input ("> ")
                if guess == planets_in_order[n]:
                    player_planets.append(guess)
                    print "Correct! Here is your list so far: %s What is the next furthest planet from the sun?" %player_planets
                    n += 1
                else:
                    print "That is not correct. Try again."
#fix this
dino_desc = """At the center of the room you see a huge dinosaur skeleton looming over you.
To the left is a sand pit that contains fossils. To the right is a large
timeline. What would you like to explore?"""
dino_room = Dinosaur("Dinosaur Room", dino_desc)

space_desc = """To your left there is what looks like a shooting star painted on the wall, to your right is a flexible mobile
with planets, and straight ahead is a rotating dial with 'Strange Space Facts'. Which would you like to explore first?"""
space_room = SpaceExploration("Space Exploration Room", space_desc)


class Game(object):
    def __init__(self, player):
        self.player = player
        self.rooms = {'dino': dino_room, 'space': space_room}
        self.over = False
        self.welcome = """You find yourself standing in a museum. There is a dinosaur exhibit to your left and a space exhibit to your right."""
        self.current_room = None

    def explore(self):
        choice = raw_input("> ")
        if 'left' in choice:
            return self.rooms['dino']
        elif 'right' in choice:
            return self.rooms['space']
        elif 'exit' in choice:
            self.over = True
        else:
            print("Invalid choice.")
            return None

    def loop(self):
        while not self.over:
            if self.current_room is None:
                print(self.welcome)
            room = self.explore()
            if room is None:
                continue
            self.current_room = room
            self.current_room.enter(self.player)
            self.current_room = None


def main():
    name = raw_input("What is your name? > ")
    player = Player(name)
    game = Game(player)
    game.loop()

if __name__ == '__main__':
    main()
#import guard to keep everything from running if you are not trying to play it.
