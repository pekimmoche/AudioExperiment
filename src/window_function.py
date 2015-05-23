import math

from matplotlib import pyplot as plt


class WindowFunction(object):
    """ 窓関数オブジェクト
    """

    def multiplying_hann_window(self, data):
        """ データにハン窓をかけて返す
        :param num:
        :return:
        """
        data_num = len(data)
        hann = self.hann_window(data_num)
        result = []
        for i, value in enumerate(data):
            result.append(hann[i] * value)
        return result

    @staticmethod
    def hann_window(num):
        """ ハン窓を返す
        w(x) = 0.5 - 0.5 \cos 2 \pi x
        :param num: 点数
        :return: ハン窓
        """
        range_by_num = range(0, num)
        w = []
        for i in range_by_num:
            w.append(0.5 - 0.5 * math.cos(2 * math.pi * i / (num - 1)))
        return w

    @staticmethod
    def __plot(data):
        """ データをグラフにする
        :param data: データ
        :return:
        """
        x = range(0, len(data))
        y = data
        plt.plot(x, y)
        plt.show()
