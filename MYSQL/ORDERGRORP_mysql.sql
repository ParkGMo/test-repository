--  꼭! 순서대로 작성
-- SELECT 열 이름
    -- FROM 테이블 이름
    -- WHERE 조건식
    -- GROUP BY 열 이름
    -- HAVING 조건식
    -- ORDER BY 열 이름
    -- LIMIT 숫자

use MARKET_DB;

SELECT mem_id, mem_name, debut_date
    FROM member
    -- ORDER BY debut_date ASC; default
    ORDER BY debut_date DESC;

SELECT mem_id, mem_name, debut_date, height
    FROM member
    WHERE height >= 164;
    ORDER BY height DESC, debut_date ASC;
    --  ORDER BY 앞 조건 우선순위

SELECT *
    FROM member
    LIMIT 3;

SELECT mem_name, debut_date
    FROM member
    ORDER BY debut_date;
    LIMIT 3;

SELECT mem_name, height
    FROM member
    ORDER BY height DESC
    LIMIT 3, 2;

SELECT addr FROM member;

-- 중복 제거 DISTINCT
SELECT DISTINCT addr FROM member

-- GROUP BY : 묶어주는 역할

-- 집게 함수
-- SUM()
-- AVG()
-- MIN()
-- MAX()
-- COUNT()
-- COUNT(DISTINCT) 중복 한개만 인정

SELECT mem_id, SUM(amount) FROM buy GROUP BY mem_id
-- 열 이름 부여
SELECT mem_id "회원 아이디", SUM(amount) "총 구매 개수" FROM buy GROUP BY mem_id

SELECT mem_id, AVG(amount) FROM buy GROUP BY mem_id
SELECT mem_id, MIN(amount) FROM buy GROUP BY mem_id

SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
    FROM buy GROUP BY mem_id;

SELECT AVG(amount) "평균 구매 개수" FROM buy;
SELECT AVG(amount) "평균 구매 개수" FROM buy GROUP BY mem_id;

SELECT COUNT(*)  FROM member;
SELECT COUNT(phone1) "연락처가 있는 회원" FROM member;


-- HAVING : GROUP BY 결과에 대한 조건

SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
    FROM buy
    GROUP BY mem_id
    HAVING SUM(price*amount) >= 1000;

SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
    FROM buy
    GROUP BY mem_id
    HAVING SUM(price*amount) >= 1000
    ORDER BY SUM(price*amount) DESC;