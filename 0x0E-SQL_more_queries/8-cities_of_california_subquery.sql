-- This script lists all cities of california that are in hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state_id IN (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY id;
