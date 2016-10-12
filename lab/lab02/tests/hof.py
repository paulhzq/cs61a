test = {
  'name': 'HOF',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def first(x):
          ...     x += 8
          ...     def second(y):
          ...         print('second')
          ...         return x + y
          ...     print('first')
          ...     return second
          >>> f = first(15)
          0cd62462fa747373868997245aecd4b2
          # locked
          >>> f
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> f(16)
          eb79794267854191554e088876646a17
          45daa0af063be1f2e19d22b17c5d51ed
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def even(f):
          ...     def odd(x):
          ...         if x < 0:
          ...             return f(-x)
          ...         return f(x)
          ...     return odd
          >>> stevphen = lambda x: x
          >>> stewart = even(stevphen)
          >>> stewart
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> stewart(61)
          fca276f013f718468273f07db52f3ab7
          # locked
          >>> stewart(-4)
          ef6b0e7c554b5515158e88d1ee908645
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
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> a = cake()
          0127137631d037670fa6a894e2d548ee
          # locked
          >>> a
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> a()
          28f5a700252060ec3bbc4bf4ca744c56
          7fccab88a7c3c0cbffe0142e723d1984
          # locked
          >>> x, b = a(), cake
          28f5a700252060ec3bbc4bf4ca744c56
          # locked
          >>> def snake(x):
          ...    if cake == b:
          ...        x += 3
          ...        return lambda y: y + x
          ...    else:
          ...        return y - x
          >>> snake(24)(23)
          6376374a6075fc68c3e4a835f97f30b6
          # locked
          >>> cake = 2
          >>> snake(26)
          ab06d135c02ab203238caafbf77976ce
          # locked
          >>> y = 50
          >>> snake(26)
          bd59b8d19695b1f54764d0bac625563f
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
