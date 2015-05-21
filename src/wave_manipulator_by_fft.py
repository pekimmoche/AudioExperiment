from matplotlib import pyplot as plt
import numpy as np

from wave_read_operator import WaveReadOperator
from wave_write_operator import WaveWriteOperator


class WaveManipulatorByFft(object):
    """ FFTを用いて、Wave波形を加工するクラス
    """

    @staticmethod
    def read_wave(filename):
        """ waveファイルを読み込む
        :param filename: 入力ファイル名
        :return: 左右のwave出力
        """
        wave = WaveReadOperator(filename)
        wave.print_parameters()
        left, right = wave.read_2ch_wave()
        return left, right

    @staticmethod
    def write_2ch_wave(filename, left, right):
        wave = WaveWriteOperator(filename)
        wave.write_2ch_wave(left, right)

    def __plot_wave(self, data, num):
        """ 波形をグラフにする
        :param data: データ
        :param num: 個数
        """
        normal_data = data / 32768
        self.__plot(data)
        self.__plot(normal_data[:num])

    @staticmethod
    def __plot(data):
        """ データをグラフにする
        :param data: データ
        :return:
        """
        x = np.arange(0, len(data), 1)
        y = data
        plt.plot(x, y)
        plt.show()
