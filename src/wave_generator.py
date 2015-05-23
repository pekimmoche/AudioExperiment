import math

SAMPLING_FREQ = 44100 # サンプリング周波数

class WaveGenerator(object):
    """ 波形生成オブジェクト
    """

    @staticmethod
    def sin(amp, freq, phase, length):
        """ 正弦波を返す。
        :param amp: 振幅
        :param freq: 周波数
        :param phase: 初期位相(°)
        :param length: 長さ
        :return: 正弦波
        """

        omega = 2 * freq * math.pi
        theta = 2 * phase / 360 * math.pi
        return [amp * math.sin(omega * n / SAMPLING_FREQ + theta) for n in range(length)]
