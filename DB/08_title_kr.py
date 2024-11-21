import requests
import json

API_KEY = '39c9908752032848483d2c4bbb58a1ec'
API_URL = 'https://api.themoviedb.org/3/'
json_file_path = 'movies_all_mtm.json'


with open(json_file_path, "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)


# 테스트용으로 처음 20개 영화만 처리
# test_limit = 40
# test_data = json_data[:test_limit]

for idx, movie in enumerate(json_data, start=1):
        tmdb_id = movie['fields']['tmdb_id']

        print(f"Processing TMDB ID: {tmdb_id} ({idx}/{len(json_data)})")

        # API 요청 URL 생성
        url = f'{API_URL}movie/{tmdb_id}?api_key={API_KEY}&language=ko-KR'
        
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        # title과 adult 데이터 확인
        title_kr = data.get('title', '한글 제목 없음')
        is_adult = data.get('adult')  

        # 디버깅용 출력
        print(f"Title (KR): {title_kr}")
        print(f"Is Adult: {is_adult}")

        # JSON 데이터에 추가할 경우
        movie['fields']['title_kr'] = title_kr
        movie['fields']['is_adult'] = is_adult
    # 결과 저장 (선택 사항)

output_file_path = 'updated_movies.json'

with open(output_file_path, "w", encoding="utf-8") as outfile:
    json.dump(json_data, outfile, ensure_ascii=False, indent=4)
    print(f"Updated data saved to {output_file_path}")