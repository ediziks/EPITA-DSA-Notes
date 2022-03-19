-- Lecture 5 Data extraction
-- 1. list of customers
select *
from customers c;

-- 2. number of different products?
select count(product_id)
from products p;

-- 3. count of employees 
select count(1)
from employees e;

-- 4. total overall revenue
--quantity * unit_price - (quantity * unit_price * discount)
-- more simple->sum(quantity * unit_price * (1 - discount))
select sum(quantity * unit_price * (1 - discount))
from order_details od;

-- 5. total revenue for one specific year
select sum(quantity * unit_price * (1 - discount))
from order_details od
  left join orders o on od.order_id = o.order_id
where extract (
    year
    from o.order_date
  ) = '1996';

-- 6. list of countries covered by delivery
select distinct ship_country
from orders o;

-- distinct finds unique (no duplicate) values
-- 7. list of available transporters
select *
from shippers s;

-- 8. number of customer per countries
select count(customer_id),
  country
from customers
group by country;

-- 9. number of orders which are "ordered" but not shipped
select count(order_id)
from orders o
where shipped_date is null;

-- 10. all the orders from france and belgium
select *
from orders o
where ship_country in ('France', 'Belgium');

-- 11. most expensive products
select *
from products p
order by unit_price desc
limit 5;

-- 12. list of discontinued products
select *
from products p
where discontinued = 1;

-- 13. count of product per category
select count(product_id),
  category_id
from products p
group by category_id;
-- OR
select count(product_id),
  c.category_id
from products p
  left join categories c on c.category_id = p.category_id
group by c.category_id;

-- 14. average order price
select avg(unit_price),
  order_id
from order_details od
group by order_id;

-- 15. revenue per category
select sum(unit_price * units_on_order),
  c.category_id
from products p
  left join categories c on c.category_id = p.category_id
group by c.category_id;

-- 16. number of orders per shipper
select count(o.ship_via),
  s.shipper_id
from orders o
  left join shippers s on s.shipper_id = o.ship_via
group by s.shipper_id;

-- 17. number of orders per employee
select count(o.order_id),
  e.employee_id
from orders o
  left join employees e on e.employee_id = o.employee_id
group by e.employee_id;

-- 18. total revenue per supplier - 'as' for table heading
select sum(od.quantity * od.unit_price * (1 - od.discount)) as total_rev_per_supp,
  s.supplier_id
from order_details od
  inner join products p on od.product_id = p.product_id
  inner join suppliers s on p.supplier_id = s.supplier_id
group by s.supplier_id;

-- 18-b. find the total revenue per region
-- tried region from suppliers table
select sum(od.quantity * od.unit_price * (1 - od.discount)) as total_rev_per_supplier_region,
  s.region
from order_details od
  inner join products p on od.product_id = p.product_id
  inner join suppliers s on p.supplier_id = s.supplier_id
group by s.region;

-- tried region from region table
select sum(od.quantity * od.unit_price * (1 - od.discount)) as total_rev_per_region,
  r.region_id,
  r.region_description
from order_details od
  inner join orders o on o.order_id = od.order_id
  inner join employees e on e.employee_id = o.employee_id
  inner join employee_territories et on et.employee_id = e.employee_id
  inner join territories t on t.territory_id = et.territory_id
  inner join region r on r.region_id = t.region_id
group by r.region_id;

-- tried ship_region from orders table
select sum(od.quantity * od.unit_price * (1 - od.discount)) as total_rev_per_ship_region,
  o.ship_region
from order_details od
  left join orders o on o.order_id = od.order_id
group by o.ship_region;
-- All of these results give unaccurate values and my guess is that it's because of the NULL values (in the region field) in the table which are not being counted
-- If we change to country instead of region it'll work 

-- PG EXERCISES
-- link to db pic -> https://pgexercises.com/img/schema-horizontal.svg 
-- get facis which are not free
select *
from cd.facilities
where membercost > 0;

-- How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.
select facid,
  name,
  membercost,
  monthlymaintenance
from cd.facilities
where membercost > 0
  and membercost < monthlymaintenance / 50;

-- How can you produce a list of all facilities with the word 'Tennis' in their name?
select *
from cd.facilities
where name like '%Tennis%';

-- How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.
select *
from cd.facilities
where facid in (1, 5);

-- How can you produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.
select name,
  case
    when (monthlymaintenance > 100) then 'expensive'
    else 'cheap'
  end as cost
from cd.facilities;

-- How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, firstname, and joindate of the members in question.
select memid,
  surname,
  firstname,
  joindate
from cd.members
where (joindate > '2012-09-01 00:00:00'); 

-- How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
select distinct surname
from cd.members
order by surname
limit 10;

