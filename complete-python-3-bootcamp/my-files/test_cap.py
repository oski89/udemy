import unittest
import test_cap


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = test_cap.cap_text(text)
        self.assertEqual(result, 'Python')

