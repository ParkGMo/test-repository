-- 스토어드 함수
--  프로시저와 비슷, 다양한 함수를 제공
-- SUM(), CAST(), CONCAT(),CURRENT_DATE() 등

-- DELIMITER $$
-- CREATE FUNCTION 스토어드드_함수_이름(매개변수)
--     RETURNS 반환타입
-- BEGIN

--     이 부분에 프로그래밍 코딩
--     RETURNS 반환값;

-- END $$
-- DELIMITER ;

-- STORED FUNCTION 사용 
-- SELECT로 호출
-- SELECT SUM(store_price) AS total_price
-- FROM products

SET GLOBAL log_bin_trust_function_creators = 1;
-- > MYSQL에서 사용하는 변수(형식상) 추후 계속 설정 유지

USE market_db;
DROP FUNCTION IF EXISTS sumFunc;
DELIMITER $$
CREATE FUNCTION sumFunc(number1 INT, number2 INT)
    RETURNS INT
BEGIN

    RETURN number1 + number2;

END $$
DELIMITER ;

SELECT sumFunc(100, 200) AS '합계';


DROP FUNCTION IF EXISTS calcYearFunc;
DELIMITER $$
CREATE FUNCTION calcYearFunc(dYear INT)
    RETURNS INT
BEGIN
    DECLARE runYear INT; -- 활동기간
    SET runYear = YEAR(CURDATE()) - dYear;
    RETURN runYear;

END $$
DELIMITER ;

SELECT calcYearFunc(2010) AS '활동기간';

-- 변수로 대입 가능
SELECT calcYearFunc(2007) INTO @debut2007;
SELECT calcYearFunc(2013) INTO @debut2013;

SELECT @debut2007-@debut2013 AS "2007과 2013 차이";


-- 쿼리안 결과로 사용 가능
SELECT mem_id, mem_name, calcYearFunc(YEAR(debut_date)) AS '활동 횟수'
    FROM member;

-- 함수 삭제
DROP FUNCTION IF EXISTS calcYearFunc;

-- 커서(CURSOR)
-- 한 행씩 처리하는 개념
-- 전체 회원의 평균을 구함
-- 과정
-- 1. CURSOR 선언
-- 2. 반복 조건 선언
-- 3. CURSOR 열기
--   * 행 마다 반복 시작
-- 4. 데이터 가져오기 
-- 5. 데이터 처리하기 
--   * 행 마다 반복 끝
-- 6. CURSOR 닫기

-- 단계별 실습
-- 1 가장 처음으로는 초기화 진행
DECLARE memNumber INT;
DECLARE cnt INT DEFAULT 0;
DECLARE totNumber INT DEFAULT 0;

-- 2 변수 준비
DECLARE end0fRow BOOLEAN DEFAULT FALSE;

-- 3 커서 선언하기
DECLARE memberCursor CURSOR FOR 
    SELECT mem_number FROM member;

-- 4 반복 조건 선언
DECLARE CONTINUE HANDLER FOR NOT FOUND SET end0fRow = TRUE;
--  > 행의 끝이 왔을 떄 end0fRow = TRUE로 하여 끝내라

-- 5 CURSOR 열기
OPEN memberCursor;

-- 6 행 반복하기
cursor_loop: LOOP
    -- 이부분 반복
END LOOP cursor_loop;