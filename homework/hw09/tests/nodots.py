test = {
  'name': 'nodots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (nodots '(1 . 2))
          16e7f90f3997618367c64ff4a1c02218
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 2 . 3))
          48b7a4131742f3894e7fa335b573b4fa
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '((1 . 2) 3))
          a18f22de846ec3d9a784505fd84b4a81
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 (2 3 . 4) . 3))
          539ce7c99587b5a410f10ca8bd7e3fab
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 . ((2 3 . 4) . 3)))
          539ce7c99587b5a410f10ca8bd7e3fab
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
