from unittest import TestCase

import matplotlib.pyplot as plt

from wave_generator import WaveGenerator


class TestWaveGenerator(TestCase):
    def test_sin(self):
        length = 44100
        sin1000 = WaveGenerator.sin(10000, 1000, 0, length)
        self.assertEqual(0, sin1000[0])
        self.assertEqual(9999.4290856537190, sin1000[44067])
        self.assertEqual(len(sin1000), length)

