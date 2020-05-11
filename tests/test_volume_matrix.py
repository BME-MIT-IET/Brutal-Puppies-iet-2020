from algorithms.matrix import (
    copy_transform,
    matrix_inversion,
    multiply,
    rotate_image
)
import time
import unittest


class TestVolume(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.m_small = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 3x3
        self.m_6x6 = [[1, 2, 4, 1, 6, 7], [4, 4, 6, 1, 7, 9], [7, 2, 9, 1, 8, 8],
                      [1, 1, 1, 1, 4, 3], [1, 2, 4, 1, 7, 7], [1, 2, 4, 1, 8, 8]]  # 6x6
        self.m_10x10 = [[1, 2, 45, 1, 6, 7, 1, 23, 4, 1], [4, 4, 6, 1, 7, 9, 1, 2, 4, 1],
                        [7, 2, 9, 1, 9, 8, 7, 2, 4, 1],
                        [1, 11, 1, 15, 4, 3, 1, 2, 4, 1], [1, 2, 4, 1, 71, 4, 7, 2, 4, 1],
                        [1, 2, 4, 1, 20, 6, 34, 2, 4, 1],
                        [1, 2, 4, 1, 6, 7, 1, 2, 4, 1], [4, 46, 5, 8, 9, 3, 13, 2, 4, 1],
                        [7, 2, 9, 1, 8, 52, 7, 10, 4, 1],
                        [18, 8, 4, 5, 4, 3, 8, 9, 10, 11]]  # 10x10
        self.m_30x30 = [list(range(1, 31))] * 30
        self.m_big = [list(range(1, 51))] * 50
        self.m_enorm = [list(range(1, 101))] * 100

    def test_measure_rotate_clockwise(self):
        print("\n small matrix rotate clockwise: (3x3)")
        start = time.time()
        copy_transform.rotate_clockwise(self.m_small)
        end = time.time()
        small = end - start
        print(small)

        print("big matrix rotate clockwise: (50x50)")
        start = time.time()
        copy_transform.rotate_clockwise(self.m_big)
        end = time.time()
        big1 = end - start
        print(big1)
        result1: float = big1 - small

        print("bigger matrix rotate clockwise: (100x100)")
        start = time.time()
        copy_transform.rotate_clockwise(self.m_enorm)
        end = time.time()
        big2 = end - start
        print(big2)
        result2: float = big2 - small
        print("rotate clockwise difference:")
        print(result1)
        print(result2)

    def test_measure_rotate_counterclockwise(self):
        print("\n small matrix rotate counter clockwise: (3x3)")
        start = time.time()
        copy_transform.rotate_counterclockwise(self.m_small)
        end = time.time()
        small = end - start
        print(small)

        print("big matrix rotate counter clockwise: (50x50)")
        start = time.time()
        copy_transform.rotate_counterclockwise(self.m_big)
        end = time.time()
        big1 = end - start
        print(big1)
        result1: float = big1 - small

        print("bigger matrix rotate counter clockwise: (100x100)")
        start = time.time()
        copy_transform.rotate_counterclockwise(self.m_enorm)
        end = time.time()
        big2 = end - start
        print(big2)
        result2: float = big2 - small
        print("rotate counter clockwise differences:")
        print(result1)
        print(result2)

    def test_measure_top_left_invert(self):
        print("\n small matrix top left invert: (3x3)")
        start = time.time()
        copy_transform.top_left_invert(self.m_small)
        end = time.time()
        small = end - start
        print(small)

        print("big matrix top left invert: (50x50)")
        start = time.time()
        copy_transform.top_left_invert(self.m_big)
        end = time.time()
        big1 = end - start
        print(big1)
        result1: float = big1 - small

        print("bigger matrix top left invert: (100x100)")
        start = time.time()
        copy_transform.top_left_invert(self.m_enorm)
        end = time.time()
        big2 = end - start
        print(big2)
        result2: float = big2 - small
        print("top left invert difference:")
        print(result1)
        print(result2)

    def test_measure_bottom_left_invert(self):
        print("\n small matrix bottom left invert: (3x3)")
        start = time.time()
        copy_transform.bottom_left_invert(self.m_small)
        end = time.time()
        small = end - start
        print(small)

        print("big matrix bottom left invert: (50x50)")
        start = time.time()
        copy_transform.bottom_left_invert(self.m_big)
        end = time.time()
        big1 = end - start
        print(big1)
        result1: float = big1 - small

        print("bigger matrix bottom left invert: (100x100)")
        start = time.time()
        copy_transform.bottom_left_invert(self.m_enorm)
        end = time.time()
        big2 = end - start
        print(big2)
        result2: float = big2 - small
        print("bottom left invert difference:")
        print(result1)
        print(result2)

    def test_measure_invert_matrix(self):
        print("\n small matrix invert matrix: (3x3)")
        start = time.time()
        matrix_inversion.invert_matrix([[1, 1, 3], [4, 5, 6], [7, 1, 9]])
        end = time.time()
        small = end - start
        print(small)

        print("big matrix invert matrix: (6x6)")
        start = time.time()
        matrix_inversion.invert_matrix(self.m_6x6)
        end = time.time()
        big1 = end - start
        print(big1)
        result1: float = big1 - small

        print("bigger matrix invert matrix: (10x10)")
        start = time.time()
        matrix_inversion.invert_matrix(self.m_10x10)
        end = time.time()
        big2 = end - start
        print(big2)
        result2: float = big2 - small
        print("invert matrix difference:")
        print(result1)
        print(result2)

    def test_measure_multiply(self):
        print("\n small matrix multiply: (3x3)x(3x3)")
        start = time.time()
        multiply.multiply(self.m_small, self.m_small)
        end = time.time()
        small = end - start
        print(small)

        print("big matrix multiply: (30x30)x(30x30)")
        start = time.time()
        multiply.multiply(self.m_30x30, self.m_30x30)
        end = time.time()
        big1 = end - start
        print(big1)
        result1: float = big1 - small

        print("bigger matrix multiply: (50x50)x(50x50)")
        start = time.time()
        multiply.multiply(self.m_big, self.m_big)
        end = time.time()
        big2 = end - start
        print(big2)
        result2: float = big2 - small
        print("multiply difference:")
        print(result1)
        print(result2)

    def test_measure_rotate_image(self):
        print("\n small matrix rotate image: (3x3)")
        start = time.time()
        rotate_image.rotate(self.m_small)
        end = time.time()
        small = end - start
        print(small)

        print("big matrix rotate image: (50x50)")
        start = time.time()
        rotate_image.rotate(self.m_big)
        end = time.time()
        big1 = end - start
        print(big1)
        result1: float = big1 - small

        print("bigger matrix rotate image: (100x100)")
        start = time.time()
        rotate_image.rotate(self.m_enorm)
        end = time.time()
        big2 = end - start
        print(big2)
        result2: float = big2 - small

        print("rotate image difference:")
        print(result1)
        print(result2)


if __name__ == '__main__':
    unittest.main()
