from unittest import TestCase

from wave_operator import WaveOperator

class TestWaveOperator(TestCase):
    def setUp(self):
        filename = "data/sample.wav"
        self.waveope = WaveOperator(filename)

    def test_prints(self):
        self.waveope.prints()
        self.assertTrue(True)

    def test_get_frames(self):
        self.assertEqual(220500, self.waveope.get_frames())

    def test_get_2ch(self):
        a, b = self.waveope.get_2ch()

        # a, b = self.f()
        left, right = self.waveope.get_2ch()

        self.assertEqual(-11723, left[len(left) - 1])
        self.assertEqual(self.waveope.get_frames(), len(left))
        self.assertEqual(-8244, right[len(right) - 1])
        self.assertEqual(self.waveope.get_frames(), len(right))
