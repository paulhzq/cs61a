test = {
  'name': 'solve',
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
          logic> (query (solve (( 1 ?b  4 ?d)
          ......                (?e  3 ?g  1)
          ......                (?i  4 ?k  2)
          ......                ( 2 ?n  3 ?p))))
          Success!
          b: 2	d: 3	e: 4	g: 2	i: 3	k: 1	n: 1	p: 4
          """,
          'hidden': False,
          'locked': False,
        },
      ]
    }
  ]
}
