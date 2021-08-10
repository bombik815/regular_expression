create table if not exists Genres(
	id_genre SERIAL PRIMARY key,
	name VARCHAR(40) not null
	);
	
create table if not exists Artist(
	id_artist SERIAL PRIMARY key,
	name VARCHAR(50),
	age INTEGER
	);
	
create table if not exists genres_artist(
	id_genres_artist SERIAL PRIMARY key,
	id_genre INTEGER NOT NULL REFERENCES Genres(id_genre) not null,
	id_artist INTEGER NOT NULL REFERENCES Artist(id_artist) not null
	);
	
	create table if not exists Album(
	id_album SERIAL PRIMARY key,
	name VARCHAR(40) not null,
	year_album INTEGER
	);
	
	
create table if not exists artist_album(
	id_artist_album SERIAL PRIMARY key,
	id_album INTEGER NOT NULL REFERENCES Album(id_album) not null,
	id_artist INTEGER NOT NULL REFERENCES Artist(id_artist)not null
	);
	
create table if not exists List_tracks(
	id_list_tracks SERIAL PRIMARY key,
	name_track VARCHAR(50) not null,
	duration_min numeric(4,2) check (duration_min > 0) not null,
	id_album integer references Album(id_album) not null
	);
	
	create table if not exists Collection(
	id_collection SERIAL PRIMARY key,
	name VARCHAR(40) not null,
	year_album INTEGER
	);
	
	create table if not exists Collection_tracks(
	id_collection_tracks SERIAL PRIMARY key,
	id_collection INTEGER NOT NULL REFERENCES Collection(id_collection) not null,
	id_list_tracks INTEGER NOT NULL REFERENCES List_tracks(id_list_tracks)not null
	);