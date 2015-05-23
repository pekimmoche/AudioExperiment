from wave_manipulator_by_fft import WaveManipulatorByFft

if __name__ == '__main__':
    # 0, 初期化
    input_filename = "../data/sample.wav"
    output_filename = "../data/out.wav"
    manipulator = WaveManipulatorByFft()

    # 1, ファイルから読み込み
    left, right = manipulator.read_wave(input_filename)

    # 2, wave をフレームごとに切り取ってループ
    data_num = 1024
    fft_num = 1024
    shift_num = int(data_num / 2)

    # 終了条件は、
    for i in range(0, len(left) - data_num, shift_num):
        print(i, i + data_num)


    print("left_len", len(left))

    # 0 1024
    # 512 512+1024
    # 1024 0+1024
    #
    # data_num
    #
    # data = left[:search_length]

    # 3, FFTの処理
    # 4, 作業
    # 5, IFFTの処理
    # 6, Hann窓をかける
    # 7, 出力結果に足し算

    out_left = left
    out_right = right

    # for i in range(1000):
    #     energy_spectrum = FftOperation.generate_energy_spectrum(data, num)
    # end = time.time()

    # 8, 出力結果をwaveに出力
    manipulator.write_2ch_wave(output_filename, left, right)
