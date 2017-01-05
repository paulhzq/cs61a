test = {
  'name': 'flights',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM flight_costs;
          1|20
          2|30
          3|40
          4|55
          5|72
          6|93
          7|82
          8|92
          9|97
          10|109
          11|123
          12|141
          13|162
          14|151
          15|161
          16|166
          17|178
          18|192
          19|210
          20|231
          21|220
          22|230
          23|235
          24|247
          25|261
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
