-- Lecture 5 Data extraction
-- 1. list of customers
select * from customers c ;
-- 2. number of different products?
select count(product_id) from products p ;
-- 3. count of employees 
select count(1) from employees e ;
-- 4. total overall revenue
--quantity * unit_price - (quantity * unit_price * discount)
-- more simple -> sum(quantity * unit_price * (1-discount))
select sum(quantity * unit_price * (1- discount)) from order_details od ;
-- 5. total revenue for one specific year
select sum(quantity * unit_price * (1- discount)) from order_details od 
left join orders o on od.order_id = o.order_id
where extract (year from o.order_date ) = '1996';
-- 6. list of countries covered by delivery
select distinct ship_country from orders o ; -- distinct finds unique (no duplicate) values
-- 7. list of available transporters
select * from shippers s ;
-- 8. number of customer per countries
select count(customer_id), country from customers group by country ;
-- 9. number of orders which are "ordered" but not shipped
select count(order_id) from orders o where shipped_date is null  ;
-- 10. all the orders from france and belgium
select * from orders o where ship_country in ('France', 'Belgium');
-- 11. most expensive products
select * from products p order by unit_price desc limit 5;
-- 12. list of discontinued products
select * from products p where discontinued = 1;
-- 13. count of product per category
select count(product_id) , category_id from products p  group by category_id ; -- OR
select count(product_id), c.category_id from products p left join categories c on c.category_id = p.category_id group by c.category_id ;
-- 14. average order price
select avg(unit_price) , order_id from order_details od group by order_id ;
-- 15. revenue per category
select sum(unit_price * units_on_order) , c.category_id from products p 
left join categories c on c.category_id = p.category_id group by c.category_id ;
-- 16. number of orders per shipper
select count(o.ship_via) , s.shipper_id from orders o left join shippers s on s.shipper_id = o.ship_via group by s.shipper_id ;
-- 17. number of orders per employee
select count(o.order_id) , e.employee_id from orders o left join employees e on e.employee_id = o.employee_id group by e.employee_id;
-- 18. total revenue per supplier - 'as' for table heading
select sum(od.quantity * od.unit_price * (1- od.discount)) as total_rev_per_supp, s.supplier_id 
from order_details od 
inner join products p on od.product_id = p.product_id 
inner join suppliers s on p.supplier_id = s.supplier_id 
group by s.supplier_id;
-- 18-b. find the total revenue per region
-- tried region from suppliers table
select sum(od.quantity * od.unit_price * (1- od.discount)) as total_rev_per_supplier_region, s.region from order_details od inner join products p on od.product_id = p.product_id inner join suppliers s on p.supplier_id = s.supplier_id group by s.region  ;
-- tried region from region table
select sum(od.quantity * od.unit_price * (1- od.discount)) as total_rev_per_region, r.region_id, r.region_description from order_details od inner join orders o on o.order_id = od.order_id inner join employees e on e.employee_id = o.employee_id inner join employee_territories et on et.employee_id = e.employee_id inner join territories t on t.territory_id = et.territory_id inner join region r on r.region_id = t.region_id group by r.region_id;
-- tried ship_region from orders table
select sum(od.quantity * od.unit_price * (1- od.discount)) as total_rev_per_ship_region, o.ship_region from order_details od left join orders o on o.order_id = od.order_id group by o.ship_region ; 

-- All of these results give unaccurate values and my guess is that it's because of the NULL values (in the region field) in the table which are not being counted
-- If we change to country instead of region it'll work 

-- get facis which are not free
select * from cd.facilities where membercost > 0;

-- How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.
select facid, name, membercost, monthlymaintenance from cd.facilities
where membercost > 0 and membercost < monthlymaintenance / 50;

-- How can you produce a list of all facilities with the word 'Tennis' in their name?
select * from cd.facilities
where name like '%Tennis%';

-- How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.
select * from cd.facilities
where facid in (1, 5);

-- How can you produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.
select name,
  case when (monthlymaintenance > 100) then 
  	'expensive'
  else 
  	'cheap'
  end as cost
  from cd.facilities;

-- How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, firstname, and joindate of the members in question.
select memid, surname, firstname, joindate from cd.members
where (joindate > '2012-09-01 00:00:00')

-- How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
select distinct surname from cd.members
order by surname
limit 10

-- You, for some reason, want a combined list of all surnames and all facility names. Yes, this is a contrived example :-). Produce that list!
select surname from cd.members
union
select name from cd.facilities

-- You'd like to get the signup date of your last member. How can you retrieve this information?
select max(joindate) as latest from cd.members

-- You'd like to get the first and last name of the last member(s) who signed up - not just the date. How can you do that?
select firstname, surname, joindate from cd.members
order by joindate desc
limit 1

