.read lab12.sql

CREATE TABLE sp16favnum AS
  select number,COUNT(*) as count from sp16students group by number
  order by count desc limit 1;


CREATE TABLE sp16favpets AS
  select pet,COUNT(*) as count from sp16students group by pet
  order by count desc limit 10;


CREATE TABLE fa16favpets AS
  select pet,COUNT(*) as count from students group by pet
  order by count desc limit 10;


CREATE TABLE fa16dragon AS
  select s.pet,COUNT(*) from students as s 
  where s.pet = "dragon"
  ;


CREATE TABLE fa16alldragons AS
  select pet,COUNT(*) from students
  where pet like '%dragon%';


CREATE TABLE obedienceimage AS
  select seven,denero,COUNT(*) from obedience
  where seven = '7'
  GROUP BY denero;

CREATE TABLE smallest_int_count AS
  select smallest,COUNT(*)
  from students 
  where smallest >=1
  group by smallest 
  ;
