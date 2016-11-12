test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab07 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link.rest.first
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> link.rest.rest.rest is Link.empty
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> link.first = 9001
          >>> link.first
          2c9f5ddf74d01d9aa3f7f14577718d55
          # locked
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          9a023de211dac9bf8558350f5fa3bdca
          # locked
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest.rest.rest.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link2.rest.first
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> print_link(link2) # Look at print_link in lab07.py
          d497ebcf288da6a97a4225117ac9a5b5
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
