from unittest import TestCase
import wave
import struct

from wave_read_operator import WaveReadOperator
from wave_write_operator import WaveWriteOperator


class TestWaveWriteOperator(TestCase):
    def setUp(self):
        output_filename = "data/test_out.wav"
        input_filename = "data/sample.wav"
        self.wave_write = WaveWriteOperator(output_filename)
        self.wave_output_read = WaveReadOperator(output_filename)
        self.wave_input_read = WaveReadOperator(input_filename)

    def test_push_2ch(self):
        input_params =  self.wave_input_read.get_parameters()
        input_left, input_right = self.wave_input_read.read_2ch_wave()

        self.wave_write.write_2ch_wave(input_left, input_right)
        output_params =  self.wave_output_read.get_parameters()
        output_left, output_right = self.wave_output_read.read_2ch_wave()

        self.assertEqual(input_params, output_params)
        self.assertEqual(input_left[0], output_left[0])
        self.assertEqual(input_left[len(input_left)-1], output_left[len(output_left)-1])
        self.assertEqual(input_right[0], output_right[0])
        self.assertEqual(input_right[len(input_right)-1], output_right[len(output_right)-1])
        self.assertEqual(len(input_left), len(output_left))
        self.assertEqual(len(input_right), len(output_right))
