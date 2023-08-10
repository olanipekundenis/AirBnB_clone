#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter class"""

    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
