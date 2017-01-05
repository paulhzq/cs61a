test = {
  'name': 'schedule',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM schedule;
          SFO, SLC, PDX|176
          SFO, LAX, PDX|186
          SFO, PDX|192
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
