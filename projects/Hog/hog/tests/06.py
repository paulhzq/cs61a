test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If this causes an error, write AssertionError
          >>> check_strategy(always_roll(5)) == None
          bc6c4798917b91886d7fa5f56e42878f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def fail_15_20(score, opponent_score):
          ...     if score == 15 and opponent_score == 20:
          ...         return 100
          ...     return 5
          >>> # If this causes an error, write AssertionError
          >>> check_strategy(fail_15_20) == None
          cfc38925cef46fde683fbb0cbb4d4025
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def fail_102_115(score, opponent_score):
          ...     if score == 102 and opponent_score == 115:
          ...         return 100
          ...     return 5
          >>> fail_102_115 == check_strategy(fail_102_115, 120)
          AssertionError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure that you check all valid pairs of scores!
          >>> # Scores can range from 0 to the goal score for both players.
          >>> all_scores = set()
          >>> def check_completeness(score, opponent_score):
          ...     all_scores.add((score, opponent_score))
          ...     return 5
          >>> # Be specific about the error type (AssertionError, rather than Error)
          >>> check_strategy(check_completeness)
          >>> count = 0
          >>> for score in range(100):
          ...     for opponent_score in range(100):
          ...         if (score, opponent_score) in all_scores:
          ...             count += 1
          >>> count
          10000
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
