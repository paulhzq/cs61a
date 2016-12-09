test = {
  'name': 'Question 15',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 1)
          c55ea5b1bca40acd76b8c213f8a08f8b
          # locked
          scm> (let ((x 5))
          ....    (+ x 3))
          29cbea0405f55882914cb294257af1c1
          # locked
          scm> x
          1d6ef7880cd9b59b64a1f4e1a1e35a12
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (let ((a 1) (b a)) b)
          0b51df1e150843e094f5a67945b0c704
          # locked
          # choice: SchemeError
          # choice: 1
          # choice: x
          # choice: y
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (let ((x 5))
          ....    (let ((x 2)
          ....          (y x))
          ....        (+ y (* x 2))))
          9cc890fba2180e73142276346c5369b9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define (square x) (* x x))
          square
          scm> (define (f x y)
          ....    (let ((a (+ 1 (* x y)))
          ....          (b (- 1 y)))
          ....        (+ (* x (square a))
          ....           (* y b)
          ....           (* a b))))
          f
          scm> (f 3 4)
          456
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 3)
          x
          scm> (define y 4)
          y
          scm> (let ((x (+ y 2))
          ....       (y (+ x 2)))
          ....      (cons x y))
          (6 . 5)
          scm> (let ((x 'hello)) x)
          hello
          scm> (define z 0)
          z
          scm> (let ((a (define z (+ z 1)))) z)
          1
          scm> (let ((x 1)
          ....       (y 3))
          ....    (define x (+ x 1))
          ....    (cons x y))
          (2 . 3)
          scm> (let ((a 1 1)) a)
          SchemeError
          scm> (let ((a 1) (2 2)) a)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