-- You, for some reason, want a combined list of all surnames and all facility names. Yes, this is a contrived example :-). Produce that list!
select surname
from cd.members
union
select name
from cd.facilities;

 -- You'd like to get the signup date of your last member. How can you retrieve this information?
select max(joindate) as latest
from cd.members 

-- You'd like to get the first and last name of the last member(s) who signed up - not just the date. How can you do that?
select firstname,
  surname,
  joindate
from cd.members
order by joindate desc
limit 1;

-- How can you produce a list of the start times for bookings by members named 'David Farrell'? -- FKs joined within 2 tables
select bks.starttime
from cd.bookings bks
  inner join cd.members mems on mems.memid = bks.memid
where mems.firstname = 'David'
  and mems.surname = 'Farrell';

-- How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.
select bks.starttime as start,
  fct.name as name
from cd.bookings bks
  inner join cd.facilities fct on fct.facid = bks.facid
where bks.starttime > ('2012-09-21')
  and bks.starttime < ('2012-09-22')
  and fct.name like ('%Tennis Court%');

-- How can you output a list of all members who have recommended another member? Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname).
select distinct recs.firstname,
  recs.surname
from cd.members mem
  inner join cd.members recs on recs.memid = mem.recommendedby
order by surname, firstname;

-- left outer join -> returns all records from the left table (table1), and the matching records from the right table (table2);
-- How can you output a list of all members, including the individual who recommended them (if any)? Ensure that results are ordered by (surname, firstname).
select mem.firstname as memfname,
  mem.surname as memsname,
  fct.firstname as recfname,
  fct.surname as recsname
from cd.members mem
  left outer join cd.members fct on mem.recommendedby = fct.memid
order by memsname, memfname;

-- 2 FK join
-- How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name followed by the facility name
select distinct mem.firstname || ' ' || mem.surname as member,
  fct.name as facility
from cd.members mem
  inner join cd.bookings bks on mem.memid = bks.memid
  left outer join cd.facilities fct on bks.facid = fct.facid
where fct.name like ('%Tennis Court%')
order by member,
  facility;

-- double inner join
-- How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries.
select mem.firstname || ' ' || mem.surname as member,
  facs.name as facility,
  case
    when mem.memid = 0 then bks.slots * facs.guestcost
    else bks.slots * facs.membercost
  end as cost
from cd.members mem 
-- *
  inner join cd.bookings bks on mem.memid = bks.memid
  inner join cd.facilities facs on bks.facid = facs.facid
where bks.starttime >= '2012-09-14'
  and bks.starttime < '2012-09-15'
  and (
    (
      bks.slots * facs.guestcost > 30
      and mem.memid = 0
    )
    or (
      bks.slots * facs.membercost > 30
      and mem.memid != 0
    )
  )
order by cost desc;

-- Subquery Method
-- How can you output a list of all members, including the individual who recommended them (if any), without using any joins? Ensure that there are no duplicates in the list, and that each firstname + surname pairing is formatted as a column and ordered.
select distinct
	mem.firstname || ' ' || mem.surname as member,
	(select 
		rec.firstname || ' ' || rec.surname as recommender
		
	from 
		cd.members rec
	where
		mem.recommendedby = rec.memid
		or
		mem.recommendedby = null)
from 
	cd.members mem
order by member, recommender;

-- subquery method with inner join (different way for the line 252)
-- How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost.
select 
	member, facility, cost 
from
	(
	  select
	  	mem.firstname || ' ' || mem.surname as member,
	  	fac.name as facility,
	  	case when
	  		mem.memid = 0 
	  	then
	  		bok.slots * fac.guestcost
	  	else
	  		bok.slots * fac.membercost
	  	end as
	  		cost
	  from
	  	cd.members mem
	  inner join
	  	cd.bookings bok
	  	on
	  	mem.memid = bok.memid
	  inner join
	  	cd.facilities fac
	  	on 
	  	bok.facid = fac.facid
	  where 
	  	bok.starttime >= '2012-09-14'
	  	and
	  	bok.starttime < '2012-09-15'
	) as bookings 
where
	cost > 30
order by cost desc;

-- insert values
-- The club is adding a new facility - a spa. We need to add it into the facilities table. Use the following values:
insert into 
	cd.facilities
values
	(9, 'Spa', 20, 30, 100000, 800);

-- insert multiple rows
insert into
	cd.facilities
values
	(9, 'Spa', 20, 30, 100000, 800),
	(10, 'Squash Court 2', 3.5, 17.5, 5000, 80);

-- calculate within insert
insert into
	cd.facilities
values
	(
	  ((select max(facid) from cd.facilities) + 1),
	  'Spa',
	  20,
	  30,
	  100000,
	  800
	);

-- update row
update
	cd.facilities fac
set 
	initialoutlay = 10000
where
	fac.facid = 1;

