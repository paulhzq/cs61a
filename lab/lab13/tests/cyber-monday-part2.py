test = {
  'name': 'cyber-monday-par2',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM lowest_prices;
          GameStation|Hallmart|298.98
          QBox|Targive|390.98
          iBook|Targive|110.99
          kBook|RestBuy|94.99
          qPhone|Hallmart|85.99
          rPhone|Hallmart|69.99
          uPhone|RestBuy|89.99
          wBook|RestBuy|114.29
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
