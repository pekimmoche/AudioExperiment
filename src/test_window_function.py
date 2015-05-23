from unittest import TestCase

from window_function import WindowFunction


class TestWindowFunction(TestCase):
    def setUp(self):
        self.window = WindowFunction()

    def test_hann_window(self):
        hann = self.window.hann_window(10)
        result = self.window.multiplying_window([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], hann, 10)
        ideal = [0.0, 1.16977778440511, 4.131759111665348, 7.499999999999999, 9.698463103929543, 9.698463103929543,
                 7.500000000000002, 4.1317591116653505, 1.169777784405111, 0.0]
        self.assertEqual(ideal, result)

    def test_half_rectangular_window(self):
        result = self.window.half_rectangular_window(10)
        ideal = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        self.assertEqual(ideal, result)
