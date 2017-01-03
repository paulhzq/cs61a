test = {
  'name': 'parent',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from by_height;
          herbert
          fillmore
          abraham
          delano
          grover
          barack
          clinton
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': r"""
      sqlite> .read hw13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
