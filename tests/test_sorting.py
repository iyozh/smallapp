import unittest

import ddt

from main import sort_with_bubble


@ddt.ddt
class TestSorting(unittest.TestCase):

    @ddt.data([1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [5, 3, 4, 2, 1])
    def test_sorting(self, lst):
        result = sort_with_bubble(lst)
        self.assertEqual(result, [1, 2, 3, 4, 5])
