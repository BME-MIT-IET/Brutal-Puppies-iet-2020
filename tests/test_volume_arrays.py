import time
import unittest
from algorithms.arrays import (
   delete_nth_naive,
   limit,
   move_zeros
)

class TestVolumeArrays(unittest.TestCase):

   def setUp(self) -> None:
      super().setUp()
      self.array_10 =[-4,-3,-2,-1,0,1,2,3,4,5]
      self.array_100 = list(range(-50, 50))
      self.array_1000 = list(range(-500, 500))
      self.array_10000 = list(range(-5000, 5000))
      self.array_100000 = list(range(-50000, 50000))
      self.array_1000000 = list(range(-500000, 500000))


   def test_delete_nth(self):
      print("\n Delete_nth with 1000 elements")
      start = time.time()
      delete_nth_naive(self.array_1000, 2)
      end = time.time()
      small = end - start
      print(small)

      print("Delete_nth with 10000 elements")
      start = time.time()
      delete_nth_naive(self.array_10000, 2)
      end = time.time()
      bigger = end - start
      print(bigger)
      result1: float = bigger - small

      print("Delete_nth with 100000 elements")
      start = time.time()
      delete_nth_naive(self.array_100000, 2)
      end = time.time()
      biggest = end - start
      print(biggest)
      result2: float = biggest - small
     
      print("Delete_nth difference:")
      print(result1)
      print(result2)

   def test_limit(self):
      print("\n Limit with 10000 elements")
      start = time.time()
      limit(self.array_10000, -500, 500)
      end = time.time()
      small = end - start
      print(small)

      print("Limit with 100000 elements")
      start = time.time()
      limit(self.array_100000, -5000, 5000)
      end = time.time()
      bigger = end - start
      print(bigger)
      result1: float = bigger - small

      print("Limit with 1000000 elements")
      start = time.time()
      limit(self.array_1000000, -50000, 50000)
      end = time.time()
      biggest = end - start
      print(biggest)
      result2: float = biggest - small
     
      print("Limit difference:")
      print(result1)
      print(result2)   

   def test_move_zeros(self):
      print("\n Move zeros with 10000 elements")
      for x in range(-5000, 5000, 10):
         self.array_10000[x] = 0
      start = time.time()
      move_zeros(self.array_10000)
      end = time.time()
      small = end - start
      print(small)

      print("Move zeros with 100000 elements")
      for x in range(-50000, 50000, 10):
         self.array_100000[x] = 0
      start = time.time()
      move_zeros(self.array_100000)
      end = time.time()
      bigger = end - start
      print(bigger)
      result1: float = bigger - small

      print("Move zeros with 1000000 elements")
      for x in range(-500000, 500000, 10):
         self.array_1000000[x] = 0
      start = time.time()
      move_zeros(self.array_1000000)
      end = time.time()
      biggest = end - start
      print(biggest)
      result2: float = biggest - small
     
      print("Move zeros difference:")
      print(result1)
      print(result2) 

if __name__ == '__main__':
    unittest.main()
