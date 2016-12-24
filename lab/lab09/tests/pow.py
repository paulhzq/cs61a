test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow 4 0)
          1
          scm> (pow 10 3)
          1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (pow 2 3)
          8
          scm> (pow 2 5)
          32
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (pow 3 3)
          27
          scm> (pow 3 4)
          81
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
