create table flights as
  select "SFO" as departure, "LAX" as arrival, 97 as price union
  select "SFO"             , "AUH"           , 848         union
  select "LAX"             , "SLC"           , 115         union
  select "SFO"             , "PDX"           , 192         union
  select "AUH"             , "SEA"           , 932         union
  select "SLC"             , "PDX"           , 79          union
  select "SFO"             , "LAS"           , 40          union
  select "SLC"             , "LAX"           , 117         union
  select "SEA"             , "PDX"           , 32          union
  select "SLC"             , "SEA"           , 42          union
  select "SFO"             , "SLC"           , 97          union
  select "LAS"             , "SLC"           , 50          union
  select "LAX"             , "PDX"           , 89               ;

create table supermarket as
  select "turkey" as item, 30 as price union
  select "tofurky"       , 20          union
  select "cornbread"     , 12          union
  select "potatoes"      , 10          union
  select "cranberries"   , 7           union
  select "pumpkin pie"   , 15          union
  select "CAKE!"         , 60          union
  select "foie gras"     , 70               ;

create table main_course as
  select "turkey" as meat, "cranberries" as side, 2000 as calories union
  select "turducken"     , "potatoes"           , 4000             union
  select "tofurky"       , "cranberries"        , 1000             union
  select "tofurky"       , "stuffing"           , 1000             union
  select "tofurky"       , "yams"               , 1000             union
  select "turducken"     , "turducken"          , 9000             union
  select "turkey"        , "potatoes"           , 2000             union
  select "turkey"        , "bread"              , 1500             union
  select "tofurky"       , "soup"               , 1200             union
  select "chicken"       , "cranberries"        , 2500             union
  select "turducken"     , "butter"             , 10000            union
  select "turducken"     , "more_butter"        , 15000                 ;

create table pies as
  select "pumpkin" as pie, 500 as calories union
  select "apple"         , 400             union
  select "chocolate"     , 600             union
  select "cherry"        , 550                  ;

create table products as
  select "phone" as category, "uPhone" as name, 99.99 as MSRP, 4.5 as rating union
  select "phone"            , "rPhone"        , 79.99        , 3             union
  select "phone"            , "qPhone"        , 89.99        , 4             union
  select "games"            , "GameStation"   , 299.99       , 3             union
  select "games"            , "QBox"          , 399.99       , 3.5           union
  select "computer"         , "iBook"         , 112.99       , 4             union
  select "computer"         , "wBook"         , 114.29       , 4.4           union
  select "computer"         , "kBook"         , 99.99        , 3.8                ;

create table inventory as
  select "Hallmart" as store, "uPhone" as item, 99.99 as price union
  select "Targive"          , "uPhone"        , 100.99         union
  select "RestBuy"          , "uPhone"        , 89.99          union

  select "Hallmart"         , "rPhone"        , 69.99          union
  select "Targive"          , "rPhone"        , 79.99          union
  select "RestBuy"          , "rPhone"        , 75.99          union

  select "Hallmart"         , "qPhone"        , 85.99          union
  select "Targive"          , "qPhone"        , 88.98          union
  select "RestBuy"          , "qPhone"        , 87.98          union

  select "Hallmart"         , "GameStation"   , 298.98         union
  select "Targive"          , "GameStation"   , 300.98         union
  select "RestBuy"          , "GameStation"   , 310.99         union

  select "Hallmart"         , "QBox"          , 399.99         union
  select "Targive"          , "QBox"          , 390.98         union
  select "RestBuy"          , "QBox"          , 410.98         union

  select "Hallmart"         , "iBook"         , 111.99         union
  select "Targive"          , "iBook"         , 110.99         union
  select "RestBuy"          , "iBook"         , 112.99         union

  select "Hallmart"         , "wBook"         , 117.29         union
  select "Targive"          , "wBook"         , 119.29         union
  select "RestBuy"          , "wBook"         , 114.29         union

  select "Hallmart"         , "kBook"         , 95.99          union
  select "Targive"          , "kBook"         , 96.99          union
  select "RestBuy"          , "kBook"         , 94.99               ;

create table stores as
  select "Hallmart" as store, "50 Lawton Way" as address, 25 as Mbs union
  select "Targive"          , "2 Red Circle Way"        , 40        union
  select "RestBuy"          , "1 Kiosk Ave"             , 30             ;