from unittest import TestCase
import sys

sys.path.append("../src")

import wave_operation as waveope


class TestWaveOperation(TestCase):
    def setUp(self):
        filename = "data/sample.wav"
        self.waveope = waveope.WaveOperation(filename)

    def test_print(self):
        self.waveope.print()
        # a, b = waveope.get_2ch()
        # print(data[0])

        # a, b = self.f()
        left, right = self.waveope.get_2ch()
        print(left, right)

        self.assertEqual(-11723, left[len(left) - 1])
        self.assertEqual(self.waveope.get_frames(), len(left))
        self.assertEqual(-8244, right[len(right) - 1])
        self.assertEqual(self.waveope.get_frames(), len(right))
