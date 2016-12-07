test = {
  'name': 'how-many-dots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (how-many-dots '(1 2 3))
          ebcdbae5d1e87206f8083fab311797e0
          # locked
          scm> (how-many-dots '(1 2 . 3))
          7710be362067e7ad1033e06983157f3e
          # locked
          scm> (how-many-dots '((1 . 2) 3 . 4))
          a1dc4335afc0b80728d0ea0f5e60ac87
          # locked
          scm> (how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
          d79950140aa30120bd9b9ff9789ce336
          # locked
          scm> (how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7))))))))
          ebcdbae5d1e87206f8083fab311797e0
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz10)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
