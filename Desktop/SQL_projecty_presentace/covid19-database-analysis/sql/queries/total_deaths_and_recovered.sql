SELECT 
	country,
	SUM(deaths) AS total_deaths, -- sum of deaths from each country
	SUM(recovered) AS total_recveredv -- sum of recovered from each counry
FROM covid19_basic cb 
GROUP BY country 
ORDER BY country;



