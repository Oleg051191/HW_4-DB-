from req import *
if __name__ == '__main__':
                                        ############# ЗАДАЧА № 1 ################
    pprint(spotify_user.download_all_genre())
    pprint(spotify_user.download_artist_info("""6wWVKhxIU2cEi0K81v7HvP,4RddZ3iHvSpGV4dvATac9X,3vvLuXEEf7sl3izJcw0GIn,1kmpkcYbuaZ8tnFejLzkj2,2KoLmBXwsgMkfAvoPBlPmb,6deZN1bslXzeGvOLaLMOIF,7MqnCTCAX6SsIYYdJCQj9B,6caPJFLv1wesmM7gwK1ACy"""))
    pprint(spotify_user.download_artist_album('6caPJFLv1wesmM7gwK1ACy'))
    pprint(spotify_user.download_tracks('6caPJFLv1wesmM7gwK1ACy'))
    pprint(spotify_user.info_albums('1kmpkcYbuaZ8tnFejLzkj2'))
    pprint(spotify_user.info_tracks('1kmpkcYbuaZ8tnFejLzkj2'))
    print(spotify_user.add_collection('My lovely Tracks', 2019))
    print(spotify_user.add_track_to_col(8, 45))
    print(spotify_user.add_artist_genre(8, 2))

                                        ############# ЗАДАЧА № 2 ################
    sel1 = sql_query.execute("""SELECT title_album, year_production FROM albums WHERE year_production BETWEEN '2018-01-01' AND '2018-12-31';""").fetchall()
    print(sel1)
    sel2 = sql_query.execute("""SELECT name_track, duration FROM tracks ORDER BY duration DESC;""").fetchone()
    print(sel2)
    sel3 = sql_query.execute("""SELECT name_track FROM tracks WHERE duration >= 210000;""").fetchall()
    pprint(sel3)
    sel4 = sql_query.execute("""SELECT name_collection FROM collection WHERE release_date BETWEEN 2018 AND 2020;""").fetchall()
    pprint(sel4)
    sel5 = sql_query.execute("""SELECT name_of_artist FROM artists WHERE name_of_artist NOT LIKE '%% %%';""").fetchall()
    pprint(sel5)
    sel6 = sql_query.execute("""SELECT name_track FROM tracks WHERE name_track LIKE '%%Me%%';""").fetchall()
    pprint(sel6)
