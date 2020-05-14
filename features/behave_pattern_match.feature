Feature: Pattern match

   Scenario Outline: run a pattern match test to success
     Given a <pattern> and a <word>
      When the <pattern> is in the <word>
      Then the pattern searching is successful

      Examples: PatternsSuccess
  | pattern  | word           |
  | aa       | appleapple     |
  | aba      | funasdfun      |
  | aaa      | wonwonwon      |
  | abcd     | behavior       |
  | abca     | technologiktech|


  Scenario Outline: run a pattern match test to fail
     Given a <pattern> and a <word>
      When the <pattern> is not in the <word>
      Then the pattern searching is a failure

      Examples: PatternFailed
  | pattern  | word      |
  | aa       | apple     |
  | aba      | function  |
  | aaa      | wondering |
  | abca     | behabeha  |
  | abab     | technology|
