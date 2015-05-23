from unittest import TestCase
import math

from matplotlib import pyplot as plt

import fft_operation as fft_ope


class TestFftOperation(TestCase):
    def setUp(self):
        self.fft_ope = fft_ope.FftOperation()

    def test_fft(self):
        num = 1024
        x = range(num)
        amp = 10000
        freq = 1000
        wav = [amp * math.sin(2 * math.pi * freq * n / 44100.0) for n in x]
        spectrum = self.fft_ope.fft(wav, num)

        # 虚数も含むよ
        energy = [math.sqrt(data.real * data.real + data.imag * data.imag) for data in spectrum]
        self.assertEqual(4714873.6723589, energy[23])

    def test_ifft(self):
        num = 1024
        x = range(num)
        amp = 10000
        freq = 1000
        wav = [amp * math.sin(2 * math.pi * freq * n / 44100.0) for n in x]
        spectrum = self.fft_ope.fft(wav, num)
        data2 = self.fft_ope.ifft(spectrum, num)
        for i, v in enumerate(wav):
            self.assertTrue(v - data2[i] < 0.00001)
