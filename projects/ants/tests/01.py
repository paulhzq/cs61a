test = {
  'name': 'Problem 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> HarvesterAnt.food_cost
          20d533d3e06345c8bd7072212867f2d1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ThrowerAnt.food_cost
          81a7d27d1a4a958871bb97b545b871db
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing HarvesterAnt action
          >>> colony.food = 4
          >>> HarvesterAnt().action(colony)
          >>> colony.food
          62674984f877ec783f37e8b8b9c264d0
          # locked
          >>> HarvesterAnt().action(colony)
          >>> colony.food
          50ae32be3e31df6c59633df7fdfb3a72
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
