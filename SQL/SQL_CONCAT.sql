/*
다음과 같은 형식으로 출력하기
Aamina(D) 
Ashley(P) 
Belvet(P) 
Britney(P)
There are a total of 3 doctors. 
There are a total of 4 actors.
*/

SELECT CONCAT(NAME,'(',LEFT(Occupation,1),')') FROM OCCUPATIONS ORDER BY NAME ASC;
SELECT CONCAT("There are a total of ", Count(Occupation), " ",LOWER(Occupation), "s.") FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY Count(Occupation) ASC