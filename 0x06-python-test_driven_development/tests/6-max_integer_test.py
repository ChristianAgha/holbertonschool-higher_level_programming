#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list_with_only_ints(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_with_not_an_int(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 2, 3, 4])

    def test_large_int(self):
        self.assertEqual(max_integer([99999999999999999999999, 1]),
                         99999999999999999999999)

    def test_no_input(self):
        self.assertFalse(max_integer())

    def test_empty_list(self):
        self.assertFalse(max_integer([]))

    def test_with_a_string(self):
        with self.assertRaises(TypeError):
            max_integer(["hi", 1, 2, 3])

    def test_with_a_boolean(self):
        self.assertEqual(max_integer([True, False, 1, 2, 3]), 3)

    def test_a_string(self):
        self.assertEqual(max_integer("hi"), 'i')

    def test_an_int(self):
        with self.assertRaises(TypeError):
            max_integer(9)

    def test_a_float(self):
        with self.assertRaises(TypeError):
            max_integer(5.6)

    def test_a_negative(self):
        with self.assertRaises(TypeError):
            max_integer(-99)

    def test_a_list_of_negatives(self):
        self.assertEqual(max_integer([-4, -3, -1, -9]), -1)

    def test_a_list_including_None(self):
        with self.assertRaises(TypeError):
            max_integer([1, 3, None, 7])

    def test_None(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_None_as_list(self):
        self.assertFalse(max_integer([None]))

    def test_neg_sign_infront_list(self):
        with self.assertRaises(TypeError):
            max_integer(-[1, 4, 5, 6])

    def test_a_list_of_floats(self):
        self.assertEqual(max_integer([4.5, 6.7, 7.8]), 7.8)

    def test_None_None_None(self):
        with self.assertRaises(TypeError):
            max_integer([None, None, None])

if __name__ == '__main__':
    unittest.main(exit=False)
