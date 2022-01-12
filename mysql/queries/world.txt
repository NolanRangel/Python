USE world;

SELECT * FROM countries;


-- 1.
SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages ON countries.id = languages.country_id
ORDER BY languages.percentage DESC;

-- 2.

SELECT countries.name, COUNT(cities.name) AS number_of_cities
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY number_of_cities DESC;

-- 3.

SELECT countries.name, cities.name, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name LIKE "Mexico%" AND LENGTH(countries.name) = 6 AND cities.population > 500000 
ORDER BY population DESC;

-- 4.

SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages on countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY percentage DESC;

-- 5.

SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

-- 6.

SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital > 200 AND countries.life_expectancy > 75
ORDER BY life_expectancy DESC;

-- 7.

SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population
FROM countries
LEFT JOIN cities on countries.id = cities.country_id
WHERE countries.name LIKE "Argentina%" AND cities.district LIKE "Buenos Aires%" AND cities.population > 500000 ;

-- 8.

SELECT  countries.region, COUNT(countries.name) AS total_countries
FROM countries
GROUP BY countries.region
ORDER BY total_countries DESC;










