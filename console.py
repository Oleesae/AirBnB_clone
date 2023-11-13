#!/usr/bin/python3
"""HBNB Console"""
import cmd
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    __classes = {'BaseModel': BaseModel, 'User': User,
                 'Place': Place, 'State': State, 'City': City,
                 'Amenity': Amenity, 'Review': Review
                 }

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
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args)().id)
            storage.save()

    def do_show(self, args):
        """USAGE: show <class> <id>
        Prints the string representation of an instance
        based on the class name and id.
        """

        new = args.partition(" ")
        cl_name = new[0]
        cl_id = new[2]

        if not cl_name:
            print("** class name missing **")
            return

        if cl_name not in HBNBCommand.__classes:
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

        new = args.partition(" ")
        cl_name = new[0]
        cl_id = new[2]

        if not cl_name:
            print("** class name missing **")
            return

        if cl_name not in HBNBCommand.__classes:
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

    def do_all(self, args):
        """USAGE: all or all classname
        shows all objects, or all objects of a class.
        """
        print_list = []

        if args:
            args = args.partition(' ')[0]

            if args not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))

        print(print_list)

    def do_update(self, args):
        """USAGE: update class id attribute-name 'attribute-value'
        Updates an instance based on the class name and id by adding
        or updating attribute
        """

        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                    type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
                    storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
