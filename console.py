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

    def do_create(self, args):
        """USAGE: create <class>
        Creates a new class and prints its id.
        """
        if not args:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            print(eval(args)().id)
            storage.save()

    def do_show(self, args):
        """USAGE: show <class> <id>
        Prints the string representation of an instance
        based on the class name and id.
        """

        new = args.split(" ")
        cl_name = new[0]
        cl_id = new[1]

        if not cl_name:
            print("** class name missing **")
            return

        if cl_name != "BaseModel":
            print("** class doesn't exist **")
            return

        if not cl_id:
            print("** instance id missing **")
            return

        key = cl_name + "." + cl_id
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """USAGE: destroy classname id
        deletes an instance based on the class name and id.
        """

        new = args.split(" ")
        cl_name = new[0]
        cl_id = new[1]

        if not cl_name:
            print("** class name missing **")
            return

        if cl_name != "BaseModel":
            print("** class doesn't exist **")
            return

        if not cl_id:
            print("** instance id missing **")
            return

        key = cl_name + "." + cl_id
        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()        
