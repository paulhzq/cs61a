test = {
  'name': 'flights',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM healthiest_meats;
          tofurky|1400
          turkey|1900
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
