#!/usr/bin/python3
"""Defines unittests for models/review
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review
import pep8


class test_review_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Review class.
    """

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = ["models/review.py"]
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, "Need to fix Pep8")

    def test_pep8_test_console(self):
        """Pep8 test_console.py"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = ["tests/test_models/test_review.py"]
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, "Need to fix Pep8")

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(Review()))
        self.assertNotIn("text", rv.__dict__)

    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Review()))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attributes(self):
        pl = Review()
        self.assertIn("user_id", dir(Review()))
        self.assertNotIn("user_id", pl.__dict__)
        self.assertEqual(str, type(Review.user_id))

    def test_two_review_unique_ids(self):
        ct1 = Review()
        ct2 = Review()
        self.assertNotEqual(ct1.id, ct2.id)

    def test_two_review_different_created_at(self):
        ct1 = Review()
        sleep(0.05)
        ct2 = Review()
        self.assertLess(ct1.created_at, ct2.created_at)

    def test_two_review_different_updated_at(self):
        ct1 = Review()
        sleep(0.05)
        ct2 = Review()
        self.assertLess(ct1.updated_at, ct2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        ctstr = rv.__str__()
        self.assertIn("[Review] (123456)", ctstr)
        self.assertIn("'id': '123456'", ctstr)
        self.assertIn("'created_at': " + dt_repr, ctstr)
        self.assertIn("'updated_at': " + dt_repr, ctstr)

    def test_args_unused(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class test_review_save(unittest.TestCase):
    """
    Unittests for testing save method of the Review class.
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
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)

    def test_two_saves(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rv.save()
        self.assertLess(second_updated_at, rv.updated_at)

    def test_save_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_updates_file(self):
        rv = Review()
        rv.save()
        ctid = "Review." + rv.id
        with open("file.json", "r") as f:
            self.assertIn(ctid, f.read())


class test_review_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Review class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_keys(self):
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    def test_to_dict_contains_added_attributes(self):
        rv = Review()
        rv.middle_name = "Holberton"
        rv.my_number = 98
        self.assertEqual("Holberton", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        rv = Review()
        am_dict = rv.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "Review",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(rv.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        rv = Review()
        self.assertNotEqual(rv.to_dict(), rv.__dict__)

    def test_to_dict_with_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)


if __name__ == "__main__":
    unittest.main()
