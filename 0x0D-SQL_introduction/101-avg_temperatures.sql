-- displays the average temperature by city ordered by temperature (descending)
SELECT city, AVG(value)
       AS avg_temp
       FROM temperatures
       WHERE city IN (SELECT DISTINCT city FROM temperatures)
       GROUP BY city
       ORDER BY avg_temp DESC;
