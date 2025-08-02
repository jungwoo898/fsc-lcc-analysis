# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:03:30 2025

@author: Admin
항공사 운항 실태 조사
2024년 1월~8월 국내노선 여객 이용률



2025년 1월 국내노선 여객 이용률
2016년 국내노선 여객 이용률


항공사별 이용율 추이
항공사 월별 이용객 수 추이

LCC 와 FCC 간 국내선 이용 실태 조사
2024년 1월과 2025년 1월 여객 수 추이 비교
2024년과 2025년 월별 평균 이용률 추이 비교
2024년 월별 여객 수 추이 비교
2024년 월별 평균 이용률 추이 비교


월별 여객 내 유아 승객 비율 비교

group by 해서
좌석수 다 합치고 여객수 다 합치고 유아 이용객 수 다 합치고

월별 좌석수/ 여객 수, 유아이용객/ 여객 수
"""

import pandas as pd
import pymysql

from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb

host = 'localhost'
user = 'root'
password = '0801'
db= 'test'
charset='utf8'

df = pd.read_csv('./data/2024년 1월 국내노선 여객 이용률.csv') # 커넥트 하기 전에 가져오는게 좋음 안 그러면 계속 열어놔야함

"""
쿼리
SELECT * FROM test.tmp2;
UPDATE tmp2 SET 항공사 = '25년 FCC' WHERE 항공사 IN ('KAL', 'AAR');
UPDATE tmp2 SET 항공사 = '25년 LCC' WHERE 항공사 not IN ('25년 FCC');
select 항공사, sum(유아) as '유아탑승객 수', sum(좌석수) as '총 좌석수',
sum(여객수) as '탑승객 수', sum(유아)/sum(여객수) as '유아탑승비율', sum(여객수)/sum(좌석수) as '탑승객 비율' from tmp2 group by 항공사 having 항공사 != 0;
"""


engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db}") #db는 db명 적는것 host랑 password 엮어주기 위해 @작성
conn = engine.connect()

#숫자만 계속 변경
df25.to_sql(name ='tmp2', con=engine, if_exists = 'replace', index=False)




df2 = pd.read_csv('./data/2024년 2월 국내노선 여객 이용률.csv')
df3 = pd.read_csv('./data/2024년 3월 국내노선 여객 이용률.csv')
df4 = pd.read_csv('./data/2024년 4월 국내노선 여객 이용률.csv')
df5 = pd.read_csv('./data/2024년 5월 국내노선 여객 이용률.csv')
df6 = pd.read_csv('./data/2024년 6월 국내노선 여객 이용률.csv')
df7 = pd.read_csv('./data/2024년 7월 국내노선 여객 이용률.csv')
df8 = pd.read_csv('./data/2024년 8월 국내노선 여객 이용률.csv')
df25 = pd.read_csv('./data/한국공항공사_국내노선 여객 월별 이용률_20250131.csv')
# 결국 노가다를 택함 외부에서 저장 후 가져오기
jan = pd.read_csv('./dt/1.csv') 

conn.close()
for i in (1,2,3,4,5,6,7,8,25) :
    {i}.format = pd.read_csv(f'./dt/{i}.csv').format

dfs = {f'df{i}': pd.read_csv(f'./dt/{i}.csv', index_col=0) for i in (1 ,25)}
dfa = {f'df{i}': pd.read_csv(f'./dt/{i}.csv', index_col=0) for i in (1,2,3,4,5,6,7,8)}
import matplotlib.pyplot as plt


import pandas as pd

flight24 = pd.concat(dfa.values(), ignore_index=False)
flight = pd.concat(dfs.values(), ignore_index=False)

# 월별 비교
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    print('Check your OS system')


    flight24.plot(kind='bar', y='유아탑승객 수', legend=False, title='항공사 및 월별 유아탑승객 수')
    
    # 4. 레이블 설정
    plt.xlabel('항공사')
    plt.ylabel('유아탑승객 수')
    plt.grid(True)
    
    # 5. 그래프 출력
    plt.show()

from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    print('Check your OS system')


    flight24.plot(kind='bar', y='탑승객 수', legend=False, title='월별 탑승객 수' , color = ['skyblue','pink'])
    

# 24년
flight24.plot(kind='bar', y='탑승객 수', legend=False, title='월별 탑승객 수' , color = ['skyblue','pink'])
    
    plt.xlabel('항공사')
    plt.ylabel('탑승객 수')
    plt.grid(True)
    
    plt.show()
    
    
#
flight.plot(kind='bar', y='탑승객 수', legend=False, title='월별 탑승객 수' , color = ['skyblue','pink'])
    
plt.xlabel('항공사')
plt.ylabel('탑승객 수')
plt.grid(True)
    
plt.show()
    plt.show()
    
    
    
    import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터
data = {
    '항공사': ['A', 'B', 'C'],
    '1월 탑승객 비율': [0.6, 0.7, 0.8],
    '2월 탑승객 비율': [0.4, 0.3, 0.2]
}

df = pd.DataFrame(data)
df.set_index('항공사', inplace=True)


flight24.plot(kind='bar', stacked=True, title='항공사별 탑승객 비율', color=['skyblue', 'pink'])
plt.xlabel('항공사')
plt.ylabel('비율')
plt.grid(True)
plt.show()

a = flight.loc[:, ['탑승객 수','유아탑승객 수']]

a.plot(kind='bar', stacked=True, title='항공사별 탑승객 비율', color=['skyblue', 'pink'])
plt.xlabel('항공사')
plt.ylabel('비율')
plt.grid(True)

plt.show()


flight24.plot(kind='bar', stacked=True, title='항공사별 탑승객 비율', color=['skyblue', 'pink'])
plt.xlabel('항공사')
plt.ylabel('비율')
plt.grid(True)
plt.show()

pd.csv