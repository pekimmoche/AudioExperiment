class SqueezeSpectrumFromSelectLocalMaximum(object):
    """ 極大点を用いて、スペクトラムを絞り込むオブジェクト
    """

    INIT_MAXIMUM = (0, 0)

    def get_local_maximum_list_only_num(self, power_spectrum, search_spectrum_num):
        """ 極大点と最大点を指定された数Nだけ取得する
        極大点を全て取得する事を試し、その中から最大となるものをreturn。
        search_spectrum_numの数に満たない場合は、search_spectrum_num以下の結果が返るので注意
        TODO: 足りなかったら最大値でも返すようにする
        :param power_spectrum: パワースペクトル
        :param search_spectrum_num: 検索スペクトル数
        :return:
        """
        if len(power_spectrum) < search_spectrum_num:
            raise ValueError("search spectrum num larger than power spectrum length")
        local_maximum_list = self.get_all_local_maximum_list(power_spectrum)
        local_maximum_list_only_num = self.sort_max_list_only_num(local_maximum_list, search_spectrum_num)
        return [m for m in local_maximum_list_only_num if m != self.INIT_MAXIMUM]

    def get_all_local_maximum_list(self, data: [float]):
        """ 極大値となるデータを全て洗い出して取得する
        隣が同値の場合、片方だけ同値の時は極大値として抽出する。左右が同値の場合は抽出しない。
        但し、このデータは全て正数である事を条件とする。
        :param data: データ
        :return: 極大値リスト
        """
        before1 = self.INIT_MAXIMUM
        before2 = self.INIT_MAXIMUM
        local_maximum_list = []
        for i, d in enumerate(data):
            if d < 0:
                raise ValueError("not positive number!")
            if (before2[1] <= before1[1] and before1[1] > d) or (before2[1] < before1[1] and before1[1] >= d):
                local_maximum_list.append(before1)
            before2 = before1
            before1 = (i, d)
        if (before2[1] <= before1[1] and before1[1] > 0) or before2[1] < before1[1]:
            local_maximum_list.append(before1)
        return local_maximum_list

    def sort_max_list_only_num(self, data: [int, float], num):
        """ データから指定した数だけ最大値を取得したリストを返す
        :param data: [index, value] のリスト
        :param num: 取得する最大値の数
        :return: [index, value] の最大値リスト
        """
        max_list = [(0, 0) for i in range(num)]
        for d in data:
            if d[1] > max_list[0][1]:
                max_list[0] = d
                max_list = self.__quicksort_for_index_list(max_list)
        return max_list

    def __quicksort_for_index_list(self, list: [int, float]):
        """ quicksortのindexリスト[index, value] 対応版
        同値があった場合は古い方をリストの奥にずらす
        :param list: 対象リスト
        :return: 昇順ソートリスト
        """
        if len(list) < 1:
            return list
        pivot = list[0]
        left = []
        right = []
        for x in range(1, len(list)):
            if list[x][1] < pivot[1]:
                left.append(list[x])
            elif list[x][1] == pivot[1] and list[x][0] > pivot[0]:
                left.append(list[x])
            else:
                right.append(list[x])
        left = self.__quicksort_for_index_list(left)
        right = self.__quicksort_for_index_list(right)
        return left + [pivot] + right
