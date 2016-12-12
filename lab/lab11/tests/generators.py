test = {
  'name': 'Generators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def generator():
          ...     print("Starting here")
          ...     i = 0
          ...     while i < 6:
          ...         print("Before yield")
          ...         yield i
          ...         print("After yield")
          ...         i += 1
          >>> g = generator() # what type of object is this?
          >>> g == iter(g) # equivalent of g.__iter__()
          308968ce50a38a2957823e1439417bf2
          # locked
          >>> next(g) # equivalent of g.__next__()
          13a515abbb3b8d304d0a5a4b3021b098
          2e7d8dbafba7985fd02fc693bc61218b
          4b569bf0e21d6369c5343767f1146f64
          # locked
          >>> next(g)
          265038a6c2ed6f967cfa87d2dcd13485
          2e7d8dbafba7985fd02fc693bc61218b
          94ce22b5936436a75abf185df37ba826
          # locked
          >>> next(g)
          265038a6c2ed6f967cfa87d2dcd13485
          2e7d8dbafba7985fd02fc693bc61218b
          805a87056a1a3fd559e4ef12a815b2be
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
