test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> woz_reviews = [make_review('Wozniak Lounge', 4),
          ...                make_review('Wozniak Lounge', 3),
          ...                make_review('Wozniak Lounge', 5)]
          >>> woz = make_restaurant('Wozniak Lounge', [127.0, 0.1],
          ...                       ['Restaurants', 'Pizza'],
          ...                       1, woz_reviews)
          >>> restaurant_num_ratings(woz)
          3
          >>> restaurant_mean_rating(woz) # should be a decimal
          4.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import abstractions
      >>> from abstractions import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
