Feature: Linear search

  Scenario Outline: run a linear search test to success
     Given an array and a query <query>
      When the <query> is in the array
      Then became <position> of <query>

      Examples: QueriesSuccess
  | query  | position |
  | 1      | 0        |
  | 2      | 1        |
  | 3      | 2        |
  | 4      | 3        |
  | 5      | 4        |


  Scenario Outline: run a linear search test to fail
     Given an array and a query <query>
      When the <query> is not in the array
      Then became -1 of <query>

    Examples: QueriesFail
  | query  |
  | 0      |
  | 6      |
  | 7      |
  | 8      |
  | 9      |

