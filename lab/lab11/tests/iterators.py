test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [1, [2, [3, [4]]]]
          >>> t = iter(s)
          >>> next(t)
          94ce22b5936436a75abf185df37ba826
          # locked
          >>> next(iter(next(t)))
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          >>> list(t)
          1f73c5ccb26eee699414362be850992d
          # locked
          >>> next(map(lambda x: x * x, filter(lambda y: y > 4, range(10))))
          14ab153d524c1654e090dd7f3fae4e31
          # locked
          >>> tuple(map(abs, reversed(range(-6, -4))))
          428f4ba08d2da7d24e73b8bf529ce614
          # locked
          >>> r = reversed(range(10000))
          >>> next(r) - next(r)
          94ce22b5936436a75abf185df37ba826
          # locked
          >>> xs = [2, 3, 4, 5]
          >>> y, z = iter(xs), iter(xs)
          >>> next(zip(y, z))
          69c3a67c61a48e19d31c19619ac12c8b
          # locked
          >>> next(zip(y, y))
          f7a0da3a12d6b603f496553c79d6eb94
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
