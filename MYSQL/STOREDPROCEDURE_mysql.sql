-- 스토어등 프로시저 
--  ( == 파이썬, 자바스크립트 함수)
-- SQL 과 프로그램이 기능 연결

--  ex) 커피자판기(스토어 프로시저 생성)  -> 커피 뽑기(스토어 프로시저 호출)

-- 필수 항목
-- DELIMITER $$
-- CREATE PROCEDURE 스토어드_프로시저_이름 (IN 또는 OUT 매개변수)
-- BEGIN
--      이 부분에 SQL 프로그래밍을 코드를 작성
-- END $$
-- DELIMITER ;

USE market_db;
DROP PROCEDURE IF EXISTS user_proc;

-- 프로시저를 생성 (커피자판기)
DELIMITER $$ 
CREATE PROCEDURE user_proc ()
BEGIN
    SELECT * FROM member; -- 스토어 프로시저 내용
END $$
DELIMITER ;

-- 프로시저를 호출 (커피 뽑기)
CALL user_proc();

-- 프로시저 삭제
DROP PROCEDURE user_proc;


-- 입력 매개변수(IN  -- OUT) == javascript(함수 매개변수)
USE market_db;
DROP PROCEDURE IF EXISTS user_proc1
DELIMITER $$ 
CREATE PROCEDURE user_proc1 (IN userName VARCHAR(10))
BEGIN
    SELECT * FROM member WHERE mem_name = userName; -- 스토어 프로시저 내용
END $$
DELIMITER ;

CALL user_proc1('에이핑크')

DROP PROCEDURE IF EXISTS user_proc2
DELIMITER $$ 
CREATE PROCEDURE user_proc2 (
        IN userNumber INT,
        IN userHeight INT )
BEGIN
    SELECT * FROM member 
    WHERE mem_number > userNumber AND height > userHeight; -- 스토어 프로시저 내용
END $$
DELIMITER ;

CALL user_proc2(6, 165);


USE market_db;
DROP PROCEDURE IF EXISTS user_proc3;
DELIMITER $$ 
CREATE PROCEDURE user_proc3 (
    IN txtValue CHAR(10),
    OUT outValue INT )
BEGIN
    INSERT INTO noTable VALUES(NULL, txtValue);
    SELECT MAX(id) INTO outValue FROM noTable; -- MAX(id) 값이 outValue로 전달
END $$
DELIMITER ;
-- 없는 테이블도 프로지저 내용에서는 가능

DESC noTable; -- 테이블이 확인! , 그러나 테이블이 없기때문에 오류!

CREATE TABLE IF NOT EXISTS noTable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    txt CHAR(10)
);

CALL user_proc3("테스트1", @myValue); -- @myValue는 OUT으로 밖에서 사용가능
SELECT CONCAT("입력된 ID 값 ==>", @myValue); -- @myValue는 OUT으로 밖에서 사용가능


-- 프로시저 if문
USE market_db;
DROP PROCEDURE IF EXISTS ifelse_proc1;
DELIMITER $$ 
CREATE PROCEDURE ifelse_proc1 (IN memName VARCHAR(10))
BEGIN
    DECLARE debutYear INT; -- 변수 선언
    SELECT YEAR(debut_date) INTO debutYear FROM member
        WHERE mem_name = memName;
    IF (debutYear >= 2015) THEN
        SELECT '신인 가수네요. 화이팅 하세요!' AS '메세지';
    ELSE
        SELECT '노래를 많이 쓴 가수네요. 감사합니다!' AS '메세지';
    END IF;
END $$
DELIMITER ;

CALL ifelse_proc1('소녀시대');

-- 프로시저 while문
USE market_db;
DROP PROCEDURE IF EXISTS while_proc;
DELIMITER $$
CREATE PROCEDURE while_proc ()
BEGIN
    DECLARE hap INT ; -- 합계
    DECLARE num INT ; -- 1부터 100까지 증가
    SET hap = 0; -- 합계 초기화
    SET num = 1;

    WHILE num <= 100 DO -- 100까지 반복
        SET hap = hap + num;
        SET num = num + 1; -- 숫자 증가
    END WHILE;

    SELECT hap AS '1부터 100까지의 합';
END $$
DELIMITER ;

CALL while_proc();

-- 프로시저 동적SQL문
USE market_db;
DROP PROCEDURE IF EXISTS dynamic_proc;
DELIMITER $$
CREATE PROCEDURE dynamic_proc (IN tableName VARCHAR(20))
BEGIN
    SET @sqlQuery = CONCAT('SELECT * FROM ', tableName);
    PREPARE myQuery FROM @sqlQuery;
    EXECUTE myQuery;
    DEALLOCATE PREPARE myQuery;
END $$
DELIMITER ;

CALL dynamic_proc('member');
CALL dynamic_proc('buy');
