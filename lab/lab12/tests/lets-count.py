test = {
  'name': 'lets-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from sp16favnum;
          69|33
          sqlite> SELECT * from sp16favpets;
          |17
          dragon|15
          dog|13
          paul hilfinger|10
          pikachu|7
          cat|6
          unicorn|6
          chinchilla|5
          phoenix|5
          puppy|5
          sqlite> SELECT * from fa16favpets;
          dog|31
          cat|22
          tiger|18
          panda|10
          penguin|8
          harambe|7
          wolf|7
          elephant|6
          dolphin|5
          dragon|5
          sqlite> SELECT * from fa16dragon;
          dragon|5
          sqlite> SELECT * from fa16alldragons;
          a dragon|9
          sqlite> SELECT * from obedienceimage;
          7|Image 1|19
          7|Image 2|39
          7|Image 3|41
          7|Image 4|55
          7|Image 5|19
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
