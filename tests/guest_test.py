import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Amy")

    def test_guest_has_name(self):
        self.assertEqual("Amy", self.guest_1.name)