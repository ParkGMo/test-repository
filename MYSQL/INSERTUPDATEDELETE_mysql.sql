-- INSERT : 테이블 추가
-- UPDATE : 정보 수정
-- DELETE : 정보 삭제

use market_db;

CREATE TABLE hongong1 (toy_id INT, toy_name CHAR(4), age INT);

INSERT INTO hongong1 VALUES (1, '우디', 25);
INSERT INTO hongong1(toy_id, toy_name) VALUES (2, '버즈');
INSERT INTO hongong1(toy_name, age, toy_id) VALUES ('제시', 20 , 3);
SELECT * FROM hongong1;

-- AUTO_INCREMENT(중복 되지 않는 값 부여 ex id) 뒤에는 반드시 PRIMARY KEY(중복이 되지 않는 키)
CREATE TABLE hongong2 (
    toy_id INT AUTO_INCREMENT PRIMARY KEY, 
    toy_name CHAR(4), 
    age INT);

INSERT INTO hongong2 VALUES (NULL,'보핍', 30);
INSERT INTO hongong2 VALUES (NULL,'슬링키', 22);
INSERT INTO hongong2(toy_name, age) VALUES ('렉스', 21);
SELECT * FROM hongong2;

-- 마지막 id 
SELECT LAST_INSERT_ID()

-- AUTO_INCREMENT를 100부터
ALTER TABLE hongong2 AUTO_INCREMENT=100;
INSERT INTO hongong2 VALUES (NULL, '재남', 35);
SELECT * FROM hongong2;


CREATE TABLE hongong3 (
    toy_id INT AUTO_INCREMENT PRIMARY KEY, 
    toy_name CHAR(4), 
    age INT);
ALTER TABLE hongong3 AUTO_INCREMENT=1000;
-- 3씩 건너띄고 
SET @@auto_increment_increment = 3;

INSERT INTO hongong3 VALUES (NULL,'토마스', 20);
INSERT INTO hongong3 VALUES (NULL,'제임스', 23);
INSERT INTO hongong3 VALUES (NULL,'고든', 25);
SELECT * FROM hongong3;

-- INSERT INTO , SELECT문 전체 입력

SELECT COUNT(*) FROM world.city;

DESC world.city

SELECT * FROM world.city LIMIT 3;

CREATE TABLE city_popul (city_name CHAR(35), population INT);

INSERT INTO city_popul
    SELECT Name, Population FROM world.city;

USE market_db;

SELECT * FROM city_popul WHERE city_name = 'Seoul';

UPDATE city_popul
    SET city_name = '서울'
    WHERE city_name = 'Seoul';
SELECT * FROM city_popul WHERE city_name = '서울';

UPDATE city_popul
    SET city_name = '뉴욕', population = 0
    WHERE city_name = 'New York';
    -- WHERE 문이 없으면 모든 데이터가 뉴욕과 0으로 바뀐다.
SELECT * FROM city_popul WHERE city_name = '뉴욕';

-- 모든 인구수가 나누어진다.WHERE 문이 없어서!
UPDATE city_popul
    SET population = population / 10000;
SELECT * FROM city_popul LIMIT 5;


-- DELETE
DELETE FROM city_popul LIKE "New%";

DELETE FROM city_popul 
    WHERE city_name LIKE "New%"
    LIMIT 5;
