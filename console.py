#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter class"""

    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
            }

    # temp test storage
    storage = {}

    def do_EOF(self, line):
        """
        Exits the console when CTRL+D is entered
        """
        print()
        return True

    def do_quit(self, line):
        """
        Quits the console
        """
        return True

    def emptyline(self):
        """
        Executes nothing on emptyline + enter
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance

        Usage: create <class name>
        """
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
        """
        Prints the string representation
        of an instance based on the class name

        Usage: show <class name> <instance_id>
        """
        cls = HBNBCommand.check_class(line)
        if cls is None:
            return

        obj = HBNBCommand.check_id(line)
        if obj is None:
            return
        print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id

        Usage: destroy <class_name> <instance_id>
        """
        cls = HBNBCommand.check_class(line)
        if cls is None:
            return

        obj = HBNBCommand.check_id(line)
        if obj is None:
            return

        del HBNBCommand.storage[f"{cls.__name__}.{obj.id}"]

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name

        Usage: all [<class_name>]
        """
        if line:
            cls = HBNBCommand.check_class(line)
            objs = {key: str(obj) for key, obj in HBNBCommand.storage.items() if type(obj) is cls}
            print(list(objs.values()))
        else:
            print([str(obj) for obj in HBNBCommand.storage.values()])

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
                return
        except Exception:
            print("** instance id missing **")
            return
        return HBNBCommand.storage.get(key)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
