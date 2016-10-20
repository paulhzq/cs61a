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
          f86124ac9392b60456505ccefe002925
          # locked
          >>> restaurant_mean_rating(woz) # should be a decimal
          257cc2ef9c54a5c0d4f0eeff0b7f7309
          # locked
          """,
          'hidden': False,
          'locked': True
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
