from unittest import TestCase

import src.wave_operation as wave_operation

class TestWaveOperation(TestCase):
    def setUp(self):
        pass

    def test_print(self):
        filename = "sample.wav"
        wave = wave_operation.WaveOperation(filename)
        wave.print()
        # a, b = wave.get_2ch()
        # print(data[0])

        # a, b = self.f()
        left, right = wave.get_2ch()
        print(type(left))

        # self.wave_operation.print()
        self.assertTrue(True)
