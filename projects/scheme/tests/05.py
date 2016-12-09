test = {
  'name': 'Question 5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> expr = read_line('(+ 2 2)')
          >>> expr
          ea71d6537edb33a861db67994c99d0c1
          # locked
          >>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
          5dc34dbe25d53109ac62b4184b75a40f
          # locked
          >>> expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
          >>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
          dfa6909c6aed8fc69176ff06e8383ec2
          # locked
          >>> expr = read_line('(yolo)')
          >>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
          0b51df1e150843e094f5a67945b0c704
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (+ 2 3) ; Type SchemeError if you think this errors
          39dba75757e21a295c7803a12e1e5877
          # locked
          scm> (* (+ 3 2) (+ 1 7)) ; Type SchemeError if you think this errors
          bc68e7f6089e3fb3f82e50eab363155b
          # locked
          scm> (1 2) ; Type SchemeError if you think this errors
          0b51df1e150843e094f5a67945b0c704
          # locked
          scm> (1 (print 0)) ; check_procedure should be called before operands are evaluated
          0b51df1e150843e094f5a67945b0c704
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (+)
          0
          scm> (odd? 13)
          True
          scm> (car (list 1 2 3 4))
          1
          scm> (car car)
          SchemeError
          scm> (odd? 1 2 3)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (+ (+ 1) (* 2 3) (+ 5) (+ 6 (+ 7)))
          25
          scm> (*)
          1
          scm> (-)
          SchemeError
          scm> (car (cdr (cdr (list 1 2 3 4))))
          3
          scm> (car cdr (list 1))
          SchemeError
          scm> (* (car (cdr (cdr (list 1 2 3 4)))) (car (cdr (list 1 2 3 4))))
          6
          scm> (* (car (cdr (cdr (list 1 2 3 4)))) (cdr (cdr (list 1 2 3 4))))
          SchemeError
          scm> (+ (/ 1 0))
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
