from unittest import TestCase

from squeeze_spectrum_by_select_local_maximum import SqueezeSpectrumFromSelectLocalMaximum


class TestSqueezeSpectrumFromSelectLocalMaximum(TestCase):
    def setUp(self):
        self.squeeze = SqueezeSpectrumFromSelectLocalMaximum()

    def test_sort_max_with_search_num(self):
        data = [(0, 100), (1, 500), (2, 100), (3, 100), (4, 4300), (5, 300), (6, 100), (7, 150), (8, 200), (9, 500)]
        result = self.squeeze.sort_max_list_only_num(data, 8)
        ideal = [(2, 100), (0, 100), (7, 150), (8, 200), (5, 300), (9, 500), (1, 500), (4, 4300)]
        self.assertEqual(ideal, result)

    def test_get_all_local_maximun(self):
        data = [300, 50, 100, 100, 500, 500, 500, 100, 100, 50, 4300, 300, 150, 200]
        result = self.squeeze.get_all_local_maximum_list(data)
        ideal = [(0, 300), (2, 100), (4, 500), (6, 500), (8, 100), (10, 4300), (13, 200)]
        self.assertEqual(ideal, result)

    def test_get_local_max_or_normal_max(self):
        data = [300, 50, 100, 100, 500, 500, 500, 100, 100, 50, 4300, 300, 150, 200]
        result = self.squeeze.get_local_maximum_list_only_num(data, 6)
        ideal = [(2, 100), (13, 200), (0, 300), (6, 500), (4, 500), (10, 4300)]
        self.assertEqual(ideal, result)

    def test_get_local_max_or_normal_max_極大点が不足している時(self):
        data = [50, 100, 500]
        result = self.squeeze.get_local_maximum_list_only_num(data, len(data))
        ideal = [(2, 500)]
        self.assertEqual(ideal, result)
