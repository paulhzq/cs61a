test = {
  'name': 'matchmaker',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          pupper|Sandstorm|seven|maroon
          bear|Starman|blue|orange
          giraffe|Closer|red|green
          dog|Closer|blue|blue
          dog|Closer|blue|red
          dog|Closer|blue|purple
          dog|Closer|blue|blue
          dog|Closer|blue|blue
          dog|Closer|blue|black
          dog|Closer|blue|purple
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
