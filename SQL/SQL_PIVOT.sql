-- 직업 열을 기준으로 피벗 테이블로 바꾸고 빈칸에는 NULL을 넣기
-- 각 직업마다 row num을 매긴 후 해당 직업 열에 name 넣기
-- row num으로 groupby 진행하기
SET @r1=0, @r2=0, @r3=0, @r4=0;

SELECT MAX(Doctor), MAX(Professor), MAX(Singer), MAX(Actor) FROM(
    SELECT
    CASE WHEN OCCUPATION='Doctor' THEN (@r1:=@r1+1)
         WHEN OCCUPATION='Actor' THEN (@r2:=@r2+1)
         WHEN OCCUPATION='Singer' THEN (@r3:=@r3+1)
         WHEN OCCUPATION='Professor' THEN (@r4:=@r4+1) END AS RowNumber,
        
        case when Occupation='Doctor' then Name end as Doctor,
        case when Occupation='Professor' then Name end as Professor,
        case when Occupation='Singer' then Name end as Singer,
        case when Occupation='Actor' then Name end as Actor
    FROM OCCUPATIONS
    ORDER BY Name) temp
GROUP BY RowNumber;