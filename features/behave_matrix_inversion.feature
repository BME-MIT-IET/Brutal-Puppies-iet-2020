Feature: Matrix Inversion

  Scenario Outline: run a matrix inversion test to fail (determinant)
     Given a matrix <matrix>
      When the determinant is 0
      Then the result is -4

      Examples: QueriesFailDet
  | matrix |
  | [[1, 2, 3], [1, 2, 3], [1, 2, 3]] |


    Scenario Outline: run a matrix inversion test to fail (array)
     Given a array <array>
      When the array is not matrix
      Then the result is -1

      Examples: QueriesFailArray
  | array |
  | [[1, 2, 3, 4, 5, 6], [1] |


      Scenario Outline: run a matrix inversion test to fail (not square)
     Given a matrix <matrix>
      When the matrix is not square
      Then the result is -2

      Examples: QueriesFailNotSquare
  | matrix |
  | [[1, 2], [1, 2], [1, 2]]     |


        Scenario Outline: run a matrix inversion test to fail (small)
     Given a matrix <matrix>
      When the matrix is too small
      Then the result is -3

      Examples: QueriesFailSmall
  | matrix |
  | [[1]]  |
