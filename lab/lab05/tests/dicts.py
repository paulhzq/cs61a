test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> letters = {'a': 1, 'b': 2, 'c': 3}
          >>> 'a' in letters
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> 2 in letters
          ac667055c8e3c84ad7260b0fefa2e007
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
          >>> food = {'bulgogi': 10, 'falafel': 4, 'ceviche': 7}
          >>> food['ultimate'] = food['bulgogi'] + food['ceviche']
          >>> food['ultimate']
          6c4c5c2026b2b916aff21d836960bbd9
          # locked
          >>> len(food)
          fef77a143fa87e746554afe9ebb16a3d
          # locked
          >>> food['ultimate'] += food['falafel']
          >>> food['ultimate']
          286a63c09649ab2e465e9e1abab82eba
          # locked
          >>> sorted(list(food.keys())) # sorted takes in a list and returns a new sorted list
          5c80b6b1619d37b4afb811e76ebc2c56
          # locked
          >>> food['bulgogi'] = food['falafel']
          >>> len(food)
          fef77a143fa87e746554afe9ebb16a3d
          # locked
          >>> 'gogi' in food
          ac667055c8e3c84ad7260b0fefa2e007
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
