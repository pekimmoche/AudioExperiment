from unittest import TestCase
import src.hello as hl

class TestHello(TestCase):
    def setUp(self):
        self.hello = hl.Hello()

    def test_hello1(self):
        self.assertEqual(3, self.hello.add(1, 2))

    def test_hello2(self):
        self.assertNotEqual(5, self.hello.add(1, 2))
