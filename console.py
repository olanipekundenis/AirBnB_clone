#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter class"""

    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel
            }

    # temp test storage
    storage = {}

    def do_EOF(self, line):
        """Exits the console when CTRL+D is entered"""
        print()
        return True

    def do_quit(self, line):
        """Quits the console"""
        return True

    def emptyline(self):
        """Executes nothing on emptyline + enter"""
        pass

    def do_create(self, line):
        """Creates a new instance

        Usage: create <class name>"""
        cls = HBNBCommand.check_class(line)
        if cls is None:
            return
        new_instance = cls()
        new_instance.save()

        # for testing only
        HBNBCommand.storage["{}.{}".format(
            cls.__name__, new_instance.id)] = new_instance

        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation"""
        """of an instance based on the class name

        Usage: show <class name> <instance_id>"""
        cls = HBNBCommand.check_class(line)
        if cls is None:
            return

        obj = HBNBCommand.check_id(line)
        if obj is None:
            return
        print(obj)

    @staticmethod
    def check_class(line):
        """checks class"""
        if not line:
            print("** class name missing **")
            return
        elif line.split()[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        return HBNBCommand.classes[line.split()[0]]

    @staticmethod
    def check_id(line):
        """checks instance id"""
        cls = line.split()[0]
        try:
            key = "{}.{}".format(cls, line.split()[1])
            if key is None or key not in HBNBCommand.storage.keys():
                print("** no instance found **")
        except Exception:
            print("** instance id missing **")
            return
        return HBNBCommand.storage[key]


if __name__ == "__main__":
    HBNBCommand().cmdloop()
