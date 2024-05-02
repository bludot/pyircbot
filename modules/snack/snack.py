import random
import sys

from pyircsdk import Module


class SnackModule(Module):
    def __init__(self, irc):
        super().__init__(irc, "!", "snack")
        self.snacks = [
            "a piece of Hawaiian pizza", 
            "a piece of New York Style pizza", 
            "a piece of Greek pizza", 
            "a piece of Margherita pizza!", 
            "a can of Pepsi", 
            "a can of Coca-cola" ,
            "popcorn" ,
            "Vanilla ice cream" ,
            "Rainbow ice cream" ,
            "Chocolate ice cream" ,
            "Coconut ice cream" ,
            "Strawberry ice cream" ,
            "nothing" ,
            "kit kat" ,
            "ferrero rocher" ,
            "Lays chips" ,
            "marshmallow" ,
            "hamburger"
        ]

    def handleCommand(self, message, command):
        if message.command == "PRIVMSG":
            if command.command == self.fantasy + self.command:
                giveTo = command.args[0]
                snack = random.choice(self.snacks)
                if command.args[0] in self.snacks:
                    snack = command.args[0]
                    giveTo = command.args[1]
                    self.irc.privmsg(message.messageTo, "The maid gives %s to %s" % (snack, giveTo))
                    return
                
                self.irc.privmsg(message.messageTo, "The maid gives %s to %s" % (snack, giveTo))
                


                
