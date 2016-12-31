test = {
  'name': 'has-cycle-constant',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (has-cycle-constant s)
          False
          scm> (has-cycle-constant cycle)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw12)
      scm> (define s (cons-stream 1 (cons-stream 2 nil)))
      scm> (define cycle (cons-stream 1 (cons-stream 2 cycle)))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
