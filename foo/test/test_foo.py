from unittest import TestCase

from foo.add import add
from foo.mult import mult


class TestAdd(TestCase):
    def test_add(self):
        result = add(4, 5)  # type: str
        self.assertEqual(result, 9)


class TestMult(TestCase):
    def test_mult(self):
        result = mult(5, 10)
        self.assertEqual(result, 50)

    def test_str_add(self):
        result = mult(3, 'foo')
        self.assertEqual(result, 'foofoofoo')
