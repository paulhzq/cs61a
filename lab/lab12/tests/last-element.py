test = {
  'name': 'last-element',
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
          logic> (query (last-element (a b c) c))
          Success!
          logic> (query (last-element (3) ?x))
          Success!
          x: 3
          logic> (query (last-element (1 2 3) ?x))
          Success!
          x: 3
          logic> (query (last-element (2 ?x) 3))
          Success!
          x: 3
          """,
          'hidden': False,
          'locked': False,
        },
      ]
    }
  ]
}
