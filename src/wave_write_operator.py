import wave
import struct
import random
import array

class WaveWriteOperator(object):
    """ WAVE音源の処理を行う操作オブジェクト
    """

    def __init__(self, filename):
        """
        :param filename: ファイル名
        """
        self.filename = filename

    def write_2ch_wave(self, left, right):
        """ 2ch信号をwave形式で出力する
        :param left: 左波形データ
        :param right: 右波形データ
        """
        length = min(len(left), len(right))
        if length == 0:
            raise ValueError("Not Writing Wave")
        data = array.array('h', [])
        for i in range(length):
            data.append(left[i])
            data.append(right[i])

        with self.__open_write() as write:
            self.__set_params(write, 2)
            write.writeframes(data)

    def write_1ch_wave(self, wave):
        """ 1ch信号をwave形式で出力する
        """
        if len(wave) == 0:
            raise ValueError("Not Writing Wave")
        data = array.array('h', [])
        [data.append(w) for w in wave]
        with self.__open_write() as write:
            self.__set_params(write, 1)
            write.writeframes(data)

    def __open_write(self):
        """ waveファイル書き込みオープン
        :return
        """
        return wave.open(self.filename, "wb")

    @staticmethod
    def __set_params(write, channel):
        """ パラメータを登録する
        :param write: 書き込み用インスタンス
        :param channel:チャンネル数
        :return:
        """
        write.setparams((channel, 2, 44100, 0, 'NONE', 'not compressed'))
