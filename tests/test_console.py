"""These are tests for the console"""
import unittest
import pep8
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Testing the console"""
    def test_console_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_Console(self):
        """ tests that docstrings are present """
        self.assertIsNotNone(HBNBCommand.preloop.__doc__)
        self.assertIsNotNone(HBNBCommand.precmd.__doc__)
        self.assertIsNotNone(HBNBCommand.postcmd.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.help_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.help_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.help_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.help_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.help_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.help_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.help_update.__doc__)
