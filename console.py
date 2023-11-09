#!/usr/bin/python3
"""HBNB Console"""
import cmd
import os
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass
    
    def do_EOF(self, line):
        """
        Exits the program.
        USAGE: Ctrl D
        """

        return True

    def do_quit(self, line):
        """Quit command to exit the program."""

        return self.do_EOF(line)

    def do_create(self, arg):
        """USAGE: create <class>
        Creates a new class and prints its id.
        """
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """USAGE: show <class> <id>
        Prints the string representation of an instance
        based on the class name and id.
        """

        


if __name__ == '__main__':
    HBNBCommand().cmdloop()        
