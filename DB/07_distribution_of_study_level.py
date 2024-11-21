import csv
from collections import Counter

# CSV 파일 경로 설정
input_file = "filtered_300.csv"

# study_level 값을 저장할 리스트
study_levels = []

# CSV 파일 읽기
with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        study_levels.append(row['study_level'])  # study_level 값을 리스트에 추가

# 각 study_level 값의 개수 세기
level_counts = Counter(study_levels)

# 결과 출력
for level in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
    print(f"{level}: {level_counts.get(level, 0)}")
# A1: 0   0%
# A2: 15  5%
# B1: 42  14 %
# B2: 76  25.33 %
# C1: 138  46 %
# C2: 29  9.67 %

# filtered
# A1: 0
# A2: 45
# B1: 90
# B2: 60
# C1: 60
# C2: 30