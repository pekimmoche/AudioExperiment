import math

from matplotlib import pyplot as plt

from fft_operation import FftOperation
from squeeze_spectrum_by_select_local_maximum import SqueezeSpectrumFromSelectLocalMaximum
from wave_read_operator import WaveReadOperator
from wave_write_operator import WaveWriteOperator
from window_function import WindowFunction


class WaveManipulatorByFft(object):
    """ FFTを用いて、Wave波形を加工するクラス
    """

    MAX_16BIT_AMP = 32767

    def __init__(self):
        self.window = WindowFunction()
        self.fft_ope = FftOperation()
        self.squeeze = SqueezeSpectrumFromSelectLocalMaximum()

    @staticmethod
    def init_result(length):
        """ 結果の初期化を行う
        :return: 0埋めされたリストを2つ
        """
        zero_list = [0 for i in range(length)]
        return zero_list, zero_list

    def roop_with_index(self, wave, result, index, length, fft_num, options):
        """
        :param wave: 波形データ
        :param result: 結果
        :param index: インデックス
        :param length: データ長
        :param fft_num: FFT点数
        :param options: メイン加工処理に使う変数群
        """
        spectrum = self.fft_ope.fft(wave, fft_num)
        spectrum_result = self.__manipulate_spectrum(spectrum[:], fft_num, options)
        wave_result = self.fft_ope.ifft(spectrum_result, fft_num)
        self.__multiplying_hann_with_wave_and_add_to_result(wave_result, result, index, length)

    def __manipulate_spectrum(self, spectrum, fft_num, options):
        """ スペクトルデータを加工する
        TODO: コールバック関数にしよう
        :param spectrum: スペクトルデータ
        :param fft_num: FFT点数
        :param options: 加工処理に使う変数群
        :return:
        """
        search_spectrum_num = 2 * options["search_spectrum_num"]  # スペクトルは左右対称なので二倍
        power_spectrum = self.fft_ope.generate_power_spectrum(spectrum)

        # 極大点を洗い出して、その値だけ取り出す
        # 99.9%は該当しないので、先端処理を楽するために一旦 0 と fft_num/2 の値は0化して省略する
        power_spectrum[0] = 0
        power_spectrum[int(fft_num / 2)] = 0
        local_maximum_list = self.squeeze.get_local_maximum_list_only_num(power_spectrum, search_spectrum_num)

        spectrum_result = [0 for n in range(fft_num)]
        for local_maximum in local_maximum_list:
            spectrum_result[local_maximum[0]] = local_maximum[1]
        return spectrum_result

    def __multiplying_hann_with_wave_and_add_to_result(self, wave, result, index, length):
        """ Hann窓をかけて、足し合わせる
        :param wave: 波形
        :param result: 出力結果
        :param index: インデックス
        :param length: データ長
        :return:
        """
        hann = self.window.hann_window(length)
        wave = self.window.multiplying_window(wave, hann, length)
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

    def adjust_16bit_by_overflow_wave(self, left, right):
        """ 16bitオーバーしてる音源を、16bit範囲内に抑える
        :param left: 左音源
        :param right: 右音源
        :return:
        """
        result = [math.fabs(w) for w in left] + [math.fabs(w) for w in right]
        adjust_ratio = max(result) / self.MAX_16BIT_AMP
        if adjust_ratio > 1:
            left_result = [w/adjust_ratio for w in left]
            right_result = [w/adjust_ratio for w in right]
        else:
            left_result = left
            right_result = right
        return left_result, right_result

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
