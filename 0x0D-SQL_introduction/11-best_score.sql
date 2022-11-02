-- This script lists all records with "score >= 10 in "second_table"
SELECT score, name
FROM second_table
ORDER BY score DESC
HAVING score >= 10;
