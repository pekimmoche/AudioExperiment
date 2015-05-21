import wave

import numpy as np


class WaveReadOperator(object):
    """ WAVE音源の処理を行う操作オブジェクト
    """

    def __init__(self, filename):
        """
        :param filename: ファイル名
        """
        self.filename = filename

    def print_parameters(self):
        """ 各種情報の出力
        """
        with self.__open_read() as read:
            print("Params : ", read.getparams())
            print('Channel num : ', read.getnchannels())
            print("Sample size : ", read.getsampwidth())
            print("Sampling rate : ", read.getframerate())
            print("Frame num : ", read.getnframes())
            print("Sec : ", float(read.getnframes()) / read.getframerate())

    def get_parameters(self):
        """ 各種情報の出力
        ex. _wave_params(nchannels=2, sampwidth=2, framerate=44100, nframes=100000, comptype='NONE',
                         compname='not compressed')
        """
        with self.__open_read() as read:
            return read.getparams()

    def get_frames(self):
        """ フレーム数を返す
        :return: フレーム数
        """
        with self.__open_read() as read:
            return read.getnframes()

    def read_2ch_wave(self):
        """ 2ch信号を数値リストで取得する
        :return 2ch信号
        """
        with self.__open_read() as read:
            if read.getnchannels() != 2:
                raise ValueError("No 2ch Wave!")

            wave = self.__get_wave(read)
            left = wave[0::2]
            right = wave[1::2]
            return left, right

    def read_1ch_wave(self):
        """ 1ch信号を数値リストで取得する
        :return 1ch信号
        """
        with self.__open_read() as read:
            if read.getnchannels() != 1:
                raise ValueError("No 1ch Wave!")
            return self.__get_wave()

    @staticmethod
    def __get_wave(read):
        """ 音源を数値リストで取得する
        :param read:
        :return 信号
        """
        data = read.readframes(read.getnframes())
        data = np.frombuffer(data, dtype="int16")
        return data

    def __open_read(self):
        """ waveファイル読み込みオープン
        :return
        """
        return wave.open(self.filename, "rb")
