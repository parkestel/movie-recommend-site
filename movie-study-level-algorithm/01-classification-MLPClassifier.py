import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import BertTokenizer, BertModel
import torch

# nltk의 불용어와 표제어 추출 준비
nltk.download('stopwords')
nltk.download('wordnet')
stop_words = set(stopwords.words('english'))
# stop_words.add(':', 'text', 'dialog')
lemmatizer = WordNetLemmatizer()

# BERT 모델과 토크나이저 로드
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# CSV 파일 로드
data = pd.read_csv('C:/Users/SUNA/Desktop/PJT/03. score-difficulty/cefr_leveled_texts.csv')  # 파일명을 실제 파일명으로 변경하세요

# 텍스트 전처리 함수 정의
def preprocess_text(text):
    # 1. 토큰화 및 소문자 변환
    tokens = text.lower().split()
    
    # 2. 불용어 제거
    tokens = [word for word in tokens if word not in stop_words]
    
    # 3. 표제어 추출
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # 전처리된 텍스트 반환
    return ' '.join(tokens)

# 데이터에 전처리 적용
data['processed_text'] = data['text'].apply(preprocess_text)

# BERT 임베딩 함수 정의
def get_bert_embeddings(text):
    # 입력 텍스트를 BERT의 입력 형식으로 변환
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    # 임베딩 결과는 모델의 마지막 은닉층
    embeddings = outputs.last_hidden_state.mean(dim=1)  # 평균 풀링으로 문장 벡터 생성
    return embeddings.squeeze().numpy()

# BERT 임베딩 생성 및 적용
data['bert_embeddings'] = data['processed_text'].apply(get_bert_embeddings)

# 결과 확인
print(data[['text', 'label', 'processed_text', 'bert_embeddings']].head())


import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neural_network import MLPClassifier

# 전처리된 데이터 로드
# data = pd.read_csv('./cefr_leveled_texts.csv')  # 실제 파일명으로 변경하세요
X = np.stack(data['bert_embeddings'].values)   # BERT 임베딩을 사용한 입력 데이터
y = data['label'].values                       # CEFR 레벨 라벨

# 데이터 분할 (80% 학습용, 20% 테스트용)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


training_model = MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=300, random_state=42)

# 교차 검증을 통한 성능 평가
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(training_model, X_train, y_train, cv=kfold, scoring='accuracy')

print("K-Fold Cross-Validation Accuracy:", cv_scores)
print("Mean Cross-Validation Accuracy:", cv_scores.mean())

# 최종 학습 및 예측
training_model.fit(X_train, y_train)
y_pred = training_model.predict(X_test)

# 모델 평가
print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 영화 대사 난이도 예측 함수
def predict_difficulty(dialogues):
    dialogues_processed = [preprocess_text(dialogue) for dialogue in dialogues]  # 전처리 적용
    embeddings = [get_bert_embeddings(dialogue) for dialogue in dialogues_processed]  # BERT 임베딩 적용
    predictions = training_model.predict(embeddings)
    return predictions

# 예시: 새로운 영화 대사 난이도 예측
# new_dialogues = ["In view of this, the Ethiopian Government and other developmental partners have introduced an extensive mechanical and biological watershed conservation schemes in various parts of the country over the last decades particularly after the famine of the 1970s"]
# difficulty_predictions = predict_difficulty(new_dialogues)
# print("Predicted CEFR Levels:", difficulty_predictions)

import os

# .txt 파일의 난이도를 예측하는 함수
def predict_difficulty_from_txt(file_path):
    if not os.path.exists(file_path):
        print(f"파일 {file_path}이(가) 존재하지 않습니다.")
        return
    
    # .txt 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as file:
        file_name = os.path.basename(file_path)
        imdb_id = os.path.splitext(file_name)[0]
        dialogues = file.read()
    
    # 텍스트 전처리
    processed_text = preprocess_text(dialogues)
    
    # BERT 임베딩 생성
    embedding = get_bert_embeddings(processed_text)
    
    # 난이도 예측
    prediction = training_model.predict([embedding])
    
    # 결과 출력
    print(f"파일 전체의 예측된 CEFR 레벨: {prediction[0]}")
    return prediction[0]

# # 예시: .txt 파일에서 난이도 예측
# txt_file_path = "merged_scripts/tt2380307.txt"  # .txt 파일 경로를 입력하세요
# predict_difficulty_from_txt(txt_file_path)


from pathlib import Path

# 특정 폴더 내 모든 텍스트 파일의 난이도 예측
def predict_folder_difficulty(folder_path):
    folder = Path(folder_path)
    
    # 폴더 확인
    if not folder.exists() or not folder.is_dir():
        print(f"폴더 {folder_path}이(가) 존재하지 않거나 유효하지 않습니다.")
        return
    
    # 폴더 내 모든 .txt 파일 리스트 가져오기
    txt_files = list(folder.glob("*.txt"))
    if not txt_files:
        print(f"폴더 {folder_path}에 텍스트 파일이 없습니다.")
        return
    
    # 결과 저장용 리스트
    results = []
    
    # 각 파일에 대해 난이도 예측
    for file_path in txt_files:
        print(f"처리 중: {file_path.name}")
        with open(file_path, 'r', encoding='utf-8') as file:
            full_text = file.read()
        
        # 텍스트 전처리 및 임베딩 생성
        processed_text = preprocess_text(full_text)
        embedding = get_bert_embeddings(processed_text)
        
        # 난이도 예측
        predicted_level = training_model.predict([embedding])[0]
        
        # 결과 저장 (파일 이름, 예측된 레벨)
        results.append((file_path.stem, predicted_level))
        print(f"파일 {file_path.stem}의 예측된 CEFR 레벨: {predicted_level}")
    
    # 최종 결과 반환
    return results

# 결과를 CSV로 저장하는 함수
import pandas as pd
def save_results_to_csv(results, output_path):
    
    # 데이터프레임 생성 및 저장
    df = pd.DataFrame(results, columns=["imdbid", "predicted_level"])
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"결과가 {output_path}에 저장되었습니다.")

# 사용 예시
folder_path = "C:/Users/SUNA/Desktop/PJT/05-score-difficulty-with-script/merged_scripts"  # 텍스트 파일이 있는 폴더 경로
output_csv_path = "C:/Users/SUNA/Desktop/PJT/05-score-difficulty-with-script/result/result.csv"  # 저장할 CSV 경로

# 폴더 내 모든 파일 처리 및 결과 저장
results = predict_folder_difficulty(folder_path)
if results:
    save_results_to_csv(results, output_csv_path)