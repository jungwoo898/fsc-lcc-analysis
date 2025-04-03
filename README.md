# ✈️ FSC & LCC 항공사 여객 이용 분석 (2024~2025)

### 프로젝트 개요

저가 항공사(LCC)와 대형 항공사(FSC)의 여객 이용률과 유아 탑승 비율을 비교 분석한 프로젝트입니다.  
특히 2024년과 2025년 1월 데이터를 중심으로, 무안공항 사고 이후 소비자 반응을 분석하고  
LCC의 향후 성장 가능성에 대한 인사이트를 도출하는 데 목적이 있습니다.

- 분석 기간: 2024년 1월 ~ 8월, 2025년 1월
- 사용 도구: Python, MySQL, Pandas, Matplotlib

---

### 분석 목표

1. FSC와 LCC의 월별 좌석 대비 탑승률 비교  
2. FSC와 LCC의 유아 탑승객 비율 비교  
3. 2024년 1월과 2025년 1월 여객 수 변화 분석

---

### 데이터 및 전처리 방식

- 한국공항공사에서 제공하는 CSV 데이터를 활용
- SQL을 통해 FSC/LCC 구분 및 그룹화
- 전처리 후 Python으로 통합, 시각화 진행

#### 주요 파일
- `sql flight.sql`: 데이터 전처리용 MySQL 쿼리 스크립트
- `flight.py`: 분석 및 시각화 전체 코드
- `FSC&LCC analysis.pdf`: 분석 개요 및 주요 결과 정리

---

### 시각화 예시

| 그래프 제목              | 설명                                    
|--------------------------|-------------------------------------------
| 항공사별 유아 탑승객 수    | FSC와 LCC의 유아 고객 비율 비교           
| 2024 vs 2025 1월 탑승객 수| 무안공항 사고 이후 여객 변화 확인          
| 월별 평균 이용률 추이      | 시즌별 항공사 성적 비교                    

---

### 주요 인사이트

- LCC는 2월을 제외한 대부분의 달에서 높은 탑승률을 보임  
- 유아 탑승객 비율 역시 LCC가 FSC보다 높아 가족 단위 수요가 뚜렷  
- 무안공항 사고 이후에도 LCC 수요는 큰 변동 없이 유지됨

---

### 기대 효과

- LCC의 사업 전략 수립에 참고자료로 활용 가능  
- 항공사 마케팅 전략 수립을 위한 소비자 수요 분석 자료 제공

---

### 실행 방법

```bash
# MySQL 설정 후 flight.sql 실행
# 데이터 CSV 파일은 ./data 폴더에 위치해야 함

# Python 코드 실행
python flight.py
```

---

### 만든 사람

- 오정우 (데이터 분석 입문자)  
- 이메일: woo0801nr@gmail.com  
- GitHub: https://github.com/jungwoo898/jungsungworkjob
