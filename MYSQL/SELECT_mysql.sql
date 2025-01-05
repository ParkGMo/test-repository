USE market_db;
-- USE 가 없다면 market_db.member 
-- USE 가 있다면 member 

SELECT * 
FROM market_db.member 
WHERE mem_name = '블랙핑크';

SELECT addr, height, debut_date
FROM member ;

SELECT height 키, debut_date "데뷔 일자"
FROM member ;

SELECT *
FROM member 
WHERE mem_number <= 4;

SELECT mem_id, mem_name
FROM member 
WHERE height <= 162;

SELECT mem_id, height, mem_name
FROM member 
WHERE height <= 162 AND mem_number > 6;

SELECT mem_id, height, mem_name
FROM member 
WHERE height <= 162 OR mem_number > 6;



SELECT mem_name, height
FROM member 
WHERE height >= 162 AND height <= 165;

SELECT mem_name, height
FROM member 
WHERE height between 162 AND  165;



SELECT mem_name, addr
FROM member 
WHERE addr ="경기" OR addr ="전남" OR addr ="경남";

SELECT mem_name, addr
FROM member 
WHERE addr IN("경기","전남", "경남");

SELECT *
FROM member 
WHERE mem_name LIKE "우%";

SELECT *
FROM member 
WHERE mem_name LIKE "__핑크";



