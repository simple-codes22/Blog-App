from django.test import TestCase
from .models import *

class Main_test(TestCase):
    def test_one(self):
        user =  User(id=1)
        self.assertIs(user.is_publisher, False)
