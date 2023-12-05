#!/usr/bin/python3
"""
 entry point of the command interpreter
"""
import cmd
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
        args = arg.split(" ")
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
        args = arg.split(" ")
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
        Prints all string representation of all instances based or not
        on the class name.
        """
        if not arg:
            print([str(value) for value in storage.all().values()])
            return
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return

        print(
            [
                str(value)
                for value in storage.all().values()
                if value.__class__.__name__ == arg
            ]
        )

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
    """
    Parse arg
    """
    args = arg.split(" ")
    class_name = args[0]
    id = args[1] if len(args) > 1 else ""
    attr_name = args[2] if len(args) > 2 else ""
    attr_val = ""

    if len(args) > 3:
        for i in range(3, len(args)):
            if args[i][0] == '"' and args[i][-1] == '"':
                attr_val = args[i][1:-1]  # Remove double quotes
                break
            elif args[i][0] == '"':
                attr_val += args[i][1:]
            elif args[i][-1] == '"':
                attr_val += args[i][:-1]
                break
            else:
                attr_val += args[i]

    return (class_name, id, attr_name, attr_val)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
