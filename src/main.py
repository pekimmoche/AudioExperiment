from wave_manipulator_by_fft import WaveManipulatorByFft

if __name__ == '__main__':
    # 0, 初期化
    # input_filename = "../data/sample.wav"
    # output_filename = "../data/out.wav"

    manipulator = WaveManipulatorByFft()
    data_length = 2048
    fft_num = 2048
    shift_num = int(data_length / 2)
    options = {"search_spectrum_num": 10}

    # input_filename = "../data/title.wav"
    # output_filename = "../data/title_out_" + str(data_length) + "_" + str(options["search_spectrum_num"]) + ".wav"

    input_filename = "../data/RisingHope.wav"
    output_filename = "../data/RisingHope_out_" + str(data_length) + "_" + str(options["search_spectrum_num"]) + ".wav"

    # input_filename = "../data/L.Miranic.wav"
    # output_filename = "../data/L.MiranicRisingHope" + str(data_length) + "_" + str(options["search_spectrum_num"]) + ".wav"


    print("length=", data_length, "search_spectrum_num", options["search_spectrum_num"])
    print("reading start")
    left, right = manipulator.read_wave(input_filename)
    wave_length = len(left)
    left_result, right_result = manipulator.init_result(wave_length)
    print("reading end")

    print("roop start")
    for i in range(0, wave_length - data_length, shift_num):
        if i % 100 == 0:
            print(str(round(100 * i / wave_length)) + "%")
        left_tmp = left[i:i + data_length]
        manipulator.roop_with_index(left_tmp, left_result, i, data_length, fft_num, options)

        right_tmp = right[i:i + data_length]
        manipulator.roop_with_index(right_tmp, right_result, i, data_length, fft_num, options)
    left_result, right_result = manipulator.adjust_16bit_by_overflow_wave(left_result, right_result)

    print("writing start")
    manipulator.write_2ch_wave(output_filename, left_result, right_result, wave_length)
    print("finish!")
