# 데이터 시각화 가이드

## 📊 시각화 목표

이 프로젝트의 시각화는 다음과 같은 인사이트를 제공하는 것을 목표로 합니다:

1. **FSC vs LCC 시장 점유율 비교**
2. **월별 여객 이용률 트렌드**
3. **노선별 이용률 분석**
4. **항공사별 성과 비교**

## 🎨 시각화 유형별 가이드

### 1. 시계열 차트 (Line Chart)
**용도**: 월별 트렌드 분석
```python
# 예시 코드
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_data, x='월', y='여객수', hue='항공사구분')
plt.title('월별 여객 수 추이 (FSC vs LCC)')
plt.xlabel('월')
plt.ylabel('여객 수')
plt.legend(title='항공사 구분')
plt.show()
```

### 2. 막대 차트 (Bar Chart)
**용도**: 항공사별 비교, 노선별 비교
```python
# 항공사별 점유율 비교
plt.figure(figsize=(10, 6))
sns.barplot(data=airline_data, x='항공사', y='이용율')
plt.title('항공사별 평균 이용률')
plt.xticks(rotation=45)
plt.show()
```

### 3. 히트맵 (Heatmap)
**용도**: 노선별 항공사별 이용률 매트릭스
```python
# 노선별 항공사별 이용률 히트맵
pivot_data = df.pivot_table(values='이용율', 
                           index='노선', 
                           columns='항공사', 
                           aggfunc='mean')

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_data, annot=True, cmap='YlOrRd', fmt='.1f')
plt.title('노선별 항공사별 평균 이용률')
plt.show()
```

### 4. 파이 차트 (Pie Chart)
**용도**: 시장 점유율 분포
```python
# FSC vs LCC 시장 점유율
plt.figure(figsize=(8, 8))
plt.pie(market_share['점유율'], 
        labels=market_share['구분'], 
        autopct='%1.1f%%')
plt.title('FSC vs LCC 시장 점유율')
plt.show()
```

### 5. 박스 플롯 (Box Plot)
**용도**: 분포 비교, 이상치 탐지
```python
# 항공사별 이용률 분포
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='항공사', y='이용율')
plt.title('항공사별 이용률 분포')
plt.xticks(rotation=45)
plt.show()
```

## 📈 주요 시각화 결과

### 1. 월별 트렌드 분석
- **여름 시즌 (6-8월)**: 여객 수 급증
- **겨울 시즌 (12-2월)**: 상대적으로 낮은 이용률
- **2024년 vs 2025년**: 회복세 및 성장세

### 2. FSC vs LCC 비교
- **LCC**: 높은 점유율 (90-95%)
- **FSC**: 안정적인 점유율 (85-90%)
- **시장 점유율 변화**: LCC 성장세

### 3. 노선별 분석
- **김포-제주**: 최고 이용률
- **지역 노선**: 특정 항공사 독점
- **중단거리**: LCC 강세

### 4. 항공사별 성과
- **제주항공**: LCC 중 최고 성과
- **대한항공**: FSC 중 안정적 성과
- **에어부산**: 지역 노선 전문

## 🎨 시각화 모범 사례

### 1. 색상 팔레트
```python
# FSC vs LCC 구분 색상
fsc_color = '#1f77b4'  # 파란색
lcc_color = '#ff7f0e'  # 주황색

# 항공사별 색상
airline_colors = {
    '대한항공': '#1f77b4',
    '아시아나': '#2ca02c',
    '제주항공': '#ff7f0e',
    '에어부산': '#d62728',
    '진에어': '#9467bd',
    '티웨이항공': '#8c564b',
    '이스타항공': '#e377c2'
}
```

### 2. 폰트 설정
```python
# 한글 폰트 설정
import matplotlib.font_manager as fm

# Windows
plt.rcParams['font.family'] = 'Malgun Gothic'
# Mac
# plt.rcParams['font.family'] = 'AppleGothic'
```

### 3. 차트 스타일
```python
# 차트 스타일 설정
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
```

## 📊 대시보드 구성

### 1. 메인 대시보드
- 월별 트렌드 차트
- FSC vs LCC 점유율 파이 차트
- 항공사별 성과 막대 차트

### 2. 상세 분석 페이지
- 노선별 히트맵
- 항공사별 분포 박스 플롯
- 시계열 상세 분석

### 3. 인사이트 요약
- 주요 지표 KPI
- 트렌드 요약
- 예측 및 전망

## 🔧 시각화 도구

### 1. Python 라이브러리
- **Matplotlib**: 기본 시각화
- **Seaborn**: 통계 시각화
- **Plotly**: 인터랙티브 차트
- **Pandas**: 데이터 처리

### 2. 대시보드 도구
- **Streamlit**: Python 기반 대시보드
- **Dash**: Plotly 기반 대시보드
- **Jupyter Notebook**: 분석 노트북

## 📋 시각화 체크리스트

- [ ] 데이터 전처리 완료
- [ ] 적절한 차트 유형 선택
- [ ] 색상 및 폰트 설정
- [ ] 제목 및 라벨 추가
- [ ] 범례 설정
- [ ] 축 스케일 조정
- [ ] 그리드 및 배경 설정
- [ ] 파일 저장 (고해상도)

---

**참고**: 모든 시각화는 분석 목적에 맞게 설계되어야 하며, 
데이터의 특성을 정확히 반영하는 것이 중요합니다. 