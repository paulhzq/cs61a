.read data.sql

-- Q1
create table flight_costs as
  with chart(day, curr, prev) as (
    select 1, 20, 0 union
    select 2, 30, 20 union
    select 3, 40, 30 union
    select day + 1, (curr +  prev)/2 + 5 * ((day+1)%7), curr from chart where day < 25 and day > 2
  )
  select day as day, curr as price from chart;

-- Q2
create table schedule as
  with trips(path, ending, flights, cost) as(
    select departure || ", " || arrival, arrival, 1, price from flights where departure = "SFO" union
    select path || ", " || arrival, arrival, flights + 1, cost + price from trips, flights where ending = departure and flights < 2
    )
  select path, cost from trips where ending = "PDX" order by cost;

-- Q3
create table shopping_cart as
  with cart(items, last, budget) as (
    select item, price, 60 - price from supermarket where price <= 60 union
    select items || ", " || item, price, budget - price from cart, supermarket where price <= budget and price >= last
  )
  select items, budget as left from cart order by left, items;

-- Q4
create table number_of_options as
  select count(distinct meat) from main_course;

-- Q5
create table calories as
  select count(*) from main_course as m, pies as p where (m.calories + p.calories) < 2500;

-- Q6
create table healthiest_meats as
  select m.meat, min(m.calories + p.calories) as cal from main_course as m, pies as p group by m.meat having max(m.calories + p.calories) < 3000;

-- Q7
create table average_prices as
  select category, avg(MSRP) from products group by category;

-- Q8
create table lowest_prices as
  select p.name as name, i.store as store, i.price as price from products as p, inventory as i where p.name = i.item group by p.name having min(i.price);

-- Q9
create table shopping_list as
  select l.name, l.store as store from lowest_prices as l, products as p where p.name = l.name group by p.category having min(p.MSRP / p.rating);

-- Q10
create table total_bandwidth as
  select sum(Mbs) from shopping_list as a, stores as b where a.store = b.store;