test = {
  'name': 'Question 5',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'While score0 and score1 are both less than goal',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          The variables score0 and score1 are the scores for both
          players. Under what conditions should the game continue?
          """
        },
        {
          'answer': 'strategy1(score1, score0)',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Play function stops at goal
          >>> s0, s1 = hog.play(always_roll(5), always_roll(3), score0=91, score1=10)
          >>> s0
          106
          >>> s1
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Goal score is not hardwired, Hog Wild, When Pigs Fly
          >>> s0, s1 = hog.play(always_roll(5), always_roll(5), goal=10)
          >>> s0
          20
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Swine Swap
          >>> s0,s1 = hog.play(always_roll(5), always_roll(3), score0=5, score1=40, goal=50)
          >>> s0
          55
          >>> s1
          29
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_roll = hog.always_roll
      >>> hog.reroll = lambda d: hog.make_test_dice(5)
      >>> hog.six_sided = hog.make_test_dice(3)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Swine swap applies to 3 digit scores
          >>> s0, s1 = hog.play(always_roll(5), always_roll(3), score0=95, score1=55)
          >>> s0
          55
          >>> s1
          110
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Goal edge case
          >>> s0, s1 = hog.play(always_roll(4), always_roll(3), score0=88, score1=20)
          >>> s0
          100
          >>> s1
          20
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Player 1 win
          >>> s0, s1 = hog.play(always_roll(2), always_roll(4), score0=87, score1=88)
          >>> s0
          97
          >>> s1
          100
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Check strategies are actually used correctly
          >>> strat0 = lambda score, opponent: opponent % 10
          >>> strat1 = lambda score, opponent: opponent // 10
          >>> s0, s1 = hog.play(strat0, strat1, score0=40, score1=92)
          >>> s0
          102
          >>> s1
          62
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Swine swap applies during Player 1 turn
          >>> s0, s1 = hog.play(always_roll(5), always_roll(5), score0=40, score1=95)
          >>> s0
          110
          >>> s1
          55
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Free bacon refers to correct opponent score
          >>> s0, s1 = hog.play(always_roll(0), always_roll(0), score0=11, score1=99)
          >>> s0
          21
          >>> s1
          104
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Handle multiple turns
          >>> s0, s1 = hog.play(always_roll(0), always_roll(0))
          >>> s0
          101
          >>> s1
          98
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Handle multiple turns
          >>> s0, s1 = hog.play(always_roll(5), always_roll(0))
          >>> s0
          110
          >>> s1
          47
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_roll = hog.always_roll
      >>> hog.reroll = lambda d: hog.make_test_dice(5)
      >>> hog.six_sided = hog.make_test_dice(3)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Assume that six-sided dice are in play
          >>> s0, s1 = hog.play(always_roll(-1), always_roll(3), score0=98, score1=91)
          >>> s0
          100
          >>> s1
          96
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Assume that six-sided dice are in play
          >>> s0, s1 = hog.play(always_roll(-1), always_roll(3), score0=97, score1=90)
          >>> s0
          99
          >>> s1
          104
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Assume that six-sided dice are in play
          >>> s0, s1 = hog.play(always_roll(-1), always_roll(3))
          >>> s0
          13
          >>> s1
          101
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Assume that six-sided dice are in play
          >>> s0, s1 = hog.play(always_roll(2), always_roll(-1))
          >>> s0
          104
          >>> s1
          20
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_roll = hog.always_roll
      >>> hog.reroll = lambda d: hog.make_test_dice(5)
      >>> hog.six_sided = hog.make_test_dice(3)
      >>> hog.four_sided = hog.make_test_dice(1)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> tests.play_utils.check_play_function(hog)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling take_turn once per turn!
      >>> import hog, importlib
      >>> importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
