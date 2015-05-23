from unittest import TestCase

from matplotlib import pyplot as plt

from window_function import WindowFunction


class TestWindowFunction(TestCase):
    def setUp(self):
        self.window = WindowFunction()

    def test_hann_window(self):
        hann = self.window.hann_window(10)
        self.__plot(hann, 10)
        result = self.window.multiplying_window([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], hann, 10)
        ideal = [0, 0.9549150281252627, 3.4549150281252627, 6.545084971874737, 9.045084971874736, 10.0,
                 9.045084971874736, 6.545084971874737, 3.4549150281252636, 0.9549150281252633]
        self.assertEqual(ideal, result)

    @staticmethod
    def __plot(data, length):
        """ データをグラフにする
        :param data: データ
        :param length: データ長
        :return:
        """
        x = range(0, length)
        y = data
        plt.plot(x, y)
        plt.show()


def test_half_rectangular_window(self):
    result = self.window.half_rectangular_window(10)
    ideal = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    self.assertEqual(ideal, result)
