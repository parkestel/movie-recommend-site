# 04_add_star_~.py 코드가 자꾸 otts 필드 제거하길래 새로 함

import requests
import json
import time

API_KEY = ''
API_URL = 'https://api.themoviedb.org/3/'
json_file = 'movies_add_otts.json'


def update_movies_and_create_stars_directors(json_data, max_stars=5):
    updated_data = []
    stars_data = {}
    directors_data = {}
    star_pk = 1
    director_pk = 1

    for idx, movie in enumerate(json_data, start=1):
        tmdb_id = movie['fields'].get('tmdb_id')
        if not tmdb_id:
            print(f"Missing TMDB ID for movie index {idx}, skipping.")
            continue

        print(f"Processing TMDB ID: {tmdb_id} ({idx}/{len(json_data)})")

        movie_credit_url = f'{API_URL}movie/{tmdb_id}/credits?api_key={API_KEY}'
        try:
            response = requests.get(movie_credit_url)
            if response.status_code != 200:
                print(f"Failed to fetch credits for TMDB ID: {tmdb_id}, Status Code: {response.status_code}")
                continue

            credits = response.json()
            cast_data = credits.get('cast', [])
            main_cast = sorted(cast_data, key=lambda x: int(x.get("order", 99999)))[:max_stars]

            # Adding stars data
            for cast in main_cast:
                if cast.get('known_for_department') == 'Acting':
                    star_id = cast.get('id')
                    if not star_id:
                        continue

                    if star_id not in stars_data:
                        stars_data[star_id] = {
                            "model": "movies.star",
                            "pk": star_pk,
                            "fields": {
                                "tmdb_id": star_id,
                                "name": cast.get('name', ''),
                                "profile_path": cast.get('profile_path'),
                                "characters": []
                            }
                        }
                        star_pk += 1
                    stars_data[star_id]["fields"]["characters"].append({
                        "movie_id": tmdb_id,
                        "character": cast.get("character", ""),
                        "order": int(cast.get("order", 99999)),
                    })

            # Adding directors data
            for crew in credits.get('crew', []):
                if crew.get('job') == 'Director':
                    director_id = crew.get('id')
                    if not director_id:
                        continue

                    if director_id not in directors_data:
                        directors_data[director_id] = {
                            "model": "movies.director",
                            "pk": director_pk,
                            "fields": {
                                "tmdb_id": director_id,
                                "name": crew.get('name', ''),
                                "profile_path": crew.get('profile_path')
                            }
                        }
                        director_pk += 1

            # Update movie with stars and directors
            movie['fields']['stars'] = [cast.get('id') for cast in main_cast if cast.get('known_for_department') == 'Acting']
            movie['fields']['directors'] = [crew.get('id') for crew in credits.get('crew', []) if crew.get('job') == 'Director']
            updated_data.append(movie)

        except Exception as e:
            print(f"Error processing TMDB ID: {tmdb_id} - {e}")

        time.sleep(0.25)

    # Save updated movies
    with open('updated_movies.json', 'w', encoding='utf-8') as movies_file:
        json.dump(updated_data, movies_file, ensure_ascii=False, indent=4)

    # Save stars and directors data
    with open('stars.json', 'w', encoding='utf-8') as stars_file:
        json.dump(list(stars_data.values()), stars_file, ensure_ascii=False, indent=4)
    with open('directors.json', 'w', encoding='utf-8') as directors_file:
        json.dump(list(directors_data.values()), directors_file, ensure_ascii=False, indent=4)

    print("Processing complete. Files saved: updated_movies.json, stars.json, directors.json")


# Load existing JSON data
with open(json_file, 'r', encoding='utf-8') as file:
    movies_json = json.load(file)

# 첫 20개만 실행
# update_movies_and_create_stars_directors(movies_json[:20], max_stars=5)

# Update movies and add stars and directors fields
update_movies_and_create_stars_directors(movies_json, max_stars=5)
