use sakila;

-- 1a. Display the first and last names of all actors from the table actor.
SELECT 
    first_name, last_name
FROM
    actor;
    
-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
SELECT 
    UPPER(CONCAT_WS(' ', first_name, last_name)) AS 'Actor Name'
FROM
    actor;
    
-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
-- What is one query would you use to obtain this information?
SELECT 
    actor_id, first_name, last_name
FROM
    actor
WHERE
    first_name = 'Joe';
    
-- 2b. Find all actors whose last name contain the letters GEN:
SELECT 
    first_name, last_name
FROM
    actor
WHERE
    last_name LIKE '%GEN%';
    
-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
SELECT 
    first_name, last_name
FROM
    actor
WHERE
    last_name LIKE '%LI%'
ORDER BY last_name , first_name;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT 
    country_id, country
FROM
    country
WHERE
    country IN ('Afghanistan' , 'Bangladesh', 'China');
    
-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
ALTER TABLE actor add column middle_name varchar(45) after first_name;

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
ALTER TABLE actor modify column middle_name blob;

-- 3c. Now delete the middle_name column.
ALTER TABLE actor drop column middle_name;

-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT 
    last_name, COUNT(*) how_many
FROM
    actor
GROUP BY last_name
ORDER BY 2 DESC;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT 
    last_name, COUNT(*) how_many
FROM
    actor
GROUP BY last_name
HAVING COUNT(*) >= 2
ORDER BY 2 DESC;

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, 
-- the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
UPDATE actor 
SET 
    first_name = 'HARPO'
WHERE
    first_name = 'GROUCHO'
        AND last_name = 'WILLIAMS';
SELECT 
    *
FROM
    actor
WHERE
    actor_id = 172;

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, 
-- if the first name of the actor is currently HARPO, change it to GROUCHO. 
-- Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. 
-- BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)
UPDATE actor 
SET 
    first_name = (CASE
        WHEN first_name = 'HARPO' THEN 'GROUCHO'
        ELSE 'MUCHO GROUCHO'
    END)
WHERE
    actor_id = 172;
                                   
-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
-- Hint: https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html
show create table address;

-- CREATE TABLE `address` (
--     `address_id` SMALLINT(5) UNSIGNED NOT NULL AUTO_INCREMENT,
--     `address` VARCHAR(50) NOT NULL,
--     `address2` VARCHAR(50) DEFAULT NULL,
--     `district` VARCHAR(20) NOT NULL,
--     `city_id` SMALLINT(5) UNSIGNED NOT NULL,
--     `postal_code` VARCHAR(10) DEFAULT NULL,
--     `phone` VARCHAR(20) NOT NULL,
--     `location` GEOMETRY NOT NULL,
--     `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--     PRIMARY KEY (`address_id`),
--     KEY `idx_fk_city_id` (`city_id`),
--     SPATIAL KEY `idx_location` ( `location` ),
--     CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`)
--         REFERENCES `city` (`city_id`)
--         ON UPDATE CASCADE
-- )  ENGINE=INNODB AUTO_INCREMENT=606 DEFAULT CHARSET=UTF8;
 
 

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT 
    s.first_name,
    s.last_name,
    a.address,
    a.address2,
    c.city,
    a.postal_code,
    co.country
FROM
    staff s
        INNER JOIN
    address a ON s.address_id = a.address_id
        INNER JOIN
    city c ON c.city_id = a.city_id
        INNER JOIN
    country co ON co.country_id = c.country_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT 
    s.staff_id,
    s.first_name,
    s.last_name,
    SUM(p.amount) 'total amount rung up'
FROM
    staff s
        INNER JOIN
    payment p ON s.staff_id = p.staff_id
WHERE
    MONTH(p.payment_date) = 8
        AND YEAR(payment_date) = 2005
GROUP BY s.staff_id , s.first_name , s.last_name
;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT 
    *
FROM
    film_actor;
SELECT 
    *
