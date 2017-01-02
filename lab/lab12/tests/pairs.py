test = {
  'name': 'pairs',
  'points': 0,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab12.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM pairs LIMIT 10;
          0|0
          0|1
          0|2
          0|3
          0|4
          0|5
          0|6
          0|7
          0|8
          0|9
          sqlite> SELECT x, y FROM pairs WHERE x + y = 42 LIMIT 10;
          0|42
          1|41
          2|40
          3|39
          4|38
          5|37
          6|36
          7|35
          8|34
          9|33
          """,
        },
      ],
    },
  ]
}
