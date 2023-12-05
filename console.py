"""
 entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
