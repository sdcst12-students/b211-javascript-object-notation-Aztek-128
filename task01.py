#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json
class yes():

    def hugh(self):
        filename = 'task01a.txt'
        file = open(filename)
        read = file.read()
        self.pile = json.loads(read)
        self.pile.sort()
        print(self.pile[-1])
        return (self.pile[-1])

    

    def hugh2(self):
        filename = 'task01b.txt'
        file = open(filename)
        read = file.read()
        self.pile = json.loads(read)
        self.pile.sort()
        print(self.pile[-1])
        return (self.pile[-1])
    
    def hugh3(self):
        filename = 'task01c.txt'
        file = open(filename)
        read = file.read()
        self.pile = json.loads(read)
        self.pile.sort()
        print(self.pile[-1])
        return (self.pile[-1])
    
    def __init__(self) -> None:
        self.hugh()
        self.hugh2()
        self.hugh3()

y = yes()