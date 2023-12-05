# AirBnB Clone - The ALX_SE

![AirBnB Logo](https://user-images.githubusercontent.com/88311316/151070609-19608294-829e-408b-b2b3-5d1f2873f1e3.png)


## Description

The ALX_SE B&B project represents the culmination of my six months of studies at the ALX Africa School, specifically in the full-stack software engineering program. The primary objective of this project is to deploy a replica of the Airbnb website using a custom server. The final version of this project encompasses the following key components:

1. A command interpreter for manipulating data without a visual interface (used for development and debugging).
2. A front-end website with both static and dynamic functionalities.
3. A comprehensive database to manage the backend functionalities.
4. An API that provides a communication interface between the front-end and back-end of the system.
5. Review of general concepts in Python and software engineering.

As you navigate through this code base, it's important to understand the following concepts that were applied during the project:

- Creating a Python package.
- Developing a command interpreter in Python using the `cmd` module.
- Implementing unit testing in a large project.
- Serializing and deserializing a class.
- Reading and writing JSON files.
- Managing datetime.
- Understanding UUID (Universally Unique Identifier).
- Utilizing `*args` and `**kwargs` in Python functions.
- Handling named arguments in a function.

## Environment

The console was developed on Ubuntu 20.04LTS using Python 3 (version 3.8.0).

## Requirements

To work on this project, you need knowledge of Python 3, command line interpreter usage, and a computer with Ubuntu 20.04, Python 3, and a pep8 style corrector.

## Repository Contents

This repository contains the following files:

1. AUTHORS Contains information about the authors of the project.
2. base_model.py Defines the BaseModel class (parent class) and methods.
3. user.py Defines the subclass User.
4. amenity.py Defines the subclass Amenity.
5. city.py Defines the subclass City.
6. place.py Defines the subclass Place.
7. review.py Defines the subclass Review.
8. state.py Defines the subclass State.
9. file_storage.py Creates a new instance of a class, serializes and deserializes data.
10. console.py Creates, retrieves, updates, and destroys objects.
11. test_base_model.py Unit tests for base_model.
   ... Other test files for various classes.

## How To Start

Clone the repository and run the console.py:

`$ git clone https://github.com/------/AirBnB_clone.git`
`$ cd AirBnB_clone`
`$ ./console.py`

## How To Use

The console provides various commands for managing objects. Here are some of the key commands:

- `create`: Creates an object of a given class.
- `show`: Prints the string representation of an instance based on the class name and ID.
- `all`: Prints all string representations of instances based on the class name.
- `update`: Updates an instance based on the class name and ID by adding or updating attributes.
- `destroy`: Deletes an instance based on the class name and ID.- `count`: Retrieves the number of instances of a class.
- `help`: Prints information about a specific command.
- `quit/EOF`: Exits the program.

## Authors

- rahim daud
- Augustine Rita
