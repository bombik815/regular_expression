/* 1. название и год выхода альбомов, вышедших в 2018 году*/
 select name, year_album from album a 
where year_album = 2018

/* 2. название и продолжительность самого длительного трека;
 * первый вариант */
 select name_track, duration_min from list_tracks lt  
order by duration_min desc 
limit 1
/*второй вариант*/
select name_track, duration_min from list_tracks lt  
where duration_min = (select max(duration_min) from lt )

/* 3.название треков, продолжительность которых не менее 3,5 минуты;*/
select name_track, duration_min from list_tracks lt 
where duration_min >= 3.5
order by duration_min desc 

/*4. названия сборников, вышедших в период с 2018 по 2020 год включительно;*/
select name, year_album from collection c 
where year_album between 2018 and 2020

/*5. исполнители, чье имя состоит из 1 слова;*/
select name from artist a 
 where name not like '% %'

/*6. название треков, которые содержат слово "мой"/"my".*/
select name_track from list_tracks lt 
where name_track ilike '%My%'