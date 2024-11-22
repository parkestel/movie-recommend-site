import csv

import csv
from collections import defaultdict

# 파일 경로 설정
input_file = "movie_data.csv"
output_file = "filtered_2_300.csv"

# 데이터 읽기
with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# rank 기준 내림차순 정렬
sorted_rows = sorted(rows, key=lambda x: float(x['rank']), reverse=True)

# study_level별 데이터 분류
grouped_by_level = defaultdict(list)
for row in sorted_rows:
    grouped_by_level[row['study_level']].append(row)

# 분포 기준 설정 (총 300개 중)
# target_counts = {
#     'A1': 15,  # 5%
#     'A2': 45,  # 15%
#     'B1': 90,  # 30%
#     'B2': 60,  # 20%
#     'C1': 60,  # 20%
#     'C2': 30   # 10%
# }
# A1 없어서 새로 함
target_counts = {
    'A1': 0,  # 5%
    'A2': 45,  # 15%
    'B1': 90,  # 30%
    'B2': 75,  # 20%
    'C1': 60,  # 20%
    'C2': 30   # 10%
}

# 최종 데이터 선택
final_rows = []
for level, target_count in target_counts.items():
    final_rows.extend(grouped_by_level[level][:target_count])

# 최종 데이터가 300개를 초과/미만하는 경우 조정
final_rows = final_rows[:300]

# 새 CSV 파일로 저장
with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    fieldnames = rows[0].keys()  # 기존 CSV의 헤더 가져오기
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(final_rows)

print(f"분포를 고려한 상위 300개 데이터를 {output_file}에 저장했습니다.")



# # 기존 CSV 파일 경로와 새로 저장할 CSV 파일 경로 설정
# input_file = "movie_data.csv"
# output_file = "output_top_300.csv"

# # CSV 파일 읽고 상위 300개 추출
# with open(input_file, mode='r', encoding='utf-8') as infile:
#     reader = csv.DictReader(infile)
#     rows = list(reader)

# # rank 기준 내림차순 정렬
# sorted_rows = sorted(rows, key=lambda x: float(x['rank']), reverse=True)

# # 상위 300개 데이터 선택
# top_300 = sorted_rows[:300]

# # 새 CSV 파일로 저장
# with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
#     fieldnames = reader.fieldnames  # 기존 CSV의 헤더 가져오기
#     writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(top_300)

# print(f"상위 300개 데이터를 {output_file}에 저장했습니다.")
