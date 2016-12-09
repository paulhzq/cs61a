test = {
  'name': 'Question 4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> twos = Pair(2, Pair(2, nil))
          >>> plus = PrimitiveProcedure(scheme_add) # + procedure
          >>> scheme_apply(plus, twos, env)
          5dc34dbe25d53109ac62b4184b75a40f
          # locked
          # choice: 4
          # choice: SchemeError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> twos = Pair(2, Pair(2, nil))
          >>> oddp = PrimitiveProcedure(scheme_oddp) # odd? procedure
          >>> scheme_apply(oddp, twos, env)
          0b51df1e150843e094f5a67945b0c704
          # locked
          # choice: True
          # choice: False
          # choice: SchemeError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> two = Pair(2, nil)
          >>> eval = PrimitiveProcedure(scheme_eval, True) # eval procedure
          >>> scheme_apply(eval, two, env) # be sure to check use_env
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> args = nil
          >>> def make_scheme_counter():
          ...     x = 0
          ...     def scheme_counter():
          ...         nonlocal x
          ...         x += 1
          ...         return x
          ...     return scheme_counter
          >>> counter = PrimitiveProcedure(make_scheme_counter()) # counter
          >>> scheme_apply(counter, args, env) # only call procedure.fn once!
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
