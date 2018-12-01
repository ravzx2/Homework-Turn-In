use sakila;

#1a
SELECT first_name, last_name
FROM actor;

#1b
alter table actor
add column Actor_Name varchar(100);
UPDATE actor SET Actor_Name = CONCAT(first_name, " ", last_name);
select Actor_name from actor;

#2a
select actor_id, first_name, last_name from actor where first_name='Joe';

#2b
select * from actor where last_name like '%gen%';

#2c
select * from actor where last_name like '%li%'
order by last_name, first_name;

#2d
SELECT * FROM country WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

#3a
alter table actor
add column description blob;

#3b
alter table actor drop column description;

#4a
SELECT last_name, count(*)
FROM actor
GROUP BY last_name;

#4b
SELECT last_name, COUNT(*) AS cnt
FROM actor
GROUP BY last_name
HAVING cnt > 1;

#4c
UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO' AND last_name = 'WILLIAMS';

#4d
update actor
set first_name = 'GROUCHO'
WHERE first_name = 'HARPO' AND last_name = 'WILLIAMS';

#5a
show create table address;

#6a
select staff.first_name, staff.last_name, address.address
from staff
join address on
staff.address_id=address.address_id;

#6b
SELECT staff.staff_id, first_name, last_name, SUM(amount) as "Total Amount Rung Up"
FROM staff
INNER JOIN payment 
ON staff.staff_id = payment.staff_id
GROUP BY staff.staff_id;

#6c
Select film.title, COUNT(film_actor.actor_id) as "Number of Actors"
FROM film
INNER JOIN film_actor
ON film.film_id = film_actor.film_id
GROUP BY film.film_id;

#6d
SELECT film.title, COUNT(inventory.inventory_id) as "Number in Inventory"
FROM film
INNER JOIN inventory
ON film.film_id = inventory.film_id
GROUP BY film.film_id
HAVING title = "Hunchback Impossible";

#6e
select customer.first_name, customer.last_name, sum(payment.amount) as "Total Amount Paid"
from customer
join payment on
customer.customer_id=payment.customer_id
group by customer.customer_id
order by customer.last_name;

#7a
SELECT title FROM film
WHERE language_id IN
	(SELECT language_id FROM language
	WHERE name = "English")
AND (title LIKE "K%") OR (title LIKE "Q%");

#7b
SELECT first_name, last_name FROM actor
WHERE actor_id IN
	(SELECT actor_id FROM film_actor
	WHERE film_id IN
		(SELECT film_id FROM film
		WHERE title = "Alone Trip"));

#7c
SELECT customer.first_name, customer.last_name, customer.email, country.country
FROM customer
LEFT JOIN address
ON customer.address_id = address.address_id
LEFT JOIN city
ON city.city_id = address.city_id
LEFT JOIN country
ON country.country_id = city.country_id
WHERE country = "Canada";

#7d
SELECT title from film
WHERE film_id IN
	(SELECT film_id FROM film_category
	WHERE category_id IN
		(SELECT category_id FROM category
		WHERE name = "Family"));
        
#7e
SELECT film.title , COUNT(rental.rental_id) AS "Number of Rentals"
FROM film
RIGHT JOIN inventory
ON film.film_id = inventory.film_id
JOIN rental 
ON rental.inventory_id = inventory.inventory_id
GROUP BY film.title
ORDER BY COUNT(rental.rental_id) DESC;

#7f
SELECT store.store_id, sum(amount) as "Revenue"
FROM store
RIGHT JOIN staff
ON store.store_id = staff.store_id
LEFT JOIN payment
ON staff.staff_id = payment.staff_id
GROUP BY store.store_id;

#7g
SELECT store.store_id, city.city, country.country
FROM store
JOIN address
ON store.address_id = address.address_id
JOIN city
ON address.city_id = city.city_id
JOIN country
ON city.country_id = country.country_id;

#7h
SELECT category.name, sum(payment.amount) as "Revenue per Category"
FROM category
JOIN film_category
ON category.category_id = film_category.category_id
JOIN inventory
ON film_category.film_id = inventory.film_id
JOIN rental
ON rental.inventory_id = inventory.inventory_id
JOIN payment
ON payment.rental_id = rental.rental_id
GROUP BY name;

#8a
CREATE VIEW top_5_by_genre AS
SELECT category.name, sum(payment.amount) as "Revenue per Category"
FROM category
JOIN film_category
ON category.category_id = film_category.category_id
JOIN inventory
ON film_category.film_id = inventory.film_id
JOIN rental
ON rental.inventory_id = inventory.inventory_id
JOIN payment
ON payment.rental_id = rental.rental_id
GROUP BY name
ORDER BY SUM(payment.amount) DESC
LIMIT 5;

#8b
SELECT * FROM top_5_by_genre;

#8c
DROP VIEW top_5_by_genre;
