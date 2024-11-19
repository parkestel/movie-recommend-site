# 장르까지 추가된 movies.json 에 otts 필드 추가

import json
import requests

API_KEY = ''
API_URL = 'https://api.themoviedb.org/3/'


json_file_path = "movies_add_genres.json"  # 기존 JSON 파일 경로
output_json_path = "movies_add_otts.json"  # 결과 JSON 파일 경로

# 기존 JSON 데이터 로드
with open(json_file_path, "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)


# 테스트용으로 처음 20개 영화만 처리
# test_limit = 40
# test_data = json_data[:test_limit]


for idx, movie in enumerate(json_data, start=1):
        tmdb_id = movie['fields']['tmdb_id']
        # print(f"Processing TMDB ID: {tmdb_id} ({idx}/{test_limit})")
        print(f"Processing TMDB ID: {tmdb_id} ({idx}/{len(json_data)})")

        # API 요청 URL 생성
        ott_api_url = f"{API_URL}movie/{tmdb_id}/watch/providers?api_key={API_KEY}"
        
        try:
            # API 요청 보내기
            response = requests.get(ott_api_url)
            response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
            watch_data = response.json()

            # "results"에서 "KR" 키 확인
            results = watch_data.get("results", {})
            kr_data = results.get("KR")

            # 조건에 따라 otts 필드 설정
            if kr_data and "flatrate" in kr_data:
               # 중복 제거를 위해 set 사용 후 list로 변환
                movie['fields']['otts'] = list({
                    provider['provider_id'] for provider in kr_data["flatrate"]
                })
            else:
                movie['fields']['otts'] = []  # "KR" 키가 없거나 "flatrate"가 없으면 빈 배열


        except requests.RequestException as e:
            print(f"Error fetching data for TMDB ID {tmdb_id}: {e}")
            movie['fields']['otts'] = []  # 요청 실패 시 빈 배열

# 수정된 데이터를 새 JSON 파일로 저장
with open(output_json_path, "w", encoding="utf-8") as output_file:
    json.dump(json_data, output_file, ensure_ascii=False, indent=4)

print("Process completed. Modified JSON saved to:", output_json_path)