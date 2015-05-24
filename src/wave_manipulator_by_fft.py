from matplotlib import pyplot as plt

from fft_operation import FftOperation
from squeeze_spectrum_by_select_local_maximum import SqueezeSpectrumFromSelectLocalMaximum
from wave_read_operator import WaveReadOperator
from wave_write_operator import WaveWriteOperator
from window_function import WindowFunction


class WaveManipulatorByFft(object):
    """ FFTを用いて、Wave波形を加工するクラス
    """

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

        # メイン処理
        spectrum_result = self.__do_it(spectrum[:], fft_num, options)

        wave_result = self.fft_ope.ifft(spectrum_result, fft_num)
        self.__multiplying_hann_with_wave_and_add_to_result(wave_result, result, index, length)

    def __do_it(self, spectrum, fft_num, options):
        search_spectrum_num = options["search_spectrum_num"]
        power_spectrum = self.fft_ope.generate_power_spectrum(spectrum)

        # 極大点を洗い出す
        self.squeeze.get_local_max_or_normal_max(power_spectrum, search_spectrum_num)
        return spectrum

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
