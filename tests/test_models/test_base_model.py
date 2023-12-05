#!/usr/bin/python3
"""
    Unittest for base_model.py
"""
import os
from time import sleep
from datetime import datetime
import unittest
from models.base_model import BaseModel


class test_basemodel_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the BaseModel class.
    """

    def test_model_no_arg(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_model_with_arg(self):
        dt = datetime.today()
        iso = dt.isoformat()
        bm = BaseModel(created_at=iso, updated_at=iso)
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_model_with_arg_dict_keys(self):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, datetime.strptime(dt_iso, date_format))
        self.assertEqual(bm.updated_at, datetime.strptime(dt_iso, date_format))

    def test_model_with_none_arg(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_id_is_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_are_unique(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        bm = BaseModel()
        self.assertEqual(str, type(str(bm)))
        self.assertIn("[BaseModel] ({}) {}".format(bm.id, bm.__dict__), str(bm))


class test_basemodel_to_dict_values(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "rahim"
        bm.my_number = 89
        d = {
            "id": bm.id,
            "created_at": bm.created_at.isoformat(),
            "updated_at": bm.updated_at.isoformat(),
            "name": "rahim",
            "my_number": 89,
            "__class__": "BaseModel",
        }
        self.assertDictEqual(d, bm.to_dict())
        self.assertIn("to_dict", dir(bm))
        self.assertEqual(dict, type(bm.to_dict()))
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("id", bm.to_dict())   
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())


class test_basemodel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
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
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


if __name__ == "__main__":
    unittest.main()
