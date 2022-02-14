import requests
from pprint import pprint
import sqlalchemy
import settings
db = 'postgresql://postgres:escort@localhost:5432/data_b_hw2'
engine = sqlalchemy.create_engine(db)
sql_query = engine.connect()

class Spotify:

    url = 'https://api.spotify.com/v1/'
    def get_headers(self):
        """Получение заголовков на отправку запросов к сервису"""
        headers = {'Authorization': f'Bearer {settings.access_token}',
                   'Content-Type': 'application/json'
                   }
        return headers

    def download_all_genre(self):
        """Метод, загружающий в БД сведения о имеющихся в Spotify жанрах"""
        url_genres = self.url + f"recommendations/available-genre-seeds"
        response = requests.get(url=url_genres, headers=self.get_headers()).json()['genres']
        all_genres = []
        for genre in response:
            if genre in ['deep-house', 'hard-rock', 'metal', 'pop', 'dance', 'drum-and-bass', 'hip-hop']:
                all_genres.append(genre)
                sql_query.execute(f"""INSERT INTO genre(name_of_genre) VALUES ('{genre}')""")
        return f"All genre ({len(all_genres)}) from Spotify was successfully downloads in DB table - 'genre'"

    def download_artist_info(self, artists_id):
        """Метод, загружающий сведения об артистах в БД по их ID"""
        url_artist = self.url + f'artists'
        params = {'ids': artists_id}
        all_artist = requests.get(url=url_artist, headers=self.get_headers(), params=params).json()['artists']
        all_name = []
        for artist in all_artist:
            url_spotify_artist = artist['external_urls']['spotify']
            artist_name = artist['name']
            all_name.append(artist_name)
            sql_query.execute(f"""INSERT INTO artists(name_of_artist, url_spotify) VALUES('{artist_name}','{url_spotify_artist}')""")
        return f"Info about {len(all_name)} artists was successfully downloads in DB table - 'artists'"

    def download_artist_album(self, artists_id):
        """Метод, загружащий сведения в БД о первом альбоме артиста по его ID. При необходимости можно изменить срез
        и загрузить информацию о всех альбомах. Помимо этого, при наличии альбомов с одиниковым именем, происходит
        загрузка только одного"""
        url_albums = self.url + f'artists/{artists_id}/albums'
        all_albums = requests.get(url=url_albums, headers=self.get_headers()).json()['items']
        albums_artist = []
        for album in all_albums[0:1]:
            if (album['name'], album['release_date']) not in albums_artist:
                albums_artist.append((album['name'], album['release_date']))
            else:
                pass
        for name_alb, data_r in albums_artist:
            sql_query.execute(f"""INSERT INTO albums(title_album, year_production) VALUES('{name_alb}', '{data_r}')""")
        return f"Info about {len(albums_artist)} albums was successfully downloads in DB table - 'albums'"

    def download_tracks(self, artists_id):
        """Метод, загружающий информацию о самых популярных треках исполнителя из Spotify в БД по ID исполнителя"""
        url_tracks = self.url + f'artists/{artists_id}/top-tracks'
        params = {'market': 'RU'}
        all_tracks = requests.get(url=url_tracks, headers=self.get_headers(), params=params).json()['tracks']
        for track in all_tracks:
            track_n = track['name']
            duration_t = track['duration_ms']
            sql_query.execute(f"""INSERT INTO tracks(name_track,duration,name_album) VALUES('{track_n}', {duration_t}, {8})""")
        return f"Info about tracks was successfully downloads in DB table - 'tracks'"


    def info_albums(self, artist_id):
        """Получение информации об альбомах"""
        url_albums = self.url + f'artists/{artist_id}/albums'
        all_albums = requests.get(url=url_albums, headers=self.get_headers()).json()['items']
        for album in all_albums[0:4]:
            pprint(album)

    def info_tracks(self, artists_id):
        """Получение информации о треках"""
        url_tracks = self.url + f'artists/{artists_id}/top-tracks'
        params = {'market': 'RU'}
        all_tracks = requests.get(url=url_tracks, headers=self.get_headers(), params=params).json()['tracks']
        return all_tracks

    def add_collection(self, name_col, release):
        """Добавление коллекции в БД"""
        sql_query.execute(f"""INSERT INTO collection(name_collection,release_date) VALUES('{name_col}', {release}) """)
        return f"collection with name {name_col} download in DB"

    def add_track_to_col(self, id_col, id_track):
        """Добавление треков к коллекции"""
        sql_query.execute(f"""INSERT INTO collection_track VALUES({id_col}, {id_track}) """)
        return f"tracks was added at col № {id_col}"

    def add_artist_genre(self, aritst_id, genre_id):
        """Добавление нового жанра в котором может выступать артист"""
        sql_query.execute(f"""INSERT INTO artist_genre VALUES({aritst_id}, {genre_id}) """)

spotify_user = Spotify()


