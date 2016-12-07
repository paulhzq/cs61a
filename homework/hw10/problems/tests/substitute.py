test = {
  'name': 'substitute',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (substitute '(c a b) 'b 'l)
          1207c1069867ba456891020014f2f641
          # locked
          scm> (substitute '(f e a r s) 'f 'b)
          4930e8c8e2751d9bd86f11f63c118a69
          # locked
          scm> (substitute '(g (o) o (o)) 'o 'r)
          c9b5606614f7553407034015aa8b4a49
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (substitute '((lead guitar) (bass guitar) (rhythm guitar) drums)
          ....               'guitar 'axe)
          ((lead axe) (bass axe) (rhythm axe) drums)
          scm> (substitute '(romeo romeo wherefore art thou romeo) 'romeo 'paris)
          (paris paris wherefore art thou paris)
          scm> (substitute '((to be) or not (to (be))) 'be 'eat)
          ((to eat) or not (to (eat)))
          scm> (substitute '(a b (c) d e) 'foo 'bar)
          (a b (c) d e)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw10)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
