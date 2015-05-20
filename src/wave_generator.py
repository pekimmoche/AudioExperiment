import math

SAMPLING_FREQ = 44100 # サンプリング周波数

class WaveGenerator(object):
    """ 波形生成オブジェクト
    """

    @staticmethod
    def sin(amp, freq, num):
        """ 正弦波を返す。初期位相は0。
        :param amp: 振幅
        :param freq: 周波数
        :param num: 点数
        :return: 正弦波
        """
        omega = 2 * math.pi * freq
        return [amp * math.sin(omega * n / SAMPLING_FREQ) for n in range(num)]

    @staticmethod
    def sin_with_theta(amp, freq, theta, num):
        """ 正弦波を返す。初期位相はtheta。
        :param amp: 振幅
        :param freq: 周波数
        :param theta: 初期位相
        :param num: 点数
        :return: 正弦波
        """
        omega = 2 * math.pi * freq
        return [amp * math.sin(omega * n / SAMPLING_FREQ + theta) for n in range(num)]
