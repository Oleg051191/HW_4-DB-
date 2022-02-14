create table if not exists artists(id serial primary key, name_of_artist text, url_spotify text);
create table if not exists genre(id serial primary key, name_of_genre text not null);
create table if not exists artist_genre(artist_id integer references artists(id), genre_id integer references genre(id),
	constraint pk primary key (artist_id, genre_id));
--	
--
create table if not exists albums(id serial primary key, title_album varchar(40) not null, year_production text not null);
create table if not exists artist_albums(artist_id integer references artists(id), album_id integer references albums(id),
	constraint pk_album primary key (artist_id, album_id));
--
create table if not exists tracks(id serial primary key, name_track text, duration integer constraint ch_600000 check(duration<600000),
	name_album integer references albums(id));
--
create table if not exists collection(id serial primary key, name_collection varchar(40) not null, release_date integer not null);
--
create table if not exists collection_track(collection_id integer references collection(id), track_id integer references tracks(id), 
	constraint col_pk primary key (collection_id, track_id));

select * from collection_track;
select * from artists;
select * from tracks;
alter table albums alter column year_production SET DATA type date USING year_production::date
select * from albums;
