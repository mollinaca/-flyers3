from unittest import TestCase
from flyers3.flyers3 import Foo

class TestFoo(TestCase):

    def test_say(self):
        self.assertEqual(Foo().say(), 'hi')

if __name__ == '__main__':
    unittest.main()
