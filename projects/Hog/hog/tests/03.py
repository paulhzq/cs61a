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
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          >>> test_dice()
          edcbd82ba98a8122be244fa325c62071
          # locked
          >>> test_dice()
          327b19ffebddf93982e1ad2a4a6486f4
          # locked
          >>> test_dice()
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> test_dice = reroll(make_test_dice(1, 3, 5))
          >>> test_dice()
          16e2cf37e8254529473d9e0a36b75fcb
          # locked
          >>> test_dice()
          43d176e102c8d95338faf8791aa509b3
          # locked
          >>> test_dice()
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          >>> test_dice()
          16e2cf37e8254529473d9e0a36b75fcb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> test_dice = reroll(make_test_dice(3, 2, 4, 1, 5))
          >>> test_dice()
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          >>> test_dice()
          edcbd82ba98a8122be244fa325c62071
          # locked
          >>> test_dice()
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          >>> test_dice()
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True
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
