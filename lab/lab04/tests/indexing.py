test = {
  'name': 'List Indexing',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 3, [5, 7], 9] # Write the code that indexes into x to output the 7
          3450d5df7f6d639c9dc883cf31cc62bd
          # locked
          >>> x = [[7]] # Write the code that indexes into x to output the 7
          03e2a566fa83f164d9923dd9c2392471
          # locked
          >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]] # Write the code that indexes into x to output the 7
          c66ba79adb64caf370da3e75203f8912
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
          >>> lst = [3, 2, 7, [84, 83, 82]]
          >>> lst[4] # Write Error if this will error
          8dfecce35cfbb620490b1aa9637bdafd
          # locked
          >>> lst = [3, 2, 7, [84, 83, 82]] # Write the code that indexes into lst to output the 82
          81ba29659b20c26d274bf1958abc576c
          # locked
          >>> lst[3][0]
          89d2c4e2851d68c81d820360eb31bc36
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
