test = {
  'name': 'Question 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> swap_strategy(33, 60, 8, 6)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> swap_strategy(30, 54, 8, 6)
          327b19ffebddf93982e1ad2a4a6486f4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> swap_strategy(7, 23, 8, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(7, 26, 8, 6)
          0
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> swap_strategy(10, 38, 8, 6) # beneficial
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(9, 1, 8, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(35, 28, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(37, 24, 8, 6)
          6
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
