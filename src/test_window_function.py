from unittest import TestCase

from window_function import WindowFunction


class TestWindowFunction(TestCase):
    def setUp(self):
        self.wf = WindowFunction()

    def test_hann_window(self):
        self.wf.hann_window(10)
        result = self.wf.multiplying_hann_window([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        ideal = [0.0, 1.16977778440511, 4.131759111665348, 7.499999999999999, 9.698463103929543, 9.698463103929543,
                 7.500000000000002, 4.1317591116653505, 1.169777784405111, 0.0]
        self.assertEqual(ideal, result)
