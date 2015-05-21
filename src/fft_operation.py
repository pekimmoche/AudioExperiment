import math
import numpy as np

class FftOperation(object):
    """
    FFT関連の処理を行う操作クラス
    """

    @staticmethod
    def fft(data, fft_num):
        """ FFT を行う
        :param data: データ
        :param fft_num: FFT点数
        :return: FFT結果
        """
        return np.fft.fft(data, fft_num)

    @staticmethod
    def generate_energy_spectrum(data, fft_num):
        """ エネルギースペクトラムを生成する
        :param data: データ
        :param fft_num: FFT点数
        :return: FFT結果
        """
        return [math.sqrt(result.real * result.real + result.imag * result.imag) for result in np.fft.fft(data, fft_num)]

