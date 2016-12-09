test = {
  'name': 'Question 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (lambda (x y) (+ x y))
          d579a305762000c8ae036c510fb2baf6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (lambda (x) (+ x) (+ x x))
          (lambda (x) (+ x) (+ x x))
          scm> (lambda (x))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (lambda () 2)
          (lambda () 2)
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
          >>> lambda_line = read_line("(lambda (x y) x)")
          >>> lambda_proc = do_lambda_form(lambda_line.second, env)
          >>> isinstance(lambda_proc, LambdaProcedure)
          True
          >>> lambda_proc.env is env
          True
          >>> lambda_proc
          LambdaProcedure(Pair('x', Pair('y', nil)), Pair('x', nil), <Global Frame>)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      >>> from scheme import *
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
