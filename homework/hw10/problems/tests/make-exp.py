test = {
  'name': 'make-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-exp 2 4)
          4deb0f03341bd98828653e1ac5731c87
          # locked
          scm> (make-exp 'x 1)
          5d643de01ee901515c3958fa5a17f9b8
          # locked
          scm> (make-exp 'x 0)
          edfeeea8163e0f3edfc46b985f61aebc
          # locked
          scm> x^2
          b31ed29ae8416257ad61f9c040fe5db0
          # locked
          scm> (base x^2)
          5d643de01ee901515c3958fa5a17f9b8
          # locked
          scm> (exponent x^2)
          7907742dd1d7ab350a6505d2374013f8
          # locked
          scm> (exp? x^2) ; True or False
          19afb82a4eb2dbbd94f99f87d967e36f
          # locked
          scm> (exp? 1)
          b34cb09c4b3085c4f9ebe21494519fc1
          # locked
          scm> (exp? 'x)
          b34cb09c4b3085c4f9ebe21494519fc1
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw10)
      scm> (define x^2 (make-exp 'x 2))
      scm> (define x^3 (make-exp 'x 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
