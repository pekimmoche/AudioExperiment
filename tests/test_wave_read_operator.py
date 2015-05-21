from unittest import TestCase
import wave

from wave_read_operator import WaveReadOperator


class TestWaveReadOperator(TestCase):
    def setUp(self):
        filename = "data/sample.wav"
        self.wave = WaveReadOperator(filename)

    def test_get_parameters(self):
        ideal = wave._wave_params(nchannels=2, sampwidth=2, framerate=44100, nframes=44100 * 5, comptype='NONE',
                                  compname='not compressed')
        self.assertEqual(ideal, self.wave.get_parameters())

    def test_get_frames(self):
        self.assertEqual(220500, self.wave.get_frames())

    def test_read_2ch_wave(self):
        a, b = self.wave.read_2ch_wave()

        # a, b = self.f()
        left, right = self.wave.read_2ch_wave()

        self.assertEqual(-11723, left[len(left) - 1])
        self.assertEqual(self.wave.get_frames(), len(left))
        self.assertEqual(-8244, right[len(right) - 1])
        self.assertEqual(self.wave.get_frames(), len(right))
