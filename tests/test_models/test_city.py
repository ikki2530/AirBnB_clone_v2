#!/usr/bin/python3
"""test_City PASO"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8


class test_City(test_basemodel):
    """test_City"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    # def test_state_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.state_id), str)

    # def test_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.name), str)

    def test_City_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)
