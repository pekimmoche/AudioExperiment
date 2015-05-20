from unittest import TestCase
import sys
import math
import matplotlib.pyplot as plt

sys.path.append("../src")

import fft_operation as fftope


class TestFftOperation(TestCase):
    def setUp(self):
        self.fftope = fftope.FftOperation()

    def test_fft(self):
        num = 1024
        x = range(num)
        amp = 10000
        freq = 1000
        wav = [amp * math.sin(2 * math.pi * freq * n / 44100.0) for n in x]
        fft = self.fftope.fft(wav, num)

        # 虚数も含むよ
        energy = [math.sqrt(data.real * data.real + data.imag * data.imag) for data in fft]
        self.assertEqual(4714873.6723589, energy[23])

        plt.plot(x, energy)
        plt.show()
