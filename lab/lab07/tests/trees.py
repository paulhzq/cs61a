test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree(1, Tree(2)) # Enter Function if you believe the answer is <function ...>, Error if it errors, and Nothing if nothing is displayed.
          Error
          >>> t = Tree(1, [Tree(2)])
          >>> t.root
          1
          >>> t.branches[0]
          Tree(2)
          >>> t.branches[0].root
          2
          >>> t.root = t.branches[0].root
          >>> t
          Tree(2, [Tree(2)])
          >>> t.branches.append(Tree(4, [Tree(8)]))
          >>> len(t.branches)
          2
          >>> t.branches[0]
          Tree(2)
          >>> t.branches[1]
          Tree(4, [Tree(8)])
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
