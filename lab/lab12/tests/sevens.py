test = {
  'name': 'sevens',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sevens;
          7
          I do what I want.
          7
          You are not the boss of me!
          7
          I do what I want.
          Choose this option instead.
          I\'m a rebel
          7
          YOLO!
          I do what I want.
          7
          7
          I\'m a rebel
          7
          7
          7
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
