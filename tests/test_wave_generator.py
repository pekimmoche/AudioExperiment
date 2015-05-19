from unittest import TestCase
import sys
import matplotlib.pyplot as plt

sys.path.append("../src")
from wave_generator import WaveGenerator

class TestWaveGenerator(TestCase):

    def test_sin(self):
        num = 44100
        sin1000 = WaveGenerator.sin(10000, 1000, num)
        self.assertEqual(0, sin1000[0])
        self.assertEqual(9999.429085653719, sin1000[44067])
        self.assertEqual(len(sin1000), num)

        # plt.plot(range(num), sin1000)
        # plt.show()
