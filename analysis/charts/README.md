# 차트 이미지 폴더

이 폴더는 분석 결과를 시각화한 차트 이미지들을 저장합니다.

## 📊 예정 차트 목록

### 1. 월별 트렌드 차트
- **파일명**: `monthly_trend.png`
- **설명**: 2024년 1월부터 2025년 1월까지의 월별 여객 수 추이
- **차트 유형**: 시계열 라인 차트

### 2. FSC vs LCC 시장 점유율
- **파일명**: `market_share_pie.png`
- **설명**: FSC와 LCC 항공사의 시장 점유율 비교
- **차트 유형**: 파이 차트

### 3. 항공사별 평균 이용률
- **파일명**: `airline_utilization.png`
- **설명**: 각 항공사별 평균 좌석 점유율
- **차트 유형**: 막대 차트

### 4. 노선별 이용률 히트맵
- **파일명**: `route_heatmap.png`
- **설명**: 주요 노선별 항공사별 이용률 매트릭스
- **차트 유형**: 히트맵

### 5. 항공사별 성과 비교
- **파일명**: `airline_performance.png`
- **설명**: 항공사별 여객 수, 이용률, 유아 비율 비교
- **차트 유형**: 복합 차트

### 6. 계절별 트렌드
- **파일명**: `seasonal_trend.png`
- **설명**: 계절별 여객 이용 패턴 분석
- **차트 유형**: 박스 플롯

### 7. 2024년 vs 2025년 비교
- **파일명**: `year_comparison.png`
- **설명**: 2024년과 2025년 1월 데이터 비교
- **차트 유형**: 막대 차트

## 🎨 차트 스타일 가이드

### 색상 팔레트
- **FSC**: 파란색 계열 (#1f77b4, #2ca02c)
- **LCC**: 주황색 계열 (#ff7f0e, #d62728)
- **배경**: 흰색 (#ffffff)
- **그리드**: 연한 회색 (#f0f0f0)

### 폰트 설정
- **제목**: 16pt, 굵게
- **축 라벨**: 12pt
- **범례**: 10pt
- **한글 폰트**: Malgun Gothic

### 차트 크기
- **기본 크기**: 12x8 인치
- **해상도**: 300 DPI
- **파일 형식**: PNG

## 📋 차트 생성 체크리스트

- [ ] 데이터 전처리 완료
- [ ] 적절한 차트 유형 선택
- [ ] 색상 및 폰트 설정
- [ ] 제목 및 라벨 추가
- [ ] 범례 설정
- [ ] 축 스케일 조정
- [ ] 그리드 및 배경 설정
- [ ] 고해상도로 저장
- [ ] 파일명 규칙 준수

## 🔧 생성 스크립트

차트들은 다음 Python 스크립트로 생성됩니다:

```python
# charts_generator.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 차트 생성 함수들
def create_monthly_trend():
    # 월별 트렌드 차트 생성
    pass

def create_market_share():
    # 시장 점유율 파이 차트 생성
    pass

# ... 기타 차트 생성 함수들
```

## 📁 파일 구조

```
charts/
├── README.md                    # 이 파일
├── monthly_trend.png           # 월별 트렌드
├── market_share_pie.png        # 시장 점유율
├── airline_utilization.png     # 항공사별 이용률
├── route_heatmap.png          # 노선별 히트맵
├── airline_performance.png     # 항공사별 성과
├── seasonal_trend.png         # 계절별 트렌드
└── year_comparison.png        # 연도별 비교
```

---

**생성 예정일**: 2025년 2월 27일  
**차트 개수**: 7개  
**파일 형식**: PNG (고해상도) 