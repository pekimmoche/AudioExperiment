
import wave
import numpy as np

class WaveOperation:
    """
    wave音源を操作する
    """

    def __init__(self, file_name):
        """
        :param file_name: ファイル名
        """
        self.file_name = file_name
        self.read = wave.open(self.file_name, "rb")

    def __del__(self):
        self.read.close()

    def print(self):
        """
        各種情報の出力
        """
        print("Prams : ", self.read.getparams())
        print('Channel num : ', self.read.getnchannels())
        print("Sample size : ", self.read.getsampwidth())
        print("Sampling rate : ", self.read.getframerate())
        print("Frame num : ", self.read.getnframes())
        print("Sec : ", float(self.read.getnframes()) / self.read.getframerate())

    def get_2ch(self):
        """
        2ch信号を取得する
        :return
        """
        if self.read.getnchannels() != 2:
            raise ValueError("No 2ch Wave!")

        data = self.get_1ch()
        left = data[0::2]
        right = data[1::2]
        return left, right

    def get_1ch(self):
        """
        音源を取得する
        """

        data = self.read.readframes(self.read.getnframes())
        data = np.frombuffer(data, dtype="int16")
        return data

