-- IF문 (조건문)

-- IF <조건식> THEN
--     SQL문장들
-- END IF;

USE market_db;
DROP PROCEDURE IF EXISTS ifProc1; -- 기존에 만든적이 있다면 삭제
DELIMITER $$
CREATE PROCEDURE ifProc1()
BEGIN
    IF 100 = 100 THEN
        SELECT '100은 100과 같습니다.';
    ELSE
        SELECT '100은 100과 다릅니다.';
    END IF;
END $$
DELIMITER ;
CALL ifProc1();

DROP PROCEDURE IF EXISTS ifProc2; -- 기존에 만든적이 있다면 삭제
DELIMITER $$
CREATE PROCEDURE ifProc2()
BEGIN
    -- 안에서 변수 지정는 @ 생략 
    DECLARE my_num INT ;
    SET my_num =200;
    IF my_num = 100 THEN
        SELECT '100입니다.';
    ELSE
        SELECT '100이 아닙니다.';
    END IF;
END $$
DELIMITER ;
CALL ifProc2();

DROP PROCEDURE IF EXISTS ifProc3; -- 기존에 만든적이 있다면 삭제
DELIMITER $$
CREATE PROCEDURE ifProc3()
BEGIN
    DECLARE debutDate DATE ; -- 데뷔일
    DECLARE curDate DATE ; -- 오늘
    DECLARE days INT ; -- 활동한 일수

    SELECT debut_date INTO debutDate -- debut_date가 debutDate로 들어간다.
        FROM market_db.member
        WHERE mem_id = 'APN' ;

    SET curDATE = CURRENT_DATE(); -- 현재 날짜
    SET days = DATEDIFF(curDATE, debutDate); -- 날짜의 차이, 열 단위

    IF (days/365) >= 5 THEN -- 5년이 지났다면
        SELECT CONCAT("데뷔한지", days, "일이나 지났습니다. 핑순이들 축하합니다.");
    ELSE
        SELECT "데뷔한지" + days + "일 남아 있습니다. 핑순이들 화이팅~.";
    END IF;
END $$
DELIMITER ;
CALL ifProc3();

-- CASE문 (다중분기)

-- CASE <변수>
--     WHEN <비교값> THEN <실행할 SQL>
--     [WHEN <비교값> THEN <실행할 SQL>]
--     ...
--     [ELSE <실행할 SQL>]
-- END CASE;

DROP PROCEDURE IF EXISTS caseProc1; -- 기존에 만든적이 있다면 삭제
DELIMITER $$
CREATE PROCEDURE caseProc1()
BEGIN
    DECLARE point INT ;
    DECLARE credit CHAR(1) ;
    SET point = 88;

    CASE
        WHEN point >= 90 THEN
            SET credit = 'A';
        WHEN point >= 80 THEN
            SET credit = 'B';
        WHEN point >= 70 THEN
            SET credit = 'C';
        WHEN point >= 60 THEN
            SET credit = 'D';
        ELSE
            SET credit = 'F';
    END CASE;

    SELECT CONCAT('취득점수 ==> ', point), CONCAT("학점 ==> ", credit);
END $$
DELIMITER ;
CALL caseProc1();


SELECT mem_id, SUM(price*amount) "총 구매액"
    FROM buy
    GROUP BY mem_id
    ORDER BY SUM(price*amount) DESC ;

SELECT B.mem_id, M.mem_name, SUM(price*amount) "총 구매액"
    FROM buy B 
        INNER JOIN member M 
        ON B.mem_id = M.mem_id
    GROUP BY B.mem_id
    ORDER BY SUM(price*amount) DESC ;


SELECT B.mem_id, M.mem_name, SUM(price*amount) "총 구매액"
    FROM buy B 
        RIGHT OUTER JOIN member M 
        ON B.mem_id = M.mem_id
    GROUP BY M.mem_id
    ORDER BY SUM(price*amount) DESC ;

SELECT M.mem_id, M.mem_name, SUM(price*amount) "총 구매액",
       CASE 
           WHEN SUM(price*amount) >= 1500 THEN 'VIP'
           WHEN SUM(price*amount) >= 1000 THEN 'Gold'
           WHEN SUM(price*amount) >= 1 THEN 'Silver'
           ELSE 'Normal'
        END "VIP등급"
    FROM buy B 
        RIGHT OUTER JOIN member M 
        ON B.mem_id = M.mem_id
    GROUP BY M.mem_id
    ORDER BY SUM(price*amount) DESC ;

-- WHILE문

-- DECLARE <변수> INT DEFAULT 0;
-- WHILE <조건> DO
--     <실행할 SQL>
--     SET <변수> = <변수> + 1;
-- END WHILE;

DROP PROCEDURE IF EXISTS whileProc1;
DELIMITER $$
CREATE PROCEDURE whileProc1()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE hap INT ;

    SET i = 1;
    SET hap = 0;
    
    WHILE (i <= 100) DO
        SET hap = hap + i;
        SET i = i + 1;
    END WHILE;
    
    SELECT "1부터 100까지의 합 ==> ", hap;
END $$
DELIMITER ;
CALL whileProc1();

DROP PROCEDURE IF EXISTS whileProc2;
DELIMITER $$
CREATE PROCEDURE whileProc2()
BEGIN
    DECLARE i INT ;
    DECLARE hap INT ;

    SET i = 1;
    SET hap = 0;
    
    myWhile: -- 원하는 이름 지정, 밑의 while문을 지칭
    WHILE (i <= 100) DO
        IF (i%4 = 0) THEN
            SET i = i + 1;
            ITERATE myWhile; -- myWhile로 이동
        END IF;
        
        SET hap = hap + i;
        IF (hap > 1000) THEN
            LEAVE myWhile; -- 지정한 label문을 떠남, while 종료
        END IF;
        SET i = i + 1;
    END WHILE;
    
    SELECT "1부터 100까지의 합(4의 배수 제외), 1000넘으면 종료 ==> ", hap;
END $$
DELIMITER ;
CALL whileProc2();


-- LOOP문

-- DECLARE <변수> INT DEFAULT 0;
-- LOOP
--     <실행할 SQL>
--     SET <변수> = <변수> + 1;
--     IF <조건> THEN
--         LEAVE LOOP; -- LOOP 종료
--     END IF;
-- END LOOP;



-- 동적 SQL문

-- PREPARE myQuery FROM 'SELECT * FROM buy WHERE mem_id =?';
-- SET @mem_id = 'APN';
-- EXECUTE myQuery USING @mem_id;
-- DEALLOCATE PREPARE myQuery;

DROP TABLE IF EXISTS gate_table;
CREATE TABLE gate_table (id INT AUTO_INCREMENT PRIMARY KEY, entry_time DATETIME);

SET @curDate = CURRENT_DATE();

PREPARE myQuery FROM "INSERT INTO gate_table VALUES(NULL, ?)";
EXECUTE myQuery USING @curDATE;
DEALLOCATE PREPARE myQuery;

SELECT * FROM gate_table;