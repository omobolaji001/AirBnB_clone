#!/usr/bin/env python3
""" The Console """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """implements the command line interface"""
    prompt = "(hbnb)"
    __models = {"BaseModel",
                "User",
                "State"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of File command to exit the program"""
        return True

    def emptyline(self):
        """does nothing when the line is empty"""
        pass

    def do_create(self, line):
        """creates a new instance of BaseModel, and prints the id.
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in type(self).__models:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

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

    def do_destroy(self, line):
        """deletes an instance based on the class name and id."""
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
            obj = objects["{}.{}".format(args[0], args[1])]
            if hasattr(obj, args[2]):
                attr_type = type(obj.__dict__[args[2]])
                setattr(obj, args[2], attr_type(args[3]))
            else:
                setattr(obj, args[2], args[3])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
