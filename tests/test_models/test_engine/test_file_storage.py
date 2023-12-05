import os
import pep8
import unittest
import models
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class test_file_storage_instantiation(unittest.TestCase):
    """
    testing FileStorage instatntiation
    """

    def test_inst_no_arg(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_inst_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_path_type(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_type(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        self.assertEqual(FileStorage, type(models.storage))


class test_file_storage_methods(unittest.TestCase):
    """
    testing FileStorage methods
    """

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
        FileStorage._FileStorage__objects = {}

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        am = Amenity()
        ct = City()
        st = State()
        pl = Place()
        rv = Review()
        models.storage.new(am)
        models.storage.new(ct)
        models.storage.new(rv)
        models.storage.new(pl)
        models.storage.new(st)
        models.storage.new(bm)
        models.storage.new(us)
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn("City." + ct.id, models.storage.all().keys())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn("User." + us.id, models.storage.all().keys())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        us = User()
        am = Amenity()
        ct = City()
        st = State()
        pl = Place()
        rv = Review()
        models.storage.new(am)
        models.storage.new(ct)
        models.storage.new(rv)
        models.storage.new(pl)
        models.storage.new(st)
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.save()
        with open("file.json", "r") as f:
            file_text = json.loads(f.read())
            self.assertIn("BaseModel." + bm.id, file_text)
            self.assertIn("User." + us.id, file_text)
            self.assertIn("Amenity." + am.id, file_text)
            self.assertIn("City." + ct.id, file_text)
            self.assertIn("State." + st.id, file_text)
            self.assertIn("Place." + pl.id, file_text)
            self.assertIn("Review." + rv.id, file_text)

    def test_save_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_reload_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