FROM
    film;

SELECT 
    f.title AS 'film', COUNT(*) 'number of actors'
FROM
    film f
        INNER JOIN
    film_actor fa ON f.film_id = fa.film_id
GROUP BY f.title;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT 
    COUNT(*)
FROM
    inventory i
WHERE
    i.film_id IN (SELECT 
            f.film_id
        FROM
            film f
        WHERE
            f.title = 'Hunchback Impossible');

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
-- 	![Total amount paid](Images/total_payment.png)
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(p.amount) 'Total amount paid'
FROM
    customer c
        INNER JOIN
    payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id , c.first_name , c.last_name
ORDER BY c.last_name
;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, 
-- films starting with the letters K and Q have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT 
    f.title
FROM
    film f
WHERE
    (f.title LIKE 'K%' OR f.title LIKE 'Q%')
        AND f.language_id IN (SELECT 
            l.language_id
        FROM
            language l
        WHERE
            l.name = 'English');
            
-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT 
    a.first_name, a.last_name
FROM
    film_actor fa
        INNER JOIN
    actor a ON fa.actor_id = a.actor_id
WHERE
    fa.film_id IN (SELECT 
            f.film_id
        FROM
            film f
        WHERE
            f.title = 'Alone Trip');

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. 
-- Use joins to retrieve this information.
SELECT 
    s.first_name, s.last_name, s.email
FROM
    customer s
        INNER JOIN
    address a ON s.address_id = a.address_id
        INNER JOIN
    city c ON c.city_id = a.city_id
        INNER JOIN
    country co ON co.country_id = c.country_id
WHERE
    co.country = 'Canada'
;


-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as famiy films.
SELECT 
    film_id, title
FROM
    film
WHERE
    rating = 'G';

-- 7e. Display the most frequently rented movies in descending order.
SELECT 
    f.film_id, f.title, COUNT(*) AS 'Number of times rented'
FROM
    rental r
        INNER JOIN
    inventory i ON r.inventory_id = i.inventory_id
        INNER JOIN
    film f ON i.film_id = f.film_id
GROUP BY f.film_id , f.title
ORDER BY 3 DESC;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT 
    st.store_id, SUM(p.amount) 'Dollars, each store brought in'
FROM
    payment p
        INNER JOIN
    staff s ON s.staff_id = p.staff_id
        INNER JOIN
    store st ON st.store_id = s.store_id
GROUP BY st.store_id;

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT 
    s.store_id, c.city, co.country
FROM
    store s
        INNER JOIN
    address a ON s.address_id = a.address_id
        INNER JOIN
    city c ON c.city_id = a.city_id
        INNER JOIN
    country co ON co.country_id = c.country_id;

-- 7h. List the top five genres in gross revenue in descending order. 
-- (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT 
    c.name, SUM(p.amount)
FROM
    payment p
        INNER JOIN
    rental r ON p.rental_id = r.rental_id
        INNER JOIN
    inventory i ON r.inventory_id = i.inventory_id
        INNER JOIN
    film_category fc ON fc.film_id = i.film_id
        INNER JOIN
    category c ON c.category_id = fc.category_id
GROUP BY c.name
ORDER BY 2 DESC
LIMIT 5;


-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
CREATE OR REPLACE VIEW top_five_genres_view AS
    SELECT 
        c.name, SUM(p.amount)
    FROM
        payment p
            INNER JOIN
        rental r ON p.rental_id = r.rental_id
            INNER JOIN
        inventory i ON r.inventory_id = i.inventory_id
            INNER JOIN
        film_category fc ON fc.film_id = i.film_id
            INNER JOIN
        category c ON c.category_id = fc.category_id
    GROUP BY c.name
    ORDER BY 2 DESC
    LIMIT 5;



-- 8b. How would you display the view that you created in 8a?
SELECT 
    *
FROM
    top_five_genres_view;
    
-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
drop view if exists top_five_genres_view;