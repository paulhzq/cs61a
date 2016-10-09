test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> select_dice(4, 24, False).__name__ == 'rerolled'
          True
          >>> select_dice(16, 64, False).__name__ == 'rerolled'
          False
          >>> select_dice(0, 0, True).__name__ == 'rerolled'
          True
          >>> select_dice(50, 80, True).__name__ == 'rerolled'
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> select_dice(4, 25, False) == six_sided
          True
          >>> select_dice(3, 4, False) == six_sided
          False
          >>> select_dice(0, 0, True) == six_sided
          False
          >>> select_dice(60, 80, True) == six_sided
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> select_dice(4, 25, False) == four_sided
          False
          >>> select_dice(3, 4, False) == four_sided
          False
          >>> select_dice(0, 0, True) == four_sided
          False
          >>> select_dice(50, 80, True) == four_sided
          True
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
