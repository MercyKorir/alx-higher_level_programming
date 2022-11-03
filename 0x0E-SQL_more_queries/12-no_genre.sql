-- This script lists all shows contained in hbtn_0d_tvshows without genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id in NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
