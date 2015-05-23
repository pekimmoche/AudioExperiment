import math

from matplotlib import pyplot as plt


class WindowFunction(object):
    """ 窓関数オブジェクト
    """
    @staticmethod
    def hann_window(length):
        """ ハン窓を返す
        w(x) = 0.5 - 0.5 \cos 2 \pi x (0 <= x <= 1)
        0 の時に0、 lengthの時に1となる。
        hann[i] + hann[i+length/2] = 1 が保証される
        :param length: 長さ
        :return: ハン窓
        """
        w = []
        for i in range(length):
            x = i / length
            w.append(0.5 - 0.5 * math.cos(2 * math.pi * x))
        return w

    @staticmethod
    def half_rectangular_window(length):
        """ 最初の半分を1にして最後の半分を0にする方形窓を返す
        :param length: 長さ
        :return: ハーフ方形窓
        """
        w = []
        half_length = int(length / 2)
        for i in range(0, half_length):
            w.append(1)
        for i in range(half_length, length):
            w.append(0)
        return w

    @staticmethod
    def multiplying_window(data, window_data, data_length):
        """ データに窓関数をかけて返す
        :param data: データ
        :param window_data: 窓関数データ
        :param data_length: データ長
        :return:
        """
        result = []
        for i, value in enumerate(data):
            result.append(value * window_data[i])
        return result

    @staticmethod
    def __plot(data, data_length):
        """ データをグラフにする
        :param data: データ
        :param data_length: データ点数
        :return:
        """
        x = range(0, data_length)
        y = data
        plt.plot(x, y)
        plt.show()
