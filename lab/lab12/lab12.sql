.read sp16data.sql
.read fa16data.sql

CREATE TABLE obedience AS
  select seven,denero from students;

CREATE TABLE smallest_int AS
  select time,smallest from students
  where smallest>8 order by smallest limit 20;

CREATE TABLE greatstudents AS
  select s.date,s.number,s.pet,f.color,s.color
  from sp16students as s, students as f
  where s.date=f.date and s.number=f.number and s.pet = f.pet;

CREATE TABLE sevens AS
  select s.seven from students as s, checkboxes as c
  where s.number = 7 and c.'7'='True' and s.time = c.time;

CREATE TABLE matchmaker AS
  select a.pet,a.song,a.color,b.color
  from students as a, students as b
  where a.pet =b.pet and a.song =b.song and a.time<b.time;
