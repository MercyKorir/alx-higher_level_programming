-- This script lists all records with "score >= 10 in "second_table"
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
