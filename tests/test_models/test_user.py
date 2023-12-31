#!/usr/bin/python3
"""Defines unittests for models/user
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User
import pep8


class test_user_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the User class.
    """

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = ["models/user.py"]
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, "Need to fix Pep8")

    def test_pep8_test_console(self):
        """Pep8 test_console.py"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = ["tests/test_models/test_user.py"]
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, "Need to fix Pep8")

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_class_attribute(self):
        us = User()

        self.assertEqual(str, type(User.email))
        self.assertIn("email", dir(us))
        self.assertNotIn("email", us.__dict__)

    def test_password_is_public_class_attribute(self):
        us = User()

        self.assertEqual(str, type(User.password))
        self.assertIn("password", dir(us))
        self.assertNotIn("password", us.__dict__)

    def test_first_name_is_public_class_attribute(self):
        us = User()

        self.assertEqual(str, type(User.first_name))
        self.assertIn("first_name", dir(us))
        self.assertNotIn("first_name", us.__dict__)

    def test_last_name_is_public_class_attribute(self):
        us = User()

        self.assertEqual(str, type(User.last_name))
        self.assertIn("last_name", dir(us))
        self.assertNotIn("last_name", us.__dict__)

    def test_two_user_unique_ids(self):
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_user_different_created_at(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_user_different_updated_at(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_args_unused(self):
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class test_user_save(unittest.TestCase):
    """
    Unittests for testing save method of the User class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_two_saves(self):
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        second_updated_at = us.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        us.save()
        self.assertLess(second_updated_at, us.updated_at)

    def test_save_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_updates_file(self):
        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class test_user_to_dius(unittest.TestCase):
    """
    Unittests for testing to_dius method of the User class.
    """

    def test_to_dius_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dius_contains_keys(self):
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        us = User()
        us.middle_name = "Holberton"
        us.my_number = 98
        self.assertEqual("Holberton", us.middle_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        us = User()
        am_dict = us.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "User",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


if __name__ == "__main__":
    unittest.main()
