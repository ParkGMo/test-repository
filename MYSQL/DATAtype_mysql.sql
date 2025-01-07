-- 정수형
-- TINYINT  : -128 ~ 127 (1 byte)
-- SMALLINT : -32,768 ~ 32,767 (2 byte)
-- INT      : 약 -21억 ~ 21억 (4 byte)
-- BIGINT   : 약 -900억 ~ 900억 (8 byte)

-- 음수 제거
-- TINYINT UNSIGNED -> 음수를 제외한 0 ~ 255 

USE market_db;
CREATE TABLE hongong4 (
    tinyint_col TINYINT,
    smallint_col SMALLINT,
    int_col INT,
    bigint_col BIGINT
)

INSERT INTO hongong4 VALUES(127, 32767, 214748364, 90000000000000000000000000000000)

-- 문자형
-- CHAR(10)    : 10자리가 다 있지 않더라도 10자리 전부 차지 (빠른 속도, 가변X 추천) ex 서울 경기 강원 ...
-- VARCHAR(10) : 10자리가 다 있지 않으면 있는 자리까지 차지 (공간 효율, 가변 추천) ex 블랙핑크 잇지 에스파 ...

-- 대량 데이터 형식
-- CHAR    : 255 까지 가능
-- VARCHAR : 16383 까지 가능

CREATE TABLE big_table(
    data1 CHAR(256),
    data2 VARCHAR(16384)
)

-- 더 많고 큰 데이터를 저장하기 위해서는
-- LONGTEXT : 긴 글자 
-- LONGBLOB : 큰 파일

CREATE DATABASE netflix_db;
USE netflix_db;
CREATE TABLE movie(
    movie_id INT,
    movie_title VARCHAR(30),
    movie_director VARCHAR(20),
    movie_star VARCHAR(20),
    movie_script LONGTEXT,
    movie_film LONGBLOB
);

-- 실수형
-- FLOAT  : 소수점 아래 7자리까지 표현  (4 bytes) ex) 시력
-- BOUBLE : 소수점 아래 15자리까지 표현 (8 bytes)

-- 날짜형
-- DATE  : YYYY-MM-DD (3 bytes)
-- TIME  : HH:MM:SS (3 bytes)
-- DATETIME : YYYY-MM-DD HH:MM:SS (8 bytes)

-- 변수 사용
--  임시 저장소
--  SET @변수이름 = 변수의 값
--  SELECT @변수이름
USE market_db;
SET @myVar1 = 5;
SET @myVar2 = 4.25;

SELECT @myVar1;
SELECT @myVar1 + @myVar2;

SET @txt = "가수 이름 ==> ";
SET @height = 166;

SELECT @txt, mem_name FROM member WHERE height > @height;


SET @count = 3;
SELECT mem_name, height FROM member ORDER BY height LIMIT @count;
-- 오류 발생

SET @count = 3;
-- 준비단계
PREPARE mySQL FROM "SELECT mem_name, height FROM member ORDER BY height LIMIT ?";
-- '?'에 값을 넣어준다
EXECUTE mySQL USING @count

-- 데이터 형 변환

-- CAST : 데이터 형을 변환
-- CAST( 값 AS 데이터_형식[(길이)])

-- CONVERT : 데이터 형을 변환
-- CONVERT(값, 데이터_형식[(길이)])

SELECT AVG(price) "평균 가격" FROM buy;

SELECT CAST(AVG(price) AS SIGNED) '평균 가격' FROM buy;
SELECT CONVERT(AVG(price), SIGNED) '평균 가격' FROM buy;

SELECT CAST("2025$01$07" AS DATE);
SELECT CAST("2025/01/07" AS DATE);
SELECT CAST("2025%01%07" AS DATE);
SELECT CAST("2025@01@07" AS DATE);

SELECT num, CONCAT(CAST(price AS CHAR), "x", CAST(amount AS CHAR), "=") "가격 x 수량",
       price * amount AS "총 가격"
    FROM buy;

SELECT "100" + "200"; -- 정수로 변환 (암시적인 형변환)
SELECT CONCAT('100' + '200'); -- 문자와 문자 연결
SELECT CONCAT(100,'200'); -- 문자로 연결
SELECT 1 > "2mega"; -- 정수인 2로 변환되어서 비교
SELECT 3 > "2MEGA"; -- 정수인 2로 변환되어서 비교
SELECT 0 = "mega2"; -- 문자는 0으로 변환됨