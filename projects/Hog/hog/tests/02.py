test = {
  'name': 'Question 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> take_turn(2, 0, make_test_dice(4, 6, 1))
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(3, 0, make_test_dice(4, 6, 1))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 35)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 71)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 7)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 0)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(2, 0, make_test_dice(6))
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(1, 0, make_test_dice(3)) # Remember Hogtimus Prime!
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(2, 0, make_test_dice(2, 3, 5))
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(1, 0, make_test_dice(2))
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 60)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 10)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 24)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(10, 0, make_test_dice(5)) # Remember When Pigs Fly!
          15
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(9, 0, make_test_dice(4))
          16
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(8, 0, make_test_dice(4))
          17
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(7, 0, make_test_dice(4))
          18
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(6, 0, make_test_dice(4))
          19
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
          >>> hog.take_turn(5, 0) # Make sure you call roll_dice!
          Called roll dice!
          20
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> def roll_dice(num_rolls, dice):
      ...     print("Called roll dice!")
      ...     return 9002
      ...
      >>> hog.roll_dice, old_roll_dice = roll_dice, hog.roll_dice
      """,
      'teardown': r"""
      >>> hog.roll_dice = old_roll_dice
      """,
      'type': 'doctest'
    }
  ]
}
