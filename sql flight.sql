SELECT * FROM test.tmp2;
UPDATE tmp2 SET 항공사 = '25년 FCC' WHERE 항공사 IN ('KAL', 'AAR');
UPDATE tmp2 SET 항공사 = '25년 LCC' WHERE 항공사 not IN ('25년 FCC');
select 항공사, sum(유아) as '유아탑승객 수', sum(좌석수) as '총 좌석수', sum(여객수) as '탑승객 수', sum(유아)/sum(여객수) as '유아탑승비율', sum(여객수)/sum(좌석수) as '탑승객 비율' from tmp2 group by 항공사 having 항공사 != 0; 
