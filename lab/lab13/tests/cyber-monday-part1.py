test = {
  'name': 'cyber-monday-part1',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM average_prices;
          computer|109.09
          games|349.99
          phone|89.99
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
