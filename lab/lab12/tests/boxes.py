test = {
  'name': 'boxes',
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
          logic> (query (boxes (( 1  2  4 ?a)
          ......                ( 4 ?b  2  1)
          ......                (?c  4  3  2)
          ......                ( 2  3  4 ?d))))
          Success!
          a: 3	b: 3	c: 1	d: 1
          """,
          'hidden': False,
          'locked': False,
        },
      ]
    }
  ]
}
