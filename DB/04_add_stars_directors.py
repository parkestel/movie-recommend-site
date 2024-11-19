# 1. 기존 movies.json에 tmdb_id 돌면서 movies_detail에 API 요청보내기
# 2. 기존 movies.json에 stars 필드랑 directors 필드 만들기
# 3. 동시에 stars.json, directors.json 새로 만들기
    # 3-1. stars.json 
    #  "known_for_department": "Acting"인 사람들
    # > tmdb_id = int("id"), name = text("name"), 
    #       profile_path = text("profile_path", default = null), character = (movies_id, "character")
    #   order가 0~4까지만 배우 받아오기 and order 필드 추가해서 일단 값 넣어놓기
    # 3-2. directors.json
    #   job": "Director"인 사람들
    # tmdb_id = int("id"), name = text("name"), 
    #       profile_path = text("profile_path", default = null),


import requests
import json
import time

API_KEY = ''
API_URL = 'https://api.themoviedb.org/3/'
json_data = 'movies_add_otts.json'


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

            movie['fields']['stars'] = [cast.get('id') for cast in main_cast if cast.get('known_for_department') == 'Acting']
            movie['fields']['directors'] = [crew.get('id') for crew in credits.get('crew', []) if crew.get('job') == 'Director']
            updated_data.append(movie)

        except Exception as e:
            print(f"Error processing TMDB ID: {tmdb_id} - {e}")

        time.sleep(0.25)

    with open('updated_movies.json', 'w', encoding='utf-8') as movies_file:
        json.dump(updated_data, movies_file, ensure_ascii=False, indent=4)
    with open('stars.json', 'w', encoding='utf-8') as stars_file:
        json.dump(list(stars_data.values()), stars_file, ensure_ascii=False, indent=4)
    with open('directors.json', 'w', encoding='utf-8') as directors_file:
        json.dump(list(directors_data.values()), directors_file, ensure_ascii=False, indent=4)

    print("Processing complete. Files saved: updated_movies.json, stars.json, directors.json")


# 기존 movies_add_genres.json 불러오기
with open('movies_add_genres.json', 'r', encoding='utf-8') as file:
    movies_json = json.load(file)

# 첫 20개만 실행
# update_movies_and_create_stars_directors(movies_json[:20], max_stars=5)

update_movies_and_create_stars_directors(movies_json, max_stars=5)
