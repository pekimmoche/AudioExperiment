from matplotlib import pyplot as plt
import numpy as np

from wave_read_operator import WaveReadOperator
from wave_write_operator import WaveWriteOperator
from window_function import WindowFunction


class WaveManipulatorByFft(object):
    """ FFTを用いて、Wave波形を加工するクラス
    """

    def __init__(self):
        self.window = WindowFunction()

    @staticmethod
    def init_result(length):
        """ 結果の初期化を行う
        :return: 0埋めされたリストを2つ
        """
        zero_list = [0 for i in range(length)]
        return zero_list, zero_list

    def do(self, wave, result, index, num):
        """
        :param wave: 元データ
        :param result: 結果
        :param index: インデックス
        :param num: 処理点数
        """
        # 3, FFTの処理
        # 4, 作業
        # 5, IFFTの処理

        # 6, Hann窓をかけて、足し合わせる
        self.__multiplying_hann_with_wave_and_add_to_result(wave, result, index, num)

    def __multiplying_hann_with_wave_and_add_to_result(self, wave, result, index, num):
        """ Hann窓をかけて、足し合わせる
        :param wave: 波形
        :param result: 出力結果
        :param index: インデックス
        :param num: データ点数
        :return:
        """
        hann = self.window.hann_window(num)
        wave = self.window.multiplying_window(wave, hann, num)
        for i, v in enumerate(wave):
            result[index + i] += v

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
    def write_2ch_wave(filename, left, right, length):
        """ 2ch信号をwave形式で出力する
        :param left: 左波形データ
        :param right: 右波形データ
        :param length: 波形データ長
        """
        wave = WaveWriteOperator(filename)
        wave.write_2ch_wave(left, right, length)

    def __plot_wave(self, wave, wave_length, num):
        """ 波形をグラフにする
        :param wave: データ
        :param data: データ点数
        :param num: 個数
        """
        normal_data = wave / 32768
        self.__plot(wave, wave_length)
        self.__plot(normal_data[:num], num)

    @staticmethod
    def __plot(wave, wave_length):
        """ データをグラフにする
        :param wave: データ
        :param data: データ点数
        :return:
        """
        x = np.arange(0, wave_length, 1)
        y = wave
        plt.plot(x, y)
        plt.show()
