import json
import requests
from collections import OrderedDict

# TMDB API 설정
API_KEY = ''
API_URL = 'https://api.themoviedb.org/3/person/'

# JSON 데이터 파일 경로
input_file = "stars.json"
output_file = "kr_name_stars.json"

def is_korean(text):
    for char in text:
        if '\uac00' <= char <= '\ud7a3':  # 한글 유니코드 범위
            return True
    return False

# JSON 파일 로드 함수
def load_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# JSON 파일 저장 함수
def save_json_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# name_kr 필드 업데이트 함수
def update_json_with_name_kr(json_data):
    updated_data = []
    for item in json_data:
        if "fields" in item and "tmdb_id" in item["fields"]:
            tmdb_id = item["fields"]["tmdb_id"]
            url = f'{API_URL}{tmdb_id}?api_key={API_KEY}&language=ko-KR'
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    person_data = response.json()
                    name_kr_value = person_data.get("name", "")
                    if not is_korean(name_kr_value):
                        name_kr_value = ""  # 영어 이름인 경우 빈 문자열로 설정
                    
                    # 필드 순서 조정
                    fields = item["fields"]
                    updated_fields = OrderedDict()
                    for key, value in fields.items():
                        updated_fields[key] = value
                        if key == "name":  # name 바로 밑에 name_kr 추가
                            updated_fields["name_kr"] = name_kr_value
                    
                    item["fields"] = updated_fields
                else:
                    print(f"Failed to fetch data for TMDB ID: {tmdb_id}, Status Code: {response.status_code}")
            except Exception as fetch_error:
                print(f"Error fetching data for TMDB ID {tmdb_id}: {fetch_error}")
        
        updated_data.append(item)
    return updated_data

# JSON 데이터 처리
try:
    # JSON 데이터 로드
    json_data = load_json_file(input_file)
    # name_kr 필드 업데이트
    updated_data = update_json_with_name_kr(json_data)
    # 업데이트된 데이터 저장
    save_json_file(output_file, updated_data)
    print(f"JSON 데이터 업데이트 완료! 저장 위치: {output_file}")
except Exception as e:
    print(f"오류 발생: {e}")