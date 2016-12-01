test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sign -42)
          62688045139d8ebd9ec47bcd78380051
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 0)
          023f53b43f605b7580be5aa5c3e5ee7e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 42)
          d7ab3c9f4f7487833d3cb935fc8c712a
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
