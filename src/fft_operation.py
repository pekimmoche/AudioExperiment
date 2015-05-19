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
