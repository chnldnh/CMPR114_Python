# m13 Ch11 Inheritance + class exercise #10
# Challenge Exercise #1

class AnimalType:
    def eats(self):
        print('This animal likes to eat ?')

class rabbits (AnimalType):
    def munch(self):
        print(' carrots ')

class birds (rabbits):
    def munch1(self):
        print(' seeds ')

class monkeys (birds):
    def munch2(self):
        print(' bananas ')

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

# here we have the Bird Object ingeriting
# from two differnt classes

BirdObject = AnimalType()
BirdObject = birds()

BirdObject.eats()
BirdObject.munch1()

# monkeys Object iheriting 2 different classes
MonkeyObject = AnimalType()
MonkeyObject = monkeys()

MonkeyObject.eats()
MonkeyObject.munch2()



