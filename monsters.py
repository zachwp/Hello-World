import random
'''Kill All Monsters!!
                       '''

def game_start():
    print("                                             KILL ALL MONSTERS!!!")
    print("A horde of monsters appear! If you want to live you must slay 3, a ghost, a zombie, and a goblin!")
    print("Type 'sa' to attack an enemy with your sword, Type 'examine' to examine an enemy.")
    print("Type 'ctrl+c' to end the game.")

game_start()

class Monsters:
    class_name = ''
    desc = ''
    objects = {}

    def __init__(self, name):
        self.name = name
        Monsters.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + '\n' + self.desc


class Goblin(Monsters):
    def __init__(self, name):
        self.class_name = 'goblin'
        self.health = 5
        self._desc = 'a foul creature'
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = 'it is wounded'
        elif self.health == 1:
            health_line = 'its lifeforce is fading'
        elif self.health <= 0:
            health_line = 'its dead'
        return self._desc + '\n' + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


class Zombie(Monsters):
    def __init__(self, name):
        self.class_name = 'zombie'
        self.health = 4
        self._desc = 'the living dead'
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = 'it is wounded'
        elif self.health == 1:
            health_line = 'its arm is cut off'
        elif self.health <= 0:
            health_line = 'its dead...again.'
        return self._desc + '\n' + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


class Ghost(Monsters):
    def __init__(self, name):
        self.class_name = 'ghost'
        self.health = 6
        self._desc = 'a frightening spirit, it may be hurt by fire.'
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = 'it is screaming back at you'
        elif self.health == 1:
            health_line = 'its lifeforce is fading'
        elif self.health <= 0:
            health_line = 'its gone'
        return self._desc + '\n' + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


class Player(Monsters):
    def __init__(self, name):
        self.class_name = 'Player Character'
        self.health = 3
        
goblin = Goblin('Gobbly')
zombie = Zombie('brains')
ghost = Ghost('roast')
player = Player('dude')

    
def sa(noun):
    if noun in Monsters.objects:
        thing = Monsters.objects[noun]
        if type(thing) == Goblin or Zombie or Ghost:
            if thing.health >= 1:
                x = random.randint(1, 3)
                if x == 1:
                    player.health = player.health - 1
                    note = 'the {} countered your attack'.format(thing.class_name)
                    return note
                else:
                    thing.health = thing.health - 1
                if thing.health == 0:
                    player.health = player.health + 1
                    msg = 'you killed the {}'.format(thing.class_name)
                    return msg
                else:
                    msg = 'you hit the {}'.format(thing.class_name)
                    return msg
            else:
                msg = 'there is no {} here'.format(noun)
                return msg
        else:
            msg = 'there is no {} here'.format(noun)
            return msg

def get_input():
    print('player health')
    print(player.health)
    command = input(': ').split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print('unknown verb {}'.format(verb_word))
        get_input()
    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb('nothing'))
    if player.health >= 1 and ghost.health <=0 and goblin.health <= 0 and zombie.health <= 0:
       # if goblin.health == 0 and ghost.health == 0 and zombie.health == 0:
        print('Player Character is Victorious!!!!!')
        print('Special thanks to williams stepdad Gary, DBA with Fanatics')
        print('And to his family and dog and cat.')
        print('William, Dev.')
        print('Kandace, wife.')
        print('Alex and Carly, the kids.')
        print('Peaches, the dog')
        print('And last and definitely the least, Penny, the cat.')
        print('Apperently I forgot my snake Luna, according to  my wife.')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('thanks for playing')
        game_start()
        player.health = 3
        goblin.health = 5
        zombie.health = 4
        ghost.health = 6
        get_input()
    if player.health <=0:
        print('Game Over.')
        player.health = 3
        goblin.health = 5
        zombie.health = 4
        ghost.health = 6
    get_input()

def say(noun):
    return 'you said "{}"'.format(noun)


def examine(noun):
    if noun in Monsters.objects:
        return Monsters.objects[noun].get_desc()
    else:
        return 'there is no {} here'.format(noun)



verb_dict = {'say': say, 'examine': examine, 'sa': sa,}

print(ghost.health)
get_input()

