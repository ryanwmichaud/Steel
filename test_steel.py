import unittest
from steelV2 import apply, transpose, toNames, findChords

class TestApply(unittest.TestCase):
    def test_apply(self):
        self.assertEqual(apply([7, 10,0, 2, 4, 7, 0, 4, 11,2], 
                               [2, 0, 0, 0, 0, 2, 0, 0, 0, 0]),
                               [9, 10,0, 2, 4, 9, 0, 4, 11,2])
    def test_apply_negative(self):
        self.assertEqual(apply([7, 10,0, 2, 4, 7, 0, 4, 11,2], 
                               [0, 0, -1, 0, 0, 0, -1, 0, 0, 0]),
                               [7, 10,11, 2, 4, 7, 11, 4, 11,2])
    def test_apply_multiple(self):
        self.assertEqual(apply(
                            apply([7, 10,0, 2, 4, 7, 0, 4, 11,2], [0, 0, -1, 0, 0, 0, -1, 0, 0, 0]), 
                            [2, 0, 0, 0, 0, 2, 0, 0, 0, 0]),
                         [9, 10,11, 2, 4, 9, 11, 4, 11,2])

class TestTranspose(unittest.TestCase):
    def test_transpose_up(self):
        self.assertEqual(transpose([7, 10,0, 2, 4, 7, 0, 4, 11,2],4),
                                   [11,2, 4, 6, 8, 11,4, 8, 3, 6])
    def test_transpose_down(self):
        self.assertEqual(transpose([7, 10,0, 2, 4, 7, 0, 4, 11,2],-7),
                                   [0, 3, 5, 7, 9, 0, 5, 9, 4, 7])
    def test_transpose_0(self):
        self.assertEqual(transpose([7, 10,0, 2, 4, 7, 0, 4, 11,2],0),
                                   [7, 10,0, 2, 4, 7, 0, 4, 11,2])

class TestToNames(unittest.TestCase):
    def test_on_ctuning(self):
        self.assertEqual(toNames([7, 10,0, 2, 4, 7, 0, 4, 11,2]),
                          ['G', 'AB', 'C', 'D', 'E', 'G', 'C', 'E', 'B', 'D'])
    def test_on_etuning(self):
        self.assertEqual(toNames([11,   2,   4,   6,    8,    11,  4,   8,    3,    6]),
                                 ['B', 'D', 'E', 'FG', 'GA', 'B', 'E', 'GA', 'DE', 'FG'])
        

class TestFindChords(unittest.TestCase):
    def test_on_open(self):
        self.assertEqual(findChords({0, 2, 4, 7, 10, 11}), [[0, 7], [4, 7]])
    def test_on_other(self):
        self.assertEqual(findChords({0, 2, 3, 7, 10, }), [[3], [0, 7]])
    def test_list_input(self):
        with self.assertRaises(TypeError):
            findChords([0, 2, 3, 7, 10, ])