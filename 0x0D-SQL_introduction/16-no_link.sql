-- This script lists all records of second_table
SELECT score, EXISTS(name)
FROM second_table
ORDER BY score DESC;
