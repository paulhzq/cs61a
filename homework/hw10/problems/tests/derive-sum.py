test = {
  'name': 'derive-sum',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-sum 1 3)
          e7bbf92744f33acda0f8f4d93ef2bb79
          # locked
          scm> (make-sum 'x 0)
          5d643de01ee901515c3958fa5a17f9b8
          # locked
          scm> (make-sum 0 'x)
          5d643de01ee901515c3958fa5a17f9b8
          # locked
          scm> (make-sum 'a 'x)
          5a9774332b0568eb8fd085503136dc7a
          # locked
          scm> (make-sum 'a (make-sum 'x 1))
          83acb82c8a831c063eaa5ab51f886872
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw10)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (derive '(+ x 3) 'x)
          edfeeea8163e0f3edfc46b985f61aebc
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw10)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
