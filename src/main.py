# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import wave_operation as waveope
import fft_operation as fftope

def plot(data):
    x = np.arange(0, len(data), 1)
    y = data
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    filename = "../data/sample.wav"

    wave = waveope.WaveOperation(filename)
    wave.print()
    left, right = wave.get_2ch()

    num = 256
    data = left[:num]

    ## 音波形の出力
    plot(data)

    # 正規化
    normal_data = data / 32768.0
    plot(normal_data[:num])

    # fftope = fftope.FftOperation(length, length)

