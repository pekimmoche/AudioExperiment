import wave
import numpy as np


class WaveOperation(object):
    """ WAVE音源の処理を行う操作クラス
    """

    def __init__(self, file_name):
        """
        :param file_name: ファイル名
        """
        self.file_name = file_name

    def print(self):
        """ 各種情報の出力
        """
        with self.__open_read() as read:
            print("Params : ", read.getparams())
            print('Channel num : ', read.getnchannels())
            print("Sample size : ", read.getsampwidth())
            print("Sampling rate : ", read.getframerate())
            print("Frame num : ", read.getnframes())
            print("Sec : ", float(read.getnframes()) / read.getframerate())

    def get_frames(self):
        """ フレーム数を返す
        :return: フレーム数
        """
        with self.__open_read() as read:
            return read.getnframes()

    def get_2ch(self):
        """ 2ch信号を数値リストで取得する
        :return 2ch信号
        """
        with self.__open_read() as read:
            if read.getnchannels() != 2:
                raise ValueError("No 2ch Wave!")

        data = self.get_1ch()
        print(len(data))
        left = data[0::2]
        right = data[1::2]
        return left, right

    def get_1ch(self):
        """ 音源を数値リストで取得する
        :return 2ch信号
        """
        with self.__open_read() as read:
            data = read.readframes(read.getnframes())
            data = np.frombuffer(data, dtype="int16")
            return data

    def __open_read(self):
        """ waveファイルオープン
        :return
        """
        return wave.open(self.file_name, "rb")

