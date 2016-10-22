test = {
  'name': 'List Comprehension',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [x*x for x in range(5)]
          c41346d26e0d7126b4eb1d6986c930bf
          # locked
          >>> [n for n in range(10) if n % 2 == 0]
          7a7f804f85741d6d6a92d03b36aa768d
          # locked
          >>> ones = [1 for i in ["hi", "bye", "you"]]
          >>> ones + [str(i) for i in [6, 3, 8, 4]]
          02ff83244e685c3c3d59303313b17287
          # locked
          >>> [i+5 for i in [n for n in range(1,4)]]
          0588f018cf09ee37f4ab5f41ec637dc7
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
          >>> [i**2 for i in range(10) if i < 3]
          7b868e71aaea249c2a9b6298c0aa78af
          # locked
          >>> lst = ['hi' for i in [1, 2, 3]]
          >>> print(lst)
          56e01ac39888835178f9d8659e723e6c
          # locked
          >>> lst + [i for i in ['1', '2', '3']]
          50230d3566127956af6676061299eec4
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
