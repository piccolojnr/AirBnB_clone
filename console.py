#!/usr/bin/python3
"""
 entry point of the command interpreter
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review,
        "Amenity": Amenity,
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        args = {
            "all": self.do_all,
            "show": self.do_show,
            "count": self.do_count,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg1 = [arg[: match.span()[0]], arg[match.span()[1] :]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match is not None:
                command = [arg1[1][: match.span()[0]], match.group()[1:-1]]
                if command[0] in args:
                    call = args[command[0]]
                    call(arg1[0])
                    return

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        Usage: quit
        """
        return True

    def do_create(self, arg):
        """Create a new instance of a class
        Usage: create <class name>
        - Usage: create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show an instance of a class
        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        args = parse_arg(arg)
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        storage_id = "{}.{}".format(args[0], args[1])
        try:
            print(storage.all()[storage_id])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Usage: destroy <class name> <id>
        - Usage: destroy BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return
        args = parse_arg(arg)
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        storage_id = "{}.{}".format(args[0], args[1])
        try:
            del storage.all()[storage_id]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Retrieve all instances or instances of a specific class.
        Usage:
          - all: Retrieve all instances across all classes.
          - all <class>: Retrieve all instances of the specified class.
          - <class>.all(): Equivalent to 'all <class>'.
        """
        args = arg.split()
        instances = []
        if not args:
            # If no arguments provided, retrieve all instances across all classes
            instances = [value.__str__() for value in storage.all().values()]
        elif len(args) == 1:
            # If one argument provided, check if it's a class name
            class_name = args[0]
            if class_name in self.__classes.keys():
                # If it's a valid class, retrieve instances of that class
                instances = [
                    value.__str__()
                    for value in storage.all().values()
                    if value.__class__.__name__ == class_name
                ]
            else:
                print("** class doesn't exist **")
                return
        elif len(args) == 3 and args[1] == "all()" and args[2] == ":":
            # If three arguments provided in the format <class>.all():
            class_name = args[0]
            if class_name in self.__classes.keys():
                # If it's a valid class, retrieve instances of that class
                instances = [
                    value.__str__()
                    for value in storage.all().values()
                    if value.__class__.__name__ == class_name
                ]
            else:
                print("** class doesn't exist **")
                return
        print(instances)

    def do_count(self, arg):
        """
         Retrieves the number of instances of a specific class.
        Usage: count <class name>
        - Usage: count BaseModel
        - Usage: <class name>.count(): Equivalent to 'count <class name>'.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        count = 0
        for key, value in storage.all().items():
            if value.__class__.__name__ == class_name:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        - Usage: update BaseModel 1234-1234-1234 name "John"
        - Usage: update User 1234-1234-1234 email "XXXXXXXXXXXXXX"
        """
        # Check if the class exists
        if not arg:
            print("** class name missing **")
            return
        args = parse_arg(arg)

        # Check for missing information
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        # Construct the storage ID
        storage_id = "{}.{}".format(args[0], args[1])

        try:
            obj = storage.all()[storage_id]
            attr = args[2]
            value = args[3]

            # Check if the attribute exists in the object's dictionary
            if attr in obj.__dict__.keys():
                # Get the expected type of the attribute
                valtype = type(obj.__dict__[attr])

                try:
                    # Convert the input value to the expected type
                    value = valtype(value)
                except ValueError:
                    print(f"** invalid value for attribute {attr} **")
                    return

            obj.__dict__[attr] = value
            obj.save()

        except (AttributeError, KeyError):
            print("** no instance found **")


def parse_arg(arg):
    # Define a regular expression pattern to match quoted and non-quoted substrings
    pattern = r'("[^"]*"|[^"\s]+)'

    # Use re.findall to extract substrings that match the pattern
    args = re.findall(pattern, arg)

    # Remove quotes from quoted substrings
    args = [substring.strip('"') for substring in args]

    return args


if __name__ == "__main__":
    HBNBCommand().cmdloop()
