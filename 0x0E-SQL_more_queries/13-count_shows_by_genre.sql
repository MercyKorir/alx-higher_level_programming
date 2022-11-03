-- This script lists all genres from hbtn_0d_tvshows
SELECT tv_genres.name COUNT(*)
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.`id` = tv_show_genres.`genre_id`
GROUP BY tv_genres.`name`
ORDER BY `number_of_shows` DESC;
