test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow 4 0)
          d912fc844d1dbaeea8a84b3ec8b315bc
          # locked
          scm> (pow 10 3)
          fe27c17af307754d3da2376333aace6d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 2 3)
          705c779aa26cefdacfc628f4e6fe0545
          # locked
          scm> (pow 2 5)
          848e0b69eef6e431bcbe9697b14733ac
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 3 3)
          20003cf15af46c423e717569612a6d51
          # locked
          scm> (pow 3 4)
          a04e586c190828f8df786d889a13d9c8
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
