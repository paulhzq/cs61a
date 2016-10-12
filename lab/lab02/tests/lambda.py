test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lambda x: x # Remember to write Function if it's a function, Error if it errors, and Nothing if nothing is displayed.
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> a = lambda x: x
          >>> a(5)  # x is the parameter for the lambda function
          d330e4294a4387ed4475ee0e95da5386
          # locked
          >>> b = lambda: 3
          >>> b()
          0f10194daf41a11a30f4adc80d959f28
          # locked
          >>> c = lambda x: lambda: print('123')
          >>> c(88)
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> c(88)()
          9e02ad5c0fa59ae9cdfdc7c71cc425b7
          # locked
          >>> d = lambda f: f(4)  # They can have functions as arguments as well.
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          9024755e0e6b1907cc6e80a977eb6fa3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> t = lambda f: lambda x: f(f(f(x)))
          >>> s = lambda x: x + 1
          >>> t(s)(0)
          0f10194daf41a11a30f4adc80d959f28
          # locked
          >>> bar = lambda y: lambda x: pow(x, y)
          >>> bar()(15)
          ab06d135c02ab203238caafbf77976ce
          # locked
          >>> foo = lambda: 32
          >>> foobar = lambda x, y: x // y
          >>> a = lambda x: foobar(foo(), bar(4)(x))
          >>> a(2)
          dcbe12f5edfd80d067e49a65db66d0b1
          # locked
          >>> b = lambda x, y: print('summer')  # When is the body of this function run?
          358b0ae001277273d8cd480ce5dbfb82
          # locked
          >>> c = b(4, 'dog')
          d8406c888e61cc29bc2b01c759a4c5c0
          # locked
          >>> print(c)
          7b760505602b62a147678e737b04445f
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> a = lambda b: b * 2
          358b0ae001277273d8cd480ce5dbfb82
          # locked
          >>> a
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> a(a(a(2)))
          9024755e0e6b1907cc6e80a977eb6fa3
          # locked
          >>> a(a(a()))
          ab06d135c02ab203238caafbf77976ce
          # locked
          >>> def d():
          ...     print(None)
          ...     print('whoo')
          >>> b = d()
          7b760505602b62a147678e737b04445f
          b36b589ffa89d962952abb0a58daf8ad
          # locked
          >>> b
          358b0ae001277273d8cd480ce5dbfb82
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x, y, z = 1, 2, 3
          >>> a = lambda b: x + y + z
          >>> x += y
          >>> y -= z
          >>> a('b')
          d330e4294a4387ed4475ee0e95da5386
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> z = 3
          >>> e = lambda x: lambda y: lambda: x + y + z
          >>> e(0)(1)()
          ef6b0e7c554b5515158e88d1ee908645
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
