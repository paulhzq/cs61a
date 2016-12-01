test = {
  'name': 'cadr-caddr',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cddr '(1 2 3 4))
          7273c8a12002a292d246841184d6eb98
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cadr '(1 2 3 4))
          3940351fe1ecdc23ea60a8fdad9aa11d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (caddr '(1 2 3 4))
          d17a76b23ca9a0f23c264eaf1fedfa70
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
