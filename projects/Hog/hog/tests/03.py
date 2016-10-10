test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_dice = reroll(make_test_dice(2, 4, 6))
          >>> test_dice()
          2
          >>> test_dice()
          4
          >>> test_dice()
          6
          >>> test_dice()
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test_dice = reroll(make_test_dice(1, 3, 5))
          >>> test_dice()
          3
          >>> test_dice()
          1
          >>> test_dice()
          5
          >>> test_dice()
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test_dice = reroll(make_test_dice(3, 2, 4, 1, 5))
          >>> test_dice()
          2
          >>> test_dice()
          4
          >>> test_dice()
          5
          >>> test_dice()
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test_dice = reroll(make_test_dice(1, 1, 1, 1, 2))
          >>> test_dice()
          1
          >>> test_dice()
          1
          >>> test_dice()
          2
          >>> test_dice()
          1
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
