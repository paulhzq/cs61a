test = {
  'name': 'derive-product',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-product 2 3)
          b5ae24cd9ab85d2538c53cfd696507c9
          # locked
          scm> (make-product 'x 0)
          4f707e907a1e81019f393aa4bed2928e
          # locked
          scm> (make-product 1 'x)
          5d643de01ee901515c3958fa5a17f9b8
          # locked
          scm> (make-product 'a 'x)
          dfa8b1cc8ac2cbe8b2cbbade325001a5
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw10)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (derive '(* x y) 'x)
          y
          scm> (derive '(* (* x y) (+ x 3)) 'x)
          (+ (* y (+ x 3)) (* x y))
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
