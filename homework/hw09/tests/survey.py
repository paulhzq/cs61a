test = {
  'name': 'survey',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (survey)
          187e2cd1a95f0071d8b510405a8c7577
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
