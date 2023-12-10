#!/usr/bin/env python3
""" The Console """
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """implements the command line interface"""
    prompt = "(hbnb)"
    __models = {"BaseModel",
                "User",
                "State",
                "City",
                "Place",
                "Amenity",
                "Review"}
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'longitude': float, 'latitude': float
            }

    def do_quit(self, arg):
        """ `quit` command to exit the program with formatting"""
        return True

    def do_EOF(self, arg):
        """End of File command to exit the program without formatting"""
        return True

    def emptyline(self):
        """does nothing when the line is empty"""
        pass

    def precmd(self, line):
        no_arg = re.search(r"[a-zA-Z]+\.[a-z]+\(\)", line)
        one_arg = re.search(r"[a-zA-Z]+\.[a-z]+\(.+\)", line)
        three_args = re.search(r"[a-zA-Z]+\.[a-z]+\(.+?\, .+?\, .+\)", line)

        if three_args:
            line = line.replace(".", " ").replace("(", " ").replace(")", "")\
                    .replace("\'", "").replace("\"", "").replace(",", "")
            line = line.split()
            line = f"{line[1]} {line[0]} {line[2]} {line[3]} {line[4]}"
        elif no_arg:
            line = line.replace("()", "")
            line = line.split(".")
            line = f"{line[1]} {line[0]}"
        elif one_arg:
            line = line.replace(".", " ").replace("(", " ").replace(")", "")\
                    .replace("\'", "").replace("\"", "")
            line = line.split()
            line = f"{line[1]} {line[0]} {line[2]}"

        return cmd.Cmd.precmd(self, line)

    def do_create(self, line):
        """creates a new instance of any class, and prints the id.
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in type(self).__models:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
        storage.save()

    def help_create(self):
        """ information on how to use create.
        """
        print("creates a new instance of class_name and prints the id")
        print("""\
        [Usage]1: create <class_name>
        [Usage]2: <class_name>.create()
        """)

    def do_show(self, line):
        """prints the string representation of an instance
        based on class name and id.
        """
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in type(self).__models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects.keys():
            print("** no instance found **")
        else:
            print(objects["{}.{}".format(args[0], args[1])])

    def help_show(self):
        """ information on how to use the show command.
        """
        print("Shows an individual instance of a class")
        print("""\
        [Usage]1: show <class_name> <id>
        [Usage]2: <class_name>.show(<id>)
        """)

    def do_destroy(self, line):
        """deletes an instance based on the class name and id.
        """
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in type(self).__models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects.keys():
            print("** no instance found **")
        else:
            del objects["{}.{}".format(args[0], args[1])]
            storage.save()

    def help_destroy(self):
        """information on how to use the destroy command
        """
        print("deletes an instance based on class_name and id")
        print("""\
        [Usage]1: destroy <class_name> <id>
        [Usage]2:<class_name>.destroy(<id>)
        """)

    def do_all(self, line):
        """prints all string representation of all instances
        based or not on the class name.
        """
        objects = storage.all()

        if line and line not in type(self).__models:
            print("** class doesn't exist **")
        elif line and line in type(self).__models:
            list_objs = [str(obj) for obj in objects.values()
                         if obj.__class__.__name__ == line]
            print(list_objs)
        else:
            list_objs = [str(obj) for obj in objects.values()]
            print(list_objs)

    def help_all(self):
        """ information on how to use the `all` command
        """
        print("prints string representation of all instances")
        print("""\
        [Usage]1: all
        [Usage]2: all <class_name>
        [Usage]3: <class_name>.all()
        """)

    def do_update(self, line):
        """updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in type(self).__models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            attr = args[2]
            value = args[3].replace("\"", "").replace("\'", "")
            obj = objects["{}.{}".format(args[0], args[1])]

            if attr in type(self).types:
                value = type(self).types[attr](value)
            setattr(obj, attr, value)
        storage.save()

    def help_update(self):
        """information on how to use the `update` command
        """
        print("updates an instance by class_name and id")
        print("""\
        [Usage]1: update <class_name> <id> <attr_name> <attr_value>
        [Usage]2: <class_name>.update(<id>, <attr_name>, <attr_value>)
        """)

    def do_count(self, line):
        """ Counts the current number of class instances """
        count = 0

        for k, v in storage.all().items():
            if line == k.split(".")[0]:
                count += 1
        print(count)

    def help_count(self):
        """Help information for count"""
        print("prints the current number of class instances")
        print("""\
        [Usage]1: count <class_name>
        [Usage]2: <class_name>.count()
        """)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
