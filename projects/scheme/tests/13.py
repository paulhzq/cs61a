test = {
  'name': 'Question 13',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (and)
          a48ad7c6cb9d8be0928e7032acab2fdd
          # locked
          # choice: True
          # choice: False
          # choice: SchemeError
          scm> (and 1 False)
          0840a73cb74e45d8ad7cd102c34eac98
          # locked
          # choice: 1
          # choice: True
          # choice: False
          scm> (and (+ 1 1) 1)
          1d6ef7880cd9b59b64a1f4e1a1e35a12
          # locked
          # choice: 2
          # choice: 1
          # choice: (+ 1 1)
          # choice: True
          scm> (and False 5)
          0840a73cb74e45d8ad7cd102c34eac98
          # locked
          # choice: 5
          # choice: True
          # choice: False
          scm> (and 4 5 (+ 3 3))
          81465e2dabdcdea0628897014da02da9
          # locked
          scm> (and True False 42 (/ 1 0))
          0840a73cb74e45d8ad7cd102c34eac98
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (and 3 2 False)
          False
          scm> (and 3 2 1)
          1
          scm> (and 3 False 5)
          False
          scm> (and 0 1 2 3)
          3
          scm> (define (true-fn) #t)
          true-fn
          scm> (and (true-fn))
          True
          scm> (define x False)
          x
          scm> (and x True)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          x
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      #f
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          False
          scm> x
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (and #t #t #t #t))
          no-mutation
          scm> no-mutation
          (lambda () (and True True True True))
          scm> (no-mutation)
          True
          scm> no-mutation ; `and` should not cause mutation
          (lambda () (and True True True True))
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
          scm> (or)
          0840a73cb74e45d8ad7cd102c34eac98
          # locked
          # choice: True
          # choice: False
          # choice: SchemeError
          scm> (or (+ 1 1))
          4b7283d4dfa392633549336acb032de7
          # locked
          # choice: 2
          # choice: True
          # choice: False
          # choice: (+ 1 1)
          scm> (or False)
          0840a73cb74e45d8ad7cd102c34eac98
          # locked
          # choice: True
          # choice: False
          # choice: SchemeError
          scm> (define (t) True)
          1df7257f69b999dcc606ccacfbfae648
          # locked
          scm> (or (t) 3)
          a48ad7c6cb9d8be0928e7032acab2fdd
          # locked
          # choice: 3
          # choice: True
          # choice: False
          scm> (or 5 2 1)
          39dba75757e21a295c7803a12e1e5877
          # locked
          scm> (or False (- 1 1) 1)
          fe0c8b4127bfc1ab429bd306a95eda1e
          # locked
          scm> (or 4 True (/ 1 0))
          5dc34dbe25d53109ac62b4184b75a40f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (or 0 1 2)
          0
          scm> (or 'a False)
          a
          scm> (or (< 2 3) (> 2 3) 2 'a)
          True
          scm> (or (< 2 3) 2)
          True
          scm> (define (false-fn) #f)
          false-fn
          scm> (or (false-fn) 'yay)
          yay
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          False
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     #t
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          True
          scm> x
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (or #f #f #f #f))
          no-mutation
          scm> no-mutation
          (lambda () (or False False False False))
          scm> (no-mutation)
          False
          scm> no-mutation ; `or` should not cause mutation
          (lambda () (or False False False False))
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
