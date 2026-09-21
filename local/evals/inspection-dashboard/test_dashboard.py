import unittest
from dashboard import summarize


class Tests(unittest.TestCase):
    def test_clear(self):
        self.assertEqual(summarize([('a', 'clear')])['status'], 'clear')

    def test_fault(self):
        self.assertEqual(summarize([('a', 'fault')])['status'], 'fault')

    def test_unknown(self):
        self.assertEqual(summarize([('a', None)])['status'], 'unknown')


if __name__ == '__main__':
    unittest.main()
