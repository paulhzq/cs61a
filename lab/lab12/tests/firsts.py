test = {
  'name': 'firsts',
  'points': 1,
  'suites': [
    {
      'scored': False,
      'setup': """
      logic> (load lab12.logic)
      logic> (load lab12_extra.logic)
      """,
      'type': 'logic',
      'cases': [
        {
          'code': """
          logic> (query (firsts ((1 2 3 4) (2 3 4 5) (1 2 3 4) (1 2 3 2)) ?x))
          Success!
          x: (1 2 1 1)
          logic> (query (firsts ((2 3 4) (3 4 5) (2 3 4) (2 3 2)) ?y))
          Success!
          y: (2 3 2 2)
          logic> (query (firsts ((?x 2 3) (4 5 6) (?y 8 9)) (1 4 7)))
          Success!
          x: 1	y: 7
          """,
          'hidden': False,
          'locked': False,
        },
      ]
    }
  ]
}
