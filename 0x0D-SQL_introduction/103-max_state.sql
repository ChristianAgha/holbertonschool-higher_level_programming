-- displays the max temperature of each state
SELECT state, MAX(value)
       AS max_temp
       FROM temperatures
       WHERE state IN (SELECT DISTINCT state FROM temperatures)
       GROUP BY state;
