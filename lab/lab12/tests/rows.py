test = {
  'name': 'rows',
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
          logic> (query (rows (( 1  2  4 ?a)
          ......               (?b  3  2  1)
          ......               (?c  4  3  2)
          ......               ( 2  4  3 ?d))))
          Success!
          a: 3	b: 4	c: 1	d: 1
          """,
          'hidden': False,
          'locked': False,
        },
      ]
    }
  ]
}
