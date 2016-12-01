test = {
  'name': 'ordered?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ordered? '(1 2 3 4 5))  ; True or False
          7346f33f3682a13d51291338e62f5a0f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(1 5 2 4 3))  ; True or False
          eb89d68eec1597c385d6e0ac3e3c6d52
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(2 2))  ; True or False
          7346f33f3682a13d51291338e62f5a0f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(1 2 2 4 3))  ; True or False
          eb89d68eec1597c385d6e0ac3e3c6d52
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
