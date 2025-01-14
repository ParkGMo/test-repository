-- 트리거
--  자동으로 실행되는 것

-- INSERT UPDATE DELETE 발생시 실행 되는 코드
-- ex 탈퇴가 되면 자동으로 탈퇴 테이블로 저장!

USE market_db;
CREATE TABLE IF NOT EXISTS trigger_table (id INT, txt VARCHAR(10));
INSERT INTO trigger_table VALUES(1, '레드벨뱃');
INSERT INTO trigger_table VALUES(2, '잇지');
INSERT INTO trigger_table VALUES(3, '블랙핑크');

DROP TRIGGER IF EXISTS myTrigger;
-- DELETE 트리거
DELIMITER $$
CREATE TRIGGER myTrigger -- 트리거 이름
    AFTER DELETE -- 삭제후에 작동하도록 지정
    ON trigger_table -- 트리거를 부착할 테이블
    FOR EACH ROW -- 각 행마다 적용시간
BEGIN
    SET @msg = "가수 그룹이 삭제됨"; -- 트리거 실행시 작동되는 코드들
END $$
DELIMITER ;

SET @msg = "";
INSERT INTO trigger_table VALUES (4, '마마무'); -- 삽입이라 트리거 함수의 결과 X
SELECT @msg;
UPDATE trigger_table SET txt = '블핑' WHERE id = 3; -- 수정이라 트리거 함수의 결과 X
SELECT @msg;

DELETE FROM trigger_table WHERE id = 4;
SELECT @msg;

-- 트리거 -> 백업
USE market_db;
CREATE TABLE singer (SELECT mem_id, mem_name, mem_number, addr FROM member);

DROP TABLE IF EXISTS backup_singer;
CREATE TABLE backup_singer
(
    mem_id CHAR(8) NOT NULL,
    mem_name VARCHAR(10) NOT NULL,
    mem_number INT NOT NULL,
    addr CHAR(2) NOT NULL,
    modType CHAR(2),
    modDate DATE,
    modUser VARCHAR(20)    
);

-- UDDATE TRIGGER
DROP TRIGGER IF EXISTS singer_updateTrg;
DELIMITER $$
CREATE TRIGGER singer_updateTrg
    AFTER UPDATE
    ON singer
    FOR EACH ROW
BEGIN
    -- 변경되기 전 저장을 위해 OLD. 으로 가져온다.
    INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name, OLD.mem_number,
    OLD.addr, '수정', CURDATE(), CURRENT_USER());
END $$
DELIMITER ;

-- DELETE TRIGGER
DROP TRIGGER IF EXISTS singer_deleteTrg;
DELIMITER $$
CREATE TRIGGER singer_deleteTrg
    AFTER DELETE
    ON singer
    FOR EACH ROW
BEGIN
    -- 변경되기 전 저장을 위해 OLD. 으로 가져온다.
    INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name, OLD.mem_number,
    OLD.addr, '삭제', CURDATE(), CURRENT_USER());
END $$
DELIMITER ;
-- 테이블 당 여러개 트리거 가능!!

UPDATE singer SET addr = "영국" WHERE mem_id = 'BLK';
DELETE FROM singer WHERE mem_number >= 7;

-- 데이터의 무결성을 보장 --> 트리거
SELECT * FROM singer;
SELECT * FROM backup_singer;

TRUNCATE backup_singer ; -- 모든 데이터를 지우지만 트리거를 작동 시키지 않는다.
-- 트리거를 작동 시키지 않는다.
SELECT * FROM backup_singer;