import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        console = HBNBCommand()
        console.do_quit("")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        console = HBNBCommand()
        console.do_EOF("")
        self.assertEqual(mock_stdout.getvalue(), "\n")

    def test_do_create(self):
        console = HBNBCommand()
        # Add your test cases here

    def test_do_show(self):
        console = HBNBCommand()
        # Add your test cases here

    def test_do_destroy(self):
        console = HBNBCommand()
        # Add your test cases here

    def test_do_all(self):
        console = HBNBCommand()
        # Add your test cases here

    def test_do_count(self):
        console = HBNBCommand()
        # Add your test cases here

    def test_do_update(self):
        console = HBNBCommand()
        # Add your test cases here

if __name__ == '__main__':
    unittest.main()