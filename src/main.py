# -*- coding: utf-8 -*-

from wave_manipulator_by_fft import WaveManipulatorByFft

if __name__ == '__main__':

    # 0, 初期化
    input_filename = "../data/sample.wav"
    output_filename = "../data/out.wav"
    manipulator = WaveManipulatorByFft()

    # 1, ファイルから読み込み
    left, right = manipulator.read_wave(input_filename)

    # 2, wave をフレームごとに切り取ってループ
    num = 256
    data = left[:num]

    # 3, FFTの処理
    # 4, 作業
    # 5, IFFTの処理
    # 6, Hann窓をかける
    # 7, 出力結果に足し算


    # for i in range(1000):
    #     energy_spectrum = FftOperation.generate_energy_spectrum(data, num)
    # end = time.time()

    # 8, 出力結果をwaveに出力
    manipulator.write_2ch_wave(output_filename, left, right)




