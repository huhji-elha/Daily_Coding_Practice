-- 총 급여의 MAX값과 개수 구하기
SELECT salary*months earnings, Count(*) FROM Employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;