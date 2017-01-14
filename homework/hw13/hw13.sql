create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select d.name,s.size 
  from dogs as d,sizes as s
  where d.height>s.min and d.height<=s.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select d.name from dogs as d, parents as p,dogs as do
  where d.name = p.child and p.parent = do.name
  order by do.height DESC ;

-- Sentences about siblings that are the same size
create table sentences as
  with 
    chart(name,parent,size) as (
      select p.child,p.parent,s.size from dogs as d,parents as p,size_of_dogs as s 
      where d.name = p.child and d.name = s.name order by s.size
      )

  select  c1.name ||' and '|| c2.name || ' are '|| c1.size || ' siblings'   
  from chart as c1,chart as c2
  where c1.parent = c2.parent and c1.name < c2.name and c1.size =c2.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with 
   totalheight(name1,name2,name3,name4,heights) as (
    select d1.name,d2.name,d3.name,d4.name,d1.height+d2.height+d3.height+d4.height as total
    FROM dogs as d1,dogs as d2,dogs as d3,dogs as d4
    where total >=170 and d1.height<d2.height and d2.height<d3.height and d3.height<d4.height 
    )
  select (t.name1||', '||t.name2||', '||t.name3||', '||t.name4) as names,heights
  from totalheight as t
  order by heights asc;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
  with chart(x, y, z) as (
    select a.n, b.n, a.n * b.n from ints as a, ints as b where a.n * b.n <= 100
  )
  select c.z as n, count(*) as k from chart as c group by c.z
;

create table primes as
    select d.n 
    from divisors as d
    where d.k =2 and d.n<=100;
