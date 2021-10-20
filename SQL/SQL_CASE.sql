-- CASE WHEN 구문 사용하기
-- A,B,C 컬럼에 각각 삼각형의 변 길이가 담겨 있을 때 어떤 삼각형인지 반환하기
SELECT (CASE WHEN A=B AND B=C THEN "Equilateral"
          WHEN C >= A+B THEN "Not A Triangle"
          WHEN A=B OR A=C OR B=C THEN "Isosceles"
          ELSE "Scalene" END) AS A
    FROM TRIANGLES