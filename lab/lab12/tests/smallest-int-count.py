test = {
  'name': 'smallest-int-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_count LIMIT 50;
          1|81
          2|11
          3|10
          4|13
          5|6
          6|8
          7|13
          8|12
          9|9
          10|1
          11|11
          12|8
          13|6
          14|13
          15|5
          16|4
          17|13
          18|3
          19|11
          21|4
          22|5
          23|17
          24|4
          25|1
          26|5
          27|3
          28|1
          29|3
          30|3
          31|5
          32|3
          33|3
          34|8
          35|2
          36|2
          37|5
          38|7
          39|4
          41|4
          42|4
          43|5
          44|1
          46|2
          47|2
          48|1
          52|2
          54|1
          56|2
          57|2
          59|1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
