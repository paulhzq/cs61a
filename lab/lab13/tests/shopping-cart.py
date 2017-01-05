test = {
  'name': 'shopping-cart',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM shopping_cart LIMIT 15;
          CAKE!|0
          cornbread, cornbread, cornbread, cornbread, cornbread|0
          cranberries, cranberries, cranberries, cornbread, cornbread, pumpkin pie|0
          cranberries, cranberries, cranberries, cranberries, cornbread, tofurky|0
          cranberries, cranberries, cranberries, cranberries, cranberries, potatoes, pumpkin pie|0
          cranberries, cranberries, cranberries, cranberries, potatoes, potatoes, cornbread|0
          cranberries, cranberries, potatoes, cornbread, cornbread, cornbread|0
          potatoes, potatoes, potatoes, potatoes, potatoes, potatoes|0
          potatoes, potatoes, potatoes, potatoes, tofurky|0
          potatoes, potatoes, potatoes, pumpkin pie, pumpkin pie|0
          potatoes, potatoes, potatoes, turkey|0
          potatoes, potatoes, tofurky, tofurky|0
          potatoes, pumpkin pie, pumpkin pie, tofurky|0
          potatoes, tofurky, turkey|0
          pumpkin pie, pumpkin pie, pumpkin pie, pumpkin pie|0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          sqlite> SELECT * FROM shopping_cart;
          CAKE!|0
          cornbread, cornbread, cornbread, cornbread, cornbread|0
          cranberries, cranberries, cranberries, cornbread, cornbread, pumpkin pie|0
          cranberries, cranberries, cranberries, cranberries, cornbread, tofurky|0
          cranberries, cranberries, cranberries, cranberries, cranberries, potatoes, pumpkin pie|0
          cranberries, cranberries, cranberries, cranberries, potatoes, potatoes, cornbread|0
          cranberries, cranberries, potatoes, cornbread, cornbread, cornbread|0
          potatoes, potatoes, potatoes, potatoes, potatoes, potatoes|0
          potatoes, potatoes, potatoes, potatoes, tofurky|0
          potatoes, potatoes, potatoes, pumpkin pie, pumpkin pie|0
          potatoes, potatoes, potatoes, turkey|0
          potatoes, potatoes, tofurky, tofurky|0
          potatoes, pumpkin pie, pumpkin pie, tofurky|0
          potatoes, tofurky, turkey|0
          pumpkin pie, pumpkin pie, pumpkin pie, pumpkin pie|0
          pumpkin pie, pumpkin pie, turkey|0
          tofurky, tofurky, tofurky|0
          turkey, turkey|0
          cornbread, cornbread, pumpkin pie, tofurky|1
          cranberries, cornbread, tofurky, tofurky|1
          cranberries, cranberries, cranberries, cranberries, cranberries, cornbread, cornbread|1
          cranberries, cranberries, cranberries, cranberries, cranberries, cranberries, cranberries, potatoes|1
          cranberries, cranberries, potatoes, potatoes, potatoes, pumpkin pie|1
          cranberries, cranberries, potatoes, pumpkin pie, tofurky|1
          cranberries, cranberries, pumpkin pie, pumpkin pie, pumpkin pie|1
          cranberries, cranberries, pumpkin pie, turkey|1
          cranberries, potatoes, cornbread, pumpkin pie, pumpkin pie|1
          cranberries, potatoes, cornbread, turkey|1
          cranberries, potatoes, potatoes, cornbread, tofurky|1
          cranberries, potatoes, potatoes, potatoes, potatoes, cornbread|1
          potatoes, potatoes, cornbread, cornbread, pumpkin pie|1
          cranberries, cornbread, cornbread, cornbread, pumpkin pie|2
          cranberries, cranberries, cornbread, cornbread, tofurky|2
          cranberries, cranberries, cranberries, cranberries, potatoes, potatoes, potatoes|2
          cranberries, cranberries, cranberries, cranberries, potatoes, tofurky|2
          cranberries, cranberries, cranberries, cranberries, pumpkin pie, pumpkin pie|2
          cranberries, cranberries, cranberries, cranberries, turkey|2
          cranberries, cranberries, cranberries, potatoes, cornbread, pumpkin pie|2
          cranberries, cranberries, potatoes, potatoes, cornbread, cornbread|2
          potatoes, cornbread, cornbread, cornbread, cornbread|2
          cornbread, pumpkin pie, pumpkin pie, pumpkin pie|3
          cornbread, pumpkin pie, turkey|3
          cranberries, cranberries, cranberries, cornbread, cornbread, cornbread|3
          cranberries, cranberries, cranberries, cranberries, cranberries, cranberries, pumpkin pie|3
          cranberries, cranberries, cranberries, cranberries, cranberries, potatoes, cornbread|3
          cranberries, potatoes, potatoes, potatoes, potatoes, potatoes|3
          cranberries, potatoes, potatoes, potatoes, tofurky|3
          cranberries, potatoes, potatoes, pumpkin pie, pumpkin pie|3
          cranberries, potatoes, potatoes, turkey|3
          cranberries, potatoes, tofurky, tofurky|3
          cranberries, pumpkin pie, pumpkin pie, tofurky|3
          cranberries, tofurky, turkey|3
          potatoes, cornbread, pumpkin pie, tofurky|3
          potatoes, potatoes, potatoes, cornbread, pumpkin pie|3
          cornbread, cornbread, cornbread, tofurky|4
          cranberries, cranberries, cornbread, pumpkin pie, pumpkin pie|4
          cranberries, cranberries, cornbread, turkey|4
          cranberries, cranberries, cranberries, cranberries, cranberries, cranberries, cranberries, cranberries|4
          cranberries, cranberries, cranberries, potatoes, potatoes, pumpkin pie|4
          cranberries, cranberries, cranberries, pumpkin pie, tofurky|4
          cranberries, cranberries, potatoes, cornbread, tofurky|4
          cranberries, cranberries, potatoes, potatoes, potatoes, cornbread|4
          cranberries, potatoes, cornbread, cornbread, pumpkin pie|4
          potatoes, potatoes, cornbread, cornbread, cornbread|4
          cranberries, cornbread, cornbread, cornbread, cornbread|5
          cranberries, cranberries, cranberries, cranberries, cornbread, pumpkin pie|5
          cranberries, cranberries, cranberries, cranberries, cranberries, potatoes, potatoes|5
          cranberries, cranberries, cranberries, cranberries, cranberries, tofurky|5
          cranberries, cranberries, cranberries, potatoes, cornbread, cornbread|5
          potatoes, potatoes, potatoes, potatoes, pumpkin pie|5
          potatoes, potatoes, pumpkin pie, tofurky|5
          potatoes, pumpkin pie, pumpkin pie, pumpkin pie|5
          potatoes, pumpkin pie, turkey|5
          pumpkin pie, tofurky, tofurky|5
          cornbread, cornbread, pumpkin pie, pumpkin pie|6
          cornbread, cornbread, turkey|6
          cranberries, cornbread, pumpkin pie, tofurky|6
          cranberries, cranberries, cranberries, cranberries, cranberries, cranberries, cornbread|6
          cranberries, cranberries, potatoes, potatoes, potatoes, potatoes|6
          cranberries, cranberries, potatoes, potatoes, tofurky|6
          cranberries, cranberries, potatoes, pumpkin pie, pumpkin pie|6
          cranberries, cranberries, potatoes, turkey|6
          cranberries, cranberries, tofurky, tofurky|6
          cranberries, potatoes, potatoes, cornbread, pumpkin pie|6
          potatoes, cornbread, cornbread, tofurky|6
          potatoes, potatoes, potatoes, cornbread, cornbread|6
          cranberries, cranberries, cornbread, cornbread, pumpkin pie|7
          cranberries, cranberries, cranberries, cornbread, tofurky|7
          cranberries, cranberries, cranberries, cranberries, potatoes, pumpkin pie|7
          cranberries, cranberries, cranberries, potatoes, potatoes, cornbread|7
          cranberries, potatoes, cornbread, cornbread, cornbread|7
          cornbread, tofurky, tofurky|8
          cranberries, cranberries, cranberries, cranberries, cornbread, cornbread|8
          cranberries, cranberries, cranberries, cranberries, cranberries, cranberries, potatoes|8
          cranberries, potatoes, potatoes, potatoes, pumpkin pie|8
          cranberries, potatoes, pumpkin pie, tofurky|8
          cranberries, pumpkin pie, pumpkin pie, pumpkin pie|8
          cranberries, pumpkin pie, turkey|8
          potatoes, cornbread, pumpkin pie, pumpkin pie|8
          potatoes, cornbread, turkey|8
          potatoes, potatoes, cornbread, tofurky|8
          potatoes, potatoes, potatoes, potatoes, cornbread|8
          cornbread, cornbread, cornbread, pumpkin pie|9
          cranberries, cornbread, cornbread, tofurky|9
          cranberries, cranberries, cranberries, potatoes, potatoes, potatoes|9
          cranberries, cranberries, cranberries, potatoes, tofurky|9
          cranberries, cranberries, cranberries, pumpkin pie, pumpkin pie|9
          cranberries, cranberries, cranberries, turkey|9
          cranberries, cranberries, potatoes, cornbread, pumpkin pie|9
          cranberries, potatoes, potatoes, cornbread, cornbread|9
          cranberries, cranberries, cornbread, cornbread, cornbread|10
          cranberries, cranberries, cranberries, cranberries, cranberries, pumpkin pie|10
          cranberries, cranberries, cranberries, cranberries, potatoes, cornbread|10
          potatoes, potatoes, potatoes, potatoes, potatoes|10
          potatoes, potatoes, potatoes, tofurky|10
          potatoes, potatoes, pumpkin pie, pumpkin pie|10
          potatoes, potatoes, turkey|10
          potatoes, tofurky, tofurky|10
          pumpkin pie, pumpkin pie, tofurky|10
          tofurky, turkey|10
          cranberries, cornbread, pumpkin pie, pumpkin pie|11
          cranberries, cornbread, turkey|11
          cranberries, cranberries, cranberries, cranberries, cranberries, cranberries, cranberries|11
          cranberries, cranberries, potatoes, potatoes, pumpkin pie|11
          cranberries, cranberries, pumpkin pie, tofurky|11
          cranberries, potatoes, cornbread, tofurky|11
          cranberries, potatoes, potatoes, potatoes, cornbread|11
          potatoes, cornbread, cornbread, pumpkin pie|11
          cornbread, cornbread, cornbread, cornbread|12
          cranberries, cranberries, cranberries, cornbread, pumpkin pie|12
          cranberries, cranberries, cranberries, cranberries, potatoes, potatoes|12
          cranberries, cranberries, cranberries, cranberries, tofurky|12
          cranberries, cranberries, potatoes, cornbread, cornbread|12
          cornbread, pumpkin pie, tofurky|13
          cranberries, cranberries, cranberries, cranberries, cranberries, cornbread|13
          cranberries, potatoes, potatoes, potatoes, potatoes|13
          cranberries, potatoes, potatoes, tofurky|13
          cranberries, potatoes, pumpkin pie, pumpkin pie|13
          cranberries, potatoes, turkey|13
          cranberries, tofurky, tofurky|13
          potatoes, potatoes, cornbread, pumpkin pie|13
          cranberries, cornbread, cornbread, pumpkin pie|14
          cranberries, cranberries, cornbread, tofurky|14
          cranberries, cranberries, cranberries, potatoes, pumpkin pie|14
          cranberries, cranberries, potatoes, potatoes, cornbread|14
          potatoes, cornbread, cornbread, cornbread|14
          cranberries, cranberries, cranberries, cornbread, cornbread|15
          cranberries, cranberries, cranberries, cranberries, cranberries, potatoes|15
          potatoes, potatoes, potatoes, pumpkin pie|15
          potatoes, pumpkin pie, tofurky|15
          pumpkin pie, pumpkin pie, pumpkin pie|15
          pumpkin pie, turkey|15
          cornbread, cornbread, tofurky|16
          cranberries, cranberries, potatoes, potatoes, potatoes|16
          cranberries, cranberries, potatoes, tofurky|16
          cranberries, cranberries, pumpkin pie, pumpkin pie|16
          cranberries, cranberries, turkey|16
          cranberries, potatoes, cornbread, pumpkin pie|16
          potatoes, potatoes, cornbread, cornbread|16
          cranberries, cornbread, cornbread, cornbread|17
          cranberries, cranberries, cranberries, cranberries, pumpkin pie|17
          cranberries, cranberries, cranberries, potatoes, cornbread|17
          cornbread, pumpkin pie, pumpkin pie|18
          cornbread, turkey|18
          cranberries, cranberries, cranberries, cranberries, cranberries, cranberries|18
          cranberries, potatoes, potatoes, pumpkin pie|18
          cranberries, pumpkin pie, tofurky|18
          potatoes, cornbread, tofurky|18
          potatoes, potatoes, potatoes, cornbread|18
          cranberries, cranberries, cornbread, pumpkin pie|19
          cranberries, cranberries, cranberries, potatoes, potatoes|19
          cranberries, cranberries, cranberries, tofurky|19
          cranberries, potatoes, cornbread, cornbread|19
          cranberries, cranberries, cranberries, cranberries, cornbread|20
          potatoes, potatoes, potatoes, potatoes|20
          potatoes, potatoes, tofurky|20
          potatoes, pumpkin pie, pumpkin pie|20
          potatoes, turkey|20
          tofurky, tofurky|20
          cornbread, cornbread, pumpkin pie|21
          cranberries, cornbread, tofurky|21
          cranberries, cranberries, potatoes, pumpkin pie|21
          cranberries, potatoes, potatoes, cornbread|21
          cranberries, cranberries, cornbread, cornbread|22
          cranberries, cranberries, cranberries, cranberries, potatoes|22
          cranberries, potatoes, potatoes, potatoes|23
          cranberries, potatoes, tofurky|23
          cranberries, pumpkin pie, pumpkin pie|23
          cranberries, turkey|23
          potatoes, cornbread, pumpkin pie|23
          cornbread, cornbread, cornbread|24
          cranberries, cranberries, cranberries, pumpkin pie|24
          cranberries, cranberries, potatoes, cornbread|24
          cranberries, cranberries, cranberries, cranberries, cranberries|25
          potatoes, potatoes, pumpkin pie|25
          pumpkin pie, tofurky|25
          cranberries, cornbread, pumpkin pie|26
          cranberries, cranberries, potatoes, potatoes|26
          cranberries, cranberries, tofurky|26
          potatoes, cornbread, cornbread|26
          cranberries, cranberries, cranberries, cornbread|27
          cornbread, tofurky|28
          cranberries, potatoes, pumpkin pie|28
          potatoes, potatoes, cornbread|28
          cranberries, cornbread, cornbread|29
          cranberries, cranberries, cranberries, potatoes|29
          potatoes, potatoes, potatoes|30
          potatoes, tofurky|30
          pumpkin pie, pumpkin pie|30
          turkey|30
          cranberries, cranberries, pumpkin pie|31
          cranberries, potatoes, cornbread|31
          cranberries, cranberries, cranberries, cranberries|32
          cornbread, pumpkin pie|33
          cranberries, potatoes, potatoes|33
          cranberries, tofurky|33
          cranberries, cranberries, cornbread|34
          potatoes, pumpkin pie|35
          cornbread, cornbread|36
          cranberries, cranberries, potatoes|36
          cranberries, pumpkin pie|38
          potatoes, cornbread|38
          cranberries, cranberries, cranberries|39
          potatoes, potatoes|40
          tofurky|40
          cranberries, cornbread|41
          cranberries, potatoes|43
          pumpkin pie|45
          cranberries, cranberries|46
          cornbread|48
          potatoes|50
          cranberries|53
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
