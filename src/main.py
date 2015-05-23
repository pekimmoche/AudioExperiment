from wave_manipulator_by_fft import WaveManipulatorByFft

if __name__ == '__main__':
    # 0, 初期化
    input_filename = "../data/sample.wav"
    output_filename = "../data/out.wav"
    manipulator = WaveManipulatorByFft()

    # 1, ファイルから読み込み
    left, right = manipulator.read_wave(input_filename)
    wave_length = len(left)
    left_result, right_result = manipulator.init_result(wave_length)

    data_length = 1024
    fft_num = 1024
    shift_num = int(data_length / 2)

    # 2, wave をフレームごとに切り取ってループ
    for i in range(0, wave_length - data_length, shift_num):
        left_tmp = left[i:i + data_length]
        manipulator.do(left_tmp, left_result, i, data_length)

        # right_tmp = right[i:i + data_length]
        # manipulator.do(right_tmp, right_result, i, data_length)


    # for i in range(1000):
    #     energy_spectrum = FftOperation.generate_energy_spectrum(data, num)
    # end = time.time()


    for i, v in enumerate(left):
        print(i, v, int(round(left_result[i])), v - int(round(left_result[i])))
        if (i > 1026): break

    # 7, 出力結果をwaveに出力
    manipulator.write_2ch_wave(output_filename, left_result, left_result, wave_length)
    # manipulator.write_2ch_wave(output_filename, left_result, right_result, wave_length)
