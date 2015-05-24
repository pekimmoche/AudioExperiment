from unittest import TestCase

from squeeze_spectrum_by_select_local_maximum import SqueezeSpectrumFromSelectLocalMaximum


class TestSqueezeSpectrumFromSelectLocalMaximum(TestCase):
    def setUp(self):
        self.squeeze = SqueezeSpectrumFromSelectLocalMaximum()

    def test_sort_max_with_search_num(self):
        data = [[0, 100], [1, 500], [2, 100], [3, 100], [4, 4300], [5, 300], [6, 100], [7, 150], [8, 200], [9, 500]]
        result = self.squeeze.sort_max_list_only_num(data, 8)
        ideal = [[2, 100], [0, 100], [7, 150], [8, 200], [5, 300], [9, 500], [1, 500], [4, 4300]]
        self.assertEqual(ideal, result)

    def test_get_all_local_maximun(self):
        data = [[0, 300], [11, 50], [12, 100], [13, 100], [20, 500], [30, 500], [40, 500], [50, 100], [60, 100],
                [70, 50], [80, 4300], [90, 300], [100, 150], [110, 200]]
        result = self.squeeze.get_all_local_maximum_list(data)
        ideal = [[0, 300], [12, 100], [20, 500], [40, 500], [60, 100], [80, 4300], [110, 200]]
        self.assertEqual(ideal, result)

    def test_get_local_max_or_normal_max(self):
        data = [[0, 300], [11, 50], [12, 100], [13, 100], [20, 500], [30, 500], [40, 500], [50, 100], [60, 100],
                [70, 50], [80, 4300], [90, 300], [100, 150], [110, 200]]
        result = self.squeeze.get_local_max_or_normal_max(data, 6)
        ideal = [[12, 100],  [110, 200], [0, 300], [40, 500], [20, 500], [80, 4300]]
        self.assertEqual(ideal, result)
